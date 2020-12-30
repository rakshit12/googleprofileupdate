from .models import Customer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Customer(user=user)
        profile.save()