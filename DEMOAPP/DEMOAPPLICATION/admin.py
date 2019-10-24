from django.contrib import admin
from .models import Officer
from .models import Guest
# Register your models here.


class OfficerAdmin(admin.ModelAdmin):
    fieldsets = [("Officer", {"fields": ["officer_fname", "officer_lname"]}),
                 ("Content", {"fields": ["officer_email", "officer_phone"]})
                 ]


admin.site.register(Officer, OfficerAdmin)


class GuestAdmin(admin.ModelAdmin):
    fields = ["guest_fname",
              "guest_lname",
              "guest_nickname",
              "guest_phonenumber",
              "guest_officer",
              "guest_email",
              "guest_date"]


admin.site.register(Guest)