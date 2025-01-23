from django.core.management.base import BaseCommand
from core.models import Accessory, Bar, RedeauAccessory

class Command(BaseCommand):
    help = 'Verifies database data integrity'

    def handle(self, *args, **options):
        try:
            # Get counts
            bar_count = Bar.objects.count()
            accessory_count = Accessory.objects.count()
            redeau_count = RedeauAccessory.objects.count()

            # Get sample data
            bars = Bar.objects.all()[:5]
            accessories = Accessory.objects.all()[:5]
            redeau_accessories = RedeauAccessory.objects.all()[:5]

            self.stdout.write(self.style.SUCCESS('\nDatabase Verification Report'))
            self.stdout.write('=' * 40)
            
            # Display counts
            self.stdout.write(f'\nBar count: {bar_count}')
            self.stdout.write(f'Accessory count: {accessory_count}')
            self.stdout.write(f'Redeau Accessory count: {redeau_count}')

            # Display sample data
            self.stdout.write('\nSample Bars:')
            for bar in bars:
                self.stdout.write(f'- {bar.name}: {bar.price}')

            self.stdout.write('\nSample Accessories:')
            for accessory in accessories:
                self.stdout.write(f'- {accessory.name}: {accessory.price}')

            self.stdout.write('\nSample Redeau Accessories:')
            for redeau in redeau_accessories:
                self.stdout.write(f'- {redeau.name}: {redeau.price}')

            self.stdout.write('\n' + '=' * 40)
            self.stdout.write(self.style.SUCCESS('Verification complete'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error verifying data: {str(e)}'))
