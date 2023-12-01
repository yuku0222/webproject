

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='商品名')
    description = models.TextField(blank=True, null=True, verbose_name='説明')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='価格')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='商品画像')

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock', verbose_name='商品')
    quantity = models.PositiveIntegerField(default=0, verbose_name='数量')
    location = models.CharField(max_length=50, verbose_name='場所')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='最終更新日時')

    def __str__(self):
        return f"{self.product} - {self.quantity}個"
