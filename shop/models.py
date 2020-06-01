from django.db import models

# Create your models here.

CATEGORY_CHOICES = (('Academic', 'Academic'), ('Non-Academic', 'Non-Academic'),)

ACADEMIC_CHOICES = (("School Books", "School Books"), ("High School Books", "High School Books"), ("A Level Books", "A Level Books"),
                     ("Bachelor's Books", "Bachelor's Books"), ("Master's Books", "Master's Books"),)

NONACADEMIC_CHOICES = (("Novel", "Novel"), ("Stories", "Stories"), ("Poetry", "Poetry"), ("Novel", "Novel"), ("Essay", "Essay"),
                        ("Biography", "Biography"), ("Auto Biography", "Auto Biography"), ("Article", "Article"), ("Travelouge", "Travelouge"),)

class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    academic_sub_category = models.CharField(max_length=50, choices=ACADEMIC_CHOICES, null=True, blank=True)
    nonacademic_sub_category = models.CharField(max_length=50, choices=NONACADEMIC_CHOICES, null=True, blank=True)
    original_price = models.DecimalField(max_digits=7, decimal_places=2 ,default=0.00)
    new_price = models.DecimalField(max_digits=7, decimal_places=2 ,default=0.00)
    discount_percent = models.DecimalField(max_digits=4, decimal_places=2 ,default=0.00)
    product_code = models.SlugField(unique=True)
    description = models.TextField(max_length=500)
    vendor = models.CharField(max_length=50, default='Sajilobook')
    contact = models.CharField(max_length=15, default='123456789')
    location = models.CharField(max_length=100, default='Nepal')
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to='products', default="")
    available_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['title', 'product_code']

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

class Sell(models.Model):
    name = models.CharField(max_length=50)
    book = models.CharField(max_length=100)
    category  = models.CharField(max_length=50)
    academic_subcategory = models.CharField(max_length=50, null=True, blank=True)
    non_academic_subcategory = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    district = models.CharField(max_length=50)
    institute = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=False, blank=False)

    def __str__(self):
        return self.book
