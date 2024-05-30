from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    # if we have metaclass - abstract as true, then only dairyProduct have all attributes of Product table
    # class Meta:     # If we comment this we have 2 table - Product table and DairyProduct table
    #     abstract = True


class DiaryProduct(Product):

    expiry_date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'diaryproduct'

