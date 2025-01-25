from django.core.management.base import BaseCommand
from core.models import Accessory

class Command(BaseCommand):
    help = 'List all accessories and their prices'

    def handle(self, *args, **options):
        accessories = Accessory.objects.all()
        
        if not accessories.exists():
            self.stdout.write(self.style.WARNING('No accessories found'))
            return
            
        for accessory in accessories:
            self.stdout.write(
                f"{accessory.name}: {accessory.price}"
            )
