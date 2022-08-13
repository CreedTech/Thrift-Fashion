from .models import *
from django.db.models import Q
import django_filters


def product_renderer(request):
    name = request.user
    category = Category.objects.all()
    hot_product1 = Item.objects.all().order_by('?')[0] if Item.objects.all().count() > 0 else Item.objects.all()
    hot_product2 = Item.objects.all().order_by('?')[1] if Item.objects.all().count() > 0 else Item.objects.all()
    recent_product = Item.objects.all().order_by('-launch_date')[0:2] if Item.objects.all().count() > 0 else Item.objects.all()
    counts = []
    for c in category:
        category_count = Item.objects.filter(category=c).count()
        counts.append(category_count)

    category_count = zip(category, counts)

    return {
        'category': category,
        'cat_count': category_count,
        'counts': counts,
        'name': name,
        'hot_product1': hot_product1,
        'hot_product2': hot_product2,
        'recent_product': recent_product,
    }


class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    launch_year = django_filters.NumberFilter(field_name='launch_date', lookup_expr='year')
    launch_year__gt = django_filters.NumberFilter(field_name='launch_date', lookup_expr='year__gt')
    launch_year__lt = django_filters.NumberFilter(field_name='launch_date', lookup_expr='year__lt')

    # category__name = django_filters.CharFilter(lookup_expr='icontains')

    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Item
        fields = ['price', 'launch_date']
