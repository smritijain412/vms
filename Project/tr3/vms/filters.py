import django_filters
from .models import Visit, Employee, Visitor


class VisitFilter(django_filters.FilterSet):
    class Meta:
        model = Visit
        fields = '__all__'
        exclude = ['employee', 'date_visited']
