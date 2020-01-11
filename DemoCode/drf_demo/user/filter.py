import django_filters
from user.models import User


class UserFilter(django_filters.FilterSet):

    # name_mh = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    # sort = django_filters.OrderingFilter(fields=('age',))
    # age_gt = django_filters.NumberFilter(field_name='age', lookup_expr='gt')
    # age_lt = django_filters.NumberFilter(field_name='age', lookup_expr='lt')
    class Meta:
        model = User
        # fields = ["name", "age"]
        fields = {
            "name": ['exact','icontains'],
            "age": ['exact','gte','lte'],
        }

