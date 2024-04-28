from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=512)
    asin = models.TextField(unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "products"


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    title = models.CharField(max_length=255)
    review = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "reviews"
