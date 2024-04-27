from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
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
                    try:
                        product = Product.objects.get(asin=row["Asin"])
                    except ObjectDoesNotExist:
                        print(f"Product not found: {row['Asin']}")
                        continue

                    review, created = product.reviews.update_or_create(
                        title=row["Title"],
                        product=product,
                        defaults={
                            "review": row["Review"],
                        },
                    )

                    if created:
                        print(f"Added: {review.title}")
                    else:
                        print(f"Updated existing: {review.title}")

        except FileNotFoundError:
            print(f"File does not exist: {file_path}")
