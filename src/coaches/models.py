from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.conf import settings
from django.dispatch import receiver
# from location_field.models.plain import PlainLocationField
import random

def upload_location(instance, filename, **kwargs):
    file_path = 'coaches/{coach_id}/{filename}'.format(
        coach_id=str(instance.coach.id), filename=filename
    )
    return file_path

# Create your models here.
class Coach(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    gender = models.CharField(max_length=1)
    focus_health = models.BooleanField(default=False)
    focus_wellness = models.BooleanField(default=False)
    focus_health_wellness = models.BooleanField(default=False)
    focus_holistic = models.BooleanField(default=False)
    focus_life = models.BooleanField(default=False)
    focus_behavioral = models.BooleanField(default=False)
    travel = models.BooleanField()
    description = models.TextField()
    # city = models.CharField(max_length=255)
    # location = PlainLocationField(based_fields=['city'], zoom=7)
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

# @receiver(pre_save, sender=Coach)
def pre_save_coach_receiver(sender, instance, *args, **kwargs):
    # TODO: RANDOM.RANDINT IS A PLACEHOLDER, REPLACE WITH COACH'S ID VALUE LATER
    instance.slug = slugify(instance.first_name + '-' + instance.last_name + '-' + str(random.randint(0, 100000000)))

pre_save.connect(pre_save_coach_receiver, sender=Coach)