
from django.shortcuts import render
from .models import Generateorder
from django.shortcuts import redirect, render
from .forms import GenerateorderRegistrationForms

def register_order(request):
    if request.method=="POST":
      form=GenerateorderRegistrationForms(request.POST,request.FILES)
      if form.is_valid():
            form.save()
      else:
            print(form.errors)
    else:
        form=GenerateorderRegistrationForms()
    return render(request,"register_order.html",{"form":form})
def order_list(request):
    generateorders=Generateorder.objects.all()
    return render(request,"order_list.html",{"generateorders":generateorders})
def edit_order(request,id):
    generateorders=Generateorder.objects.get(id=id)
    if request.method=="POST":
        form=GenerateorderRegistrationForms(request.POST,instance=generateorders)
        if form.is_valid():
            form.save()
    else:
        form=GenerateorderRegistrationForms(instance=generateorders)
    return render(request,"edit_order.html",{"form":form})

def delete_order(request,id):
    generateorder=Generateorder.objects.get(id=id)
    generateorder.delete()
    return  render ('order_list')


# def delete_order(request,id):
#     generateorder=Generateorder.objects.get(id=id)
#     if request.method == 'POST':
#         generateorder.delete()
#         return redirect(order_list)
#     return render (request,'delete_order.html')
