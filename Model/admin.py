from django.contrib import admin

from Model.models import Test,Contact,Tag
from Model.mutualfund import FundFinance,FundScale,FundConfig,FundNetData,BankGoldData
from Model.morningstar import MutualFundRating,MutualFundBuyInfo,MutualFundReturnInfo,MutualFundManagerInfo,MutualFundManagerDetail
from Model.fundselector import FundRecommend

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

class FundFinanceAdmin(admin.ModelAdmin):
    list_display = ('code','name','time') # list
class FundScaleAdmin(admin.ModelAdmin):
    list_display = ('code','name','time') # list
class FundConfigAdmin(admin.ModelAdmin):
        list_display = ('code','name','time') # list
class FundNetDataAdmin(admin.ModelAdmin):
    list_display = ('symbol','sname','nav_date','jjlx') # list
class BankGoldDataAdmin(admin.ModelAdmin):
    list_display = ('variety','midpri','todayopen','closeyes','time') # list
class MutualFundRatingAdmin(admin.ModelAdmin):
    list_display = ('code','name','fundType','StarRating3','StarRating5','SD3Year','DR3Year','SR3Year','ReturnYTD') # list
class MutualFundBuyInfoAdmin(admin.ModelAdmin):
    list_display = ('code','name','establishDate','applyState','returnState','frontCharge','backCharge','redeemFee','manageFee') # list
class MutualFundReturnInfoAdmin(admin.ModelAdmin):
    list_display = ('code','name','oneDayReturn','oneMonthReturn','sixMonthReturn','oneYearReturn','threeYearReturn','updateDate') # list
class MutualFundManagerInfoAdmin(admin.ModelAdmin):
    list_display = ('code','name','fundType','manager','totalStart','manageStart','manageAchive','manageAvgAchive','updateDate') # list
class MutualFundManagerDetailAdmin(admin.ModelAdmin):
    list_display = ('manager','code','name','manageStart','manageEnd','length','manageAchive','manageAvgAchive','updateDate') # list
class FundRecommendAdmin(admin.ModelAdmin):
    list_display = ('code','name','threeYearSharp','threeYearStandard','threeYearRisk','StarRating3','StarRating5','updateDate') # list

admin.site.register(FundFinance, FundFinanceAdmin)
admin.site.register(FundScale, FundScaleAdmin)
admin.site.register(FundConfig, FundConfigAdmin)
admin.site.register(FundNetData, FundNetDataAdmin)
admin.site.register(BankGoldData, BankGoldDataAdmin)
admin.site.register(MutualFundRating, MutualFundRatingAdmin)
admin.site.register(MutualFundBuyInfo, MutualFundBuyInfoAdmin)
admin.site.register(MutualFundReturnInfo, MutualFundReturnInfoAdmin)
admin.site.register(MutualFundManagerInfo, MutualFundManagerInfoAdmin)
admin.site.register(MutualFundManagerDetail, MutualFundManagerDetailAdmin)
admin.site.register(FundRecommend, FundRecommendAdmin)