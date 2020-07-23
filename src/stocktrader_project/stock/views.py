from django.shortcuts import render

from .forms import OrderForm


# Create your views here.
def order_create_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save

    context = {
        'form': form
    }
    return render(request, "stock/order_create.html", context)