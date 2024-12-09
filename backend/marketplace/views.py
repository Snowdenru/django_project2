from marketplace.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from marketplace.forms import ProductForm
from django.http import Http404

def product_list(request):
    """
    Представления для товаров
    """

    products = Product.objects.all()
    return render(request, "marketplace/product_list.html", 
                  {"products": products})




def product_edit(request, pk):
    """Обновление карточки товара"""
    try:
        old_data = get_object_or_404(Product, pk=pk)
    except Exception:
        raise Http404('Такого товара не существует')
    
    # Если метод POST, то это обновленные данные студента
    # Остальные методы - возврат данных для изменения
    if request.method =='POST':
        form = ProductForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect('marketplace:product_list')
    else:
        form = ProductForm(instance = old_data)
        context = {
            'form': form
        }
        return render(request, 'marketplace/product_edit.html', context)