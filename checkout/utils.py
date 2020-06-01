import random
import string
from checkout.models import Checkout

def id_generator(size=10, chars=string.ascii_uppercase+string.digits):
    new_id = "".join(random.choice(chars) for i in range(size))
    try:
        checkout = Checkout.objects.get(checkout_id=new_id)
        id_generator()
    except Checkout.DoesNotExist:
        return new_id
