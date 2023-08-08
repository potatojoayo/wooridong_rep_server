from django.contrib import admin

from .models import BillMessage, UserVerificationMessage, RepVerificationMessage, AnnouncementMessage, InterimSettlementMessage


@admin.register(BillMessage)
class BillMessage(admin.ModelAdmin):
    pass

@admin.register(UserVerificationMessage)
class UserVerificationMessageAdmin(admin.ModelAdmin):
    pass

@admin.register(RepVerificationMessage)
class RepVerificationMessageAdmin(admin.ModelAdmin):
    pass

@admin.register(AnnouncementMessage)
class AnnouncementMessageAdmin(admin.ModelAdmin):
    pass

@admin.register(InterimSettlementMessage)
class InterimSettlementMessageAdmin(admin.ModelAdmin):
    pass
