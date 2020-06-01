from django.shortcuts import render, redirect, Http404
from shop.models import Product, Contact, Sell
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    product = Product.objects.all().order_by('-date_added')
    context = {'products':product}
    return render(request, 'index.html', context)

def search(request):
    try:
        q = request.GET.get('search')
    except:
        q = None
    if q:
        prd = Product.objects.all()
        product = prd.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(category__icontains=q) | Q(academic_sub_category__icontains=q) | Q(nonacademic_sub_category__icontains=q)).order_by('-date_added')
        context = {'q':q, 'productFilter':product}
    else:
        product = Product.objects.all().order_by('-date_added')
        context = {'productFilter':product}
    return render(request, 'search.html', context)

def academic(request):
    product = Product.objects.filter(category = "Academic").order_by('-date_added')
    paginator = Paginator(product, 9)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    context = {'products':product}
    return render(request, 'category-academic.html', context)

def non_academic(request):
    product = Product.objects.filter(category = "Non-Academic").order_by('-date_added')
    paginator = Paginator(product, 9)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    context = {'products':product}
    return render(request, 'category-non-academic.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, f"{name}, Your message has been sent.")
        return redirect('contact')

    else:
        return render(request, 'contact.html')

def sell(request):
    if request.method == 'POST':
        name = request.POST.get('user-name')
        book = request.POST.get('user-book')
        category = request.POST.get('user-bookcat')
        academic_subcategory = request.POST.get('user-academiccat')
        non_academic_subcategory = request.POST.get('user-nonacademiccat')
        price = request.POST.get('price')
        email = request.POST.get('user-email')
        mobile = request.POST.get('user-no')
        district = request.POST.get('user-district')
        institute = request.POST.get('user-college')
        image = request.FILES.get('book-image')
        sell = Sell(name=name, book=book, category=category, academic_subcategory=academic_subcategory, non_academic_subcategory=non_academic_subcategory,
                    price=price, email=email, mobile=mobile, district=district, institute=institute, image=image)
        sell.save()
        messages.info(request, "Your details have been submitted.")
        return redirect('sell')

    else:
        return render(request, 'sell.html')

def single(request, product_code):
    try:
        product = Product.objects.get(product_code=product_code)
        context = {'product':product}
        return render(request, 'single.html', context)
    except:
        raise Http404
