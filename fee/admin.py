from django.contrib import admin
from .models import *
from .models import SentVillaFee, SentUnitFee, SentUnitBill
from .models.villa_fee import VillaFee


class FeeTypeAdmin(admin.ModelAdmin):
    pass


class ImposeFeeOnUnitAdmin(admin.ModelAdmin):
    pass


class UnitFeeAdmin(admin.ModelAdmin):
    pass


class VillaFeeAdmin(admin.ModelAdmin):
    pass


class ImposeTypeAdmin(admin.ModelAdmin):
    pass


class UniitBillAdmin(admin.ModelAdmin):
    pass


class InterimSettlementAdmin(admin.ModelAdmin):
    pass


class SentVillaFeeAdmin(admin.ModelAdmin):
    pass


class SentUnitFeeAdmin(admin.ModelAdmin):
    pass


class SentUnitBillAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeeType, FeeTypeAdmin)
admin.site.register(ImposeType, ImposeTypeAdmin)
admin.site.register(ImposeFeeOnUnit, ImposeFeeOnUnitAdmin)
admin.site.register(UnitFee, UnitFeeAdmin)
admin.site.register(VillaFee, VillaFeeAdmin)
admin.site.register(UnitBill, UniitBillAdmin)
admin.site.register(InterimSettlement, InterimSettlementAdmin)
admin.site.register(SentVillaFee, SentVillaFeeAdmin)
admin.site.register(SentUnitFee, SentUnitFeeAdmin)
admin.site.register(SentUnitBill, SentUnitBillAdmin)
