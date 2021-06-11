from django.db import models

# Create your models here.
class Item(models.Model):
    item_no = models.CharField(max_length=100, primary_key=True, verbose_name='제품번호')
    item_name = models.CharField(max_length=100, verbose_name='제품명')
    item_price = models.PositiveIntegerField(verbose_name='제품가격')

    def __str__(self):
        return f"{self.item_no}. {self.item_name}"

#from .models import Item
#import random
#
#for i in range(20):
#    item = Item(item_no=f'id-{i}', item_name=f'제품-{i}', item_price=random.randrange(100,1000)*1000)
#    item.save()        