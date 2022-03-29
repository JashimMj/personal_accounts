from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CompanyInformation)
admin.site.register(CashReceiveList)
admin.site.register(CashReceiveEntry)
admin.site.register(ExpenseList)
admin.site.register(ExpenseEntry)

