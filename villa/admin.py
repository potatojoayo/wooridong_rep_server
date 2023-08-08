from django.contrib import admin
from .models import *
from .models.rep_take_over import RepTakeOver


class VillaAdmin(admin.ModelAdmin):
    pass


class BuildingAdmin(admin.ModelAdmin):
    pass


class UnitAdmin(admin.ModelAdmin):
    pass



class AddressAdmin(admin.ModelAdmin):
    pass

class RepTakeOverAdmin(admin.ModelAdmin):
    pass

admin.site.register(Villa, VillaAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(RepTakeOver, RepTakeOverAdmin)
