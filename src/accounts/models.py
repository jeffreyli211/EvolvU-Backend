from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    # If user's account is removed/delete, delete the corresponding email as well.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    location = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    profile_pic = models.ImageField(blank=True, null=True)

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.created(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''