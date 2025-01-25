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
    accessories_json = json.dumps({
        a.name: float(a.price) for a in accessories
    })
    return render(request, 'home.html', {
        'bars': bars,
        'accessories': accessories,
        'accessories_json': accessories_json
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

@csrf_exempt
def save_prices(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            table = data.get('table')
            items = data.get('data')
            
            # Update prices in database
            for item in items:
                name = item['name']
                price = float(item['price'])
                
                if table == 'accessoriesTable':
                    Accessory.objects.filter(name=name).update(price=price)
                elif table == 'barsTable':
                    Bar.objects.filter(name=name).update(price=price)
                elif table == 'redeauTable':
                    RedeauAccessory.objects.filter(name=name).update(price=price)
            
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
