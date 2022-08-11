from django.contrib import admin

from finance.models import Income, Budget, Expense

admin.site.register(Income)
admin.site.register(Budget)
admin.site.register(Expense)
