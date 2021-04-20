from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(addBook)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["issue_date"]
    list_filter = ["studentname"] #add filters
    search_fields = ["studentname"]

admin.site.register(order,OrderAdmin)