from django.urls import path, include
from rest_framework import routers

from finance.views import IncomeViewSet, BudgetViewSet, ExpenseViewSet

router = routers.DefaultRouter()
router.register(r'incomes', IncomeViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
