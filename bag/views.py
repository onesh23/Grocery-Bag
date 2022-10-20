from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from bag.models import Item
from django.contrib import messages


# Create your views here.

@login_required
def index(request):
    date = request.GET.get('date')
    if date:
        items = Item.objects.filter(user=request.user,date=date).order_by('-id')
    else:
        items = Item.objects.filter(user=request.user).order_by('-id')
    context = {'items':items}
    return render(request,'index.html',context)


@login_required
def add_Item(request):
    print('aa')
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        date = request.POST.get('date')
        print(date,name)
        if name and quantity and status and date:
            new_Item = Item(name=name,quantity=quantity,status=status,date=date,user=request.user)
            new_Item.save()
            messages.success(request,'Items Added Successfully')
            return redirect('index')
        messages.error(request,'All fields Are Required')
        return redirect('add_item')
    return render(request,'add.html')

def update_Item(request,id):
    item = Item.objects.get(id=id)
    date = item.date.strftime("%d-%m-%y")
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.quantity = request.POST.get('quantity')
        item.status = request.POST.get('status')
        item.date = request.POST.get('date')

        item.save()
        messages.success(request,'Item Updated Successfully')
        return redirect('index')
    return render(request,'update_item.html',{'item':item,'date':date})


@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    messages.error(request, 'Item deleted successfully!')
    return redirect('index')