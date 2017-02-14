from django.contrib import admin

from Model.models import Test,Contact,Tag
from Model.mutualfund import FundFinance,FundScale,FundConfig

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    inlines = [TagInline]  # Inline
    search_fields = ('name',)

    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
admin.site.register([FundFinance, FundScale, FundConfig])
