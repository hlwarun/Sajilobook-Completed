from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from user.models import Profile

#This will create a profile everytime user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#This will save the profile everytime it is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
