from django.db import models
import uuid
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User

my_choices = (
    ('one', 'number one'),
    ('two', 'number two')
)


class TestModel(models.Model):
    # when we set verbose name it will work like a label in frontend you can see the description that i give it here ("this is a boolean field")
    #  otherwise if i don't set so you see ("bolean")
    bolean = models.BooleanField(
        default=True, verbose_name="This is a boolean field")
    # help text will appear underneath of the text box
    char = models.CharField(
        verbose_name="new Name", max_length=100, unique=True, help_text="add help text")
    date = models.DateField(default=timezone.now)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(max_length=100)
    file = models.FileField(upload_to="uploads", blank=True)
    image = models.ImageField(upload_to="uploads/image", blank=True)
    # integer = t supports values from -2147483648 to 2147483647 are safe in all databases supported by Django.
    integer = models.IntegerField()
    # positive init = It supports values from 0 to 2147483647 are safe in all databases supported by Django.
    positive_int = models.PositiveIntegerField()
    # small  =  is used to store integer values from -32768 to 32767 (2 Bytes). This field is useful for values not are not extremes.
    positive_smal_init = models.PositiveSmallIntegerField()
    slug = models.SlugField(blank=True)
    # for string above 255 chars
    text = models.TextField()
    url = models.URLField(max_length=100)
    # storing universaly unique identifier
    uuid1 = models.UUIDField(default=uuid.uuid4)
    # when we define the primary key here it will become the primary key to our model database
    # when we set ediatable = False ---> so it will become invisible and admin or the model usere won't see anymore
    uuid2 = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)
    ceate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    date_and_time = models.DateTimeField()
    choice = models.CharField(max_length=10, choices=my_choices)

    phone_number = PhoneNumberField()

    new_field = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text[:30])
        super(TestModel, self).save(*args, **kwargs)
