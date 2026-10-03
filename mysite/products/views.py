from django.shortcuts import render

from products.forms import ProductForm
from django.http import HttpResponse

from products.models import Product


def create_product(request):
    if request.method == 'POST':
        form =ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('success')
    else:
        form=ProductForm()

    return render (request,'form.html',{'form':form})



def update_product(request,p_id):
    p= Product.objects.get(pk=p_id)
    if request.method == 'POST':
        form =ProductForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
        return HttpResponse('success')
    else:
        form=ProductForm(instance=p)
    return render (request,'form.html',{'form':form})

def delete_product(request,p_id):
    Product.objects.get(pk=p_id).delete()
    return render (request,'form.html')