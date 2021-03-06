# Generated by Django 3.0.5 on 2020-05-26 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('bolean', models.BooleanField(default=True, verbose_name='This is a boolean field')),
                ('char', models.CharField(help_text='add help text', max_length=100, unique=True, verbose_name='new Name')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('email', models.EmailField(max_length=100)),
                ('file', models.FileField(blank=True, upload_to='uploads')),
                ('image', models.ImageField(blank=True, upload_to='uploads/image')),
                ('integer', models.IntegerField()),
                ('positive_int', models.PositiveIntegerField()),
                ('positive_smal_init', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField(blank=True)),
                ('text', models.TextField()),
                ('url', models.URLField(max_length=100)),
                ('uuid1', models.UUIDField(default=uuid.uuid4)),
                ('uuid2', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ceate', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('date_and_time', models.DateTimeField()),
                ('choice', models.CharField(choices=[('one', 'number one'), ('two', 'number two')], max_length=10)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('new_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
