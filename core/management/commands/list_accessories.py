from django.core.management.base import BaseCommand
from core.models import Accessory, RedeauAccessory

class Command(BaseCommand):
    help = 'List all accessories with their prices and calculate totals'

    def handle(self, *args, **kwargs):
        width = 10  # meters
        height = 10  # meters
        
        # List regular accessories and calculate cost
        accessories = Accessory.objects.all()
        accessory_prices = {a.name.lower(): float(a.price) for a in accessories}
        
        if not accessories.exists():
            self.stdout.write(self.style.WARNING('No accessories found'))
        else:
            self.stdout.write(self.style.SUCCESS('\nRegular Accessories:'))
            for accessory in accessories:
                self.stdout.write(f"{accessory.name}: {accessory.price}")
            
            # Calculate accessory cost
            accessory_cost = (
                accessory_prices.get('cremon', 0) +
                accessory_prices.get('kit cremon', 0) +
                accessory_prices.get('ecair', 0) * 8 +
                accessory_prices.get('pomelle', 0) * 2 +
                accessory_prices.get('silcon', 0) +
                (accessory_prices.get('join baitement', 0) * (height + width) * 4) +
                (accessory_prices.get('join vitrage', 0) * (height + width) * 4) +
                accessory_prices.get('vitrage', 0) * (height * width)
            )
            self.stdout.write(self.style.SUCCESS(f'\nTotal Accessory Cost: {accessory_cost:.2f}'))

        # List redeau accessories and calculate total
        redeau_accessories = RedeauAccessory.objects.all()
        
        if not redeau_accessories.exists():
            self.stdout.write(self.style.WARNING('\nNo redeau accessories found'))
        else:
            self.stdout.write(self.style.SUCCESS('\nRedeau Accessories:'))
            
            # Get prices for each component
            redeau_prices = {a.name.lower(): float(a.price) for a in redeau_accessories}
            
            # Calculate total using the formula
            total_redeau = (
                redeau_prices.get('rolange axe', 0) +
                redeau_prices.get('axe', 0) * (width - 0.1) +
                redeau_prices.get('moteur', 0) +
                (2 * redeau_prices.get('tirent', 0)) +
                redeau_prices.get('glissiére', 0) * (height * 2 + 0.12) +
                redeau_prices.get('lamet', 0) * (((height + 0.11) / 5.5) * width) +
                redeau_prices.get('lame finale', 0) * width
            )
            
            # Display individual prices
            for accessory in redeau_accessories:
                self.stdout.write(f"{accessory.name}: {accessory.price}")
            
            # Display calculated total
            self.stdout.write(self.style.SUCCESS(f'\nTotal Redeau Price: {total_redeau:.2f}'))

        total_count = accessories.count() + redeau_accessories.count()
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully listed {total_count} accessories'))
