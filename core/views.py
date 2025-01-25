from django.shortcuts import render
from rest_framework import viewsets
from .models import Accessory, Bar, RedeauAccessory
from .serializers import AccessorySerializer, BarSerializer, RedeauAccessorySerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    bars = Bar.objects.all()
    accessories = Accessory.objects.all()
    redeau_accessories = RedeauAccessory.objects.all()
    accessories_json = json.dumps({
        a.name: float(a.price) for a in accessories
    })
    redeau_json = json.dumps({
        r.name: float(r.price) for r in redeau_accessories
    })
    return render(request, 'home.html', {
        'bars': bars,
        'accessories': accessories,
        'accessories_json': accessories_json,
        'redeau_json': redeau_json
    })

def tables(request):
    accessories = Accessory.objects.all()
    bars = Bar.objects.all()
    redeau_accessories = RedeauAccessory.objects.all()
    
    context = {
        'accessories': accessories,
        'bars': bars,
        'redeau_accessories': redeau_accessories
    }
    return render(request, 'tables.html', context)

from django.db import transaction

@csrf_exempt
def save_prices(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            table = data.get('table')
            items = data.get('data')
            
            with transaction.atomic():
                for item in items:
                    name = item['name']
                    price = float(item['price'])
                    
                    if table == 'accessoriesTable':
                        acc = Accessory.objects.filter(name=name).first()
                        if acc:
                            print(f"Updating {name} from {acc.price} to {price}")
                            acc.price = price
                            acc.save()
                            print(f"New price: {Accessory.objects.get(name=name).price}")
                    elif table == 'barsTable':
                        bar = Bar.objects.filter(name=name).first()
                        if bar:
                            print(f"Updating {name} from {bar.price} to {price}")
                            bar.price = price
                            bar.save()
                            print(f"New price: {Bar.objects.get(name=name).price}")
                    elif table == 'redeauTable':
                        redeau = RedeauAccessory.objects.filter(name=name).first()
                        if redeau:
                            print(f"Updating {name} from {redeau.price} to {price}")
                            redeau.price = price
                            redeau.save()
                            print(f"New price: {RedeauAccessory.objects.get(name=name).price}")
                
                return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

class RedeauAccessoryViewSet(viewsets.ModelViewSet):
    queryset = RedeauAccessory.objects.all()
    serializer_class = RedeauAccessorySerializer
