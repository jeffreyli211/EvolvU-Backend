# Generated by Django 3.1.7 on 2021-03-22 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=users.models.upload_location)),
                ('gender', models.CharField(max_length=1)),
                ('focus_health', models.BooleanField(default=False)),
                ('focus_wellness', models.BooleanField(default=False)),
                ('focus_health_wellness', models.BooleanField(default=False)),
                ('focus_holistic', models.BooleanField(default=False)),
                ('focus_life', models.BooleanField(default=False)),
                ('focus_behavioral', models.BooleanField(default=False)),
                ('focus_unsure', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]