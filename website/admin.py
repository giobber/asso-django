from django.contrib import admin

import common.admin

from .models import Member, Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ["year", "card", "member"]
    list_filter = ["year", "card"]


class MembershipInline(admin.StackedInline):
    model = Membership
    extra = 0


class MemberAdmin(common.admin.EditInfoAdmin, common.admin.TrashBinAdmin):
    list_display = ["full_name", "id", "cf", "first_name", "last_name", "email"]
    list_filter = ["first_name", "last_name", "cf", "email"]

    inlines = [MembershipInline]


admin.site.register(Member, MemberAdmin)
admin.site.register(Membership, MembershipAdmin)
