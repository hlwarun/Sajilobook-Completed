from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from checkout.models import Checkout, BillingDetail
from checkout.forms import BillingDetailForm
from checkout.utils import id_generator
from django.contrib import messages

# Create your views here.

@login_required
def checkout(request):
    try:
       new_id = request.session['cart_id']
       cart = Cart.objects.get(id=new_id)
    except:
        new_id = None
        return HttpResponseRedirect(reverse('cart'))

    try:
        new_checkout = Checkout.objects.get(cart=cart)
    except Checkout.DoesNotExist:
        new_checkout = Checkout(cart=cart, user=request.user, checkout_id=id_generator())
        new_checkout.save()
    except:
        return HttpResponseRedirect(reverse('cart'))

    if new_checkout.status == "Delivered" or  new_checkout.status == "Abandoned":
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart'))

    form = BillingDetailForm()
    if request.method == 'POST':
        form = BillingDetailForm(request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            messages.info(request, "Your order has been sent.")
            return HttpResponseRedirect(reverse('non_academic'))
            # BillingDetail.objects.create(**form.cleaned_data)
    context = {'form':form}
    return render(request, 'checkouts.html', context)
