from django.db import models


class Item(models.Model):
    item_name=models.CharField(max_length=100)
    item_variety=models.IntegerField(default=1)

    def __str__(self):
        return self.item_name



class Item_list(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=300)
    qty=models.IntegerField(default=0)
    price=models.FloatField(default=100.00)

    def __str__(self):
        return self.choice_text
