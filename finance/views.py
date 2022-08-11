from rest_framework import viewsets, permissions

from finance.models import Income, Budget
from finance.serializers import IncomeSerializer, BudgetSerializer


def filter_query(query, params):
    print(query)
    print(params.get("month"))
    month = params.get("month", None)
    if month:
        query.filter(date__month=month)
        print(query)
    return query


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id", None)
        month = self.request.query_params.get("month", None)
        if user_id is None:
            queryset = Income.objects.none()
        else:
            queryset = Income.objects.filter(user=user_id, date__month=month)
            print(queryset)
            # queryset = filter_query(queryset, self.request.query_params)
        return queryset


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id", None)
        month = self.request.query_params.get("month", None)
        if user_id is None:
            queryset = Budget.objects.none()
        else:
            queryset = Budget.objects.filter(user=user_id)
            if month:
                queryset.filter(date__month=month)
        return queryset


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id", None)
        month = self.request.query_params.get("month", None)
        if user_id is None:
            queryset = Budget.objects.none()
        else:
            queryset = Budget.objects.filter(user=user_id)
            if month:
                queryset.filter(date__month=month)
        return queryset
