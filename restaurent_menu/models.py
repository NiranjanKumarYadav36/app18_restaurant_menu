from django.db import models
# from django.contrib.auth.models import User
#
# # Create your models here.
#
MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)
#
#
# class Item(models.Model):
#     meal = models.CharField(max_length=1000, unique=True)
#     description = models.CharField(max_length=1000)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     meal_type = models.CharField(choices=MEAL_TYPE, max_length=100)
#     author = models.ForeignKey(User, on_delete=models.PROTECT) # CSCADE will delete all meals, SET_NULL, PROTECT
#     status = models.IntegerField(choices=STATUS, default=1)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.meal} - {self.price}"
#
#


class Item(models.Model):
    meal = models.CharField(primary_key=True, max_length=45, choices=MEAL_TYPE)
    description = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    meal_type = models.CharField(max_length=45, blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True, choices=STATUS, default=1)
    date_created = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return f"{self.meal} - {self.price}"

