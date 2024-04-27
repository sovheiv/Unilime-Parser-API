from django.core.management.base import BaseCommand
import csv
from api.models import Product


class Command(BaseCommand):
    help = "Imports from CSV"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="CSV file path")

    def handle(self, *args, **options):
        file_path = options["csv_file"]
        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product, created = Product.objects.update_or_create(
                        asin=row["Asin"],
                        defaults={"title": row["Title"]},
                    )
                    if created:
                        print(f"Added :{product.title}")
                    else:
                        print(f"Updated existing :{product.title}")

        except FileNotFoundError:
            print(f"File does not exist: {file_path}")
