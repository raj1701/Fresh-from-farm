from django.shortcuts import render
from item_display.models import Item,Item_list

def index(request):
    category_list=Item.objects.order_by('item_name')[:5]
    grocery_list=Item_list.objects.order_by('choice_text')
    context={'categories':category_list , 'groceries':grocery_list}
    return render(request,'item_display/display.html', context)


def display(request,id):
    category_list=Item.objects.get(pk=id)
    grocery_list=Item_list.objects.filter(item_id=id)
    context={'categories':category_list , 'groceries':grocery_list}
    return render(request,'item_display/item_display.html',context)