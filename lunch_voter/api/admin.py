from django.contrib import admin
from .models import Employee, Restaurant, Menu, Vote

admin.site.register(Employee)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Vote)
