from django.contrib import admin
from .models import RationDistribution
from .models import Member


admin.site.register(RationDistribution)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_no', 'address', 'created_at')  # ✅ Added 'address'
    search_fields = ('name', 'email', 'mobile_no', 'address')  # ✅ Allow searching by 'address'
    list_filter = ('created_at',)  # Filter by creation date


