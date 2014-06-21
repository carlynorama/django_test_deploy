from django.shortcuts import render
from lists.models import Item

def home_page(request):    
    if request.method == 'POST':
        new_item_text = request.POST['item_text']  #1
        Item.objects.create(text=new_item_text)  #2
    else:
        new_item_text = ''  #3

    return render(request, 'home.html', {
        'new_item_text': new_item_text,  #4
    })