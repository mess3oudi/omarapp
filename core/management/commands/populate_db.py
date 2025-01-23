from django.core.management.base import BaseCommand
from core.models import Accessory, Bar, RedeauAccessory

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        try:
            # Delete existing records
            Bar.objects.all().delete()
            Accessory.objects.all().delete()
            RedeauAccessory.objects.all().delete()

            # Create sample bars
            bars = [
                Bar(name='402 k', price=49.99),
                Bar(name='405 k', price=79.99),
                Bar(name='102', price=99.99),
                Bar(name='148', price=99.99),
                Bar(name='100', price=99.99),
                Bar(name='404', price=99.99),
                Bar(name='22106', price=99.99),
                Bar(name='22104', price=99.99),
            ]
            Bar.objects.bulk_create(bars)

            # Create sample accessories
            accessories = [
                Accessory(name='Cremon', price=0.00),
                Accessory(name='Piquette', price=0.00),
                Accessory(name='Kit Cremon', price=0.00),
                Accessory(name='Ecair', price=0.00),
                Accessory(name='Pomelle', price=0.00),
                Accessory(name='Bouchon 112', price=0.00),
                Accessory(name='Serrure', price=0.00),
                Accessory(name='Silcon', price=0.00),
                Accessory(name='Join Baitement', price=0.00),
                Accessory(name='Join Vitrage', price=0.00),
                Accessory(name='Vitrage', price=0.00),
                Accessory(name='Kit Verro', price=0.00),
                Accessory(name='Galet', price=0.00),
                Accessory(name='Fermeture', price=0.00),
                Accessory(name='40112', price=0.00),
                Accessory(name='22112', price=0.00),
                Accessory(name='166', price=0.00),
                Accessory(name='154', price=0.00),
            ]
            Accessory.objects.bulk_create(accessories)

            # Create sample redeau accessories
            redeau_accessories = [
                RedeauAccessory(name='Rolange axe', price=0.00),
                RedeauAccessory(name='axe', price=0.00),
                RedeauAccessory(name='moteur', price=0.00),
                RedeauAccessory(name='tirent', price=0.00),
                RedeauAccessory(name='glissiére', price=0.00),
                RedeauAccessory(name='lamet', price=0.00),
                RedeauAccessory(name='Lame finale', price=0.00),
            ]
            RedeauAccessory.objects.bulk_create(redeau_accessories)

            self.stdout.write(self.style.SUCCESS('Successfully populated database with clean data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {str(e)}'))
