from django.contrib import admin
from .models import Bank

# Register your models here.


class BankAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bank, BankAdmin)
