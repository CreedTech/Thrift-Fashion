from .models import *
from django.db.models import Q


def product_renderer(request):
    category = Category.objects.all()
    counts = []
    for c in category:
        category_count = Item.objects.filter(category=c).count()
        counts.append(category_count)

    category_count = zip(category, counts)

    return {
        'category': category,
        'cat_count': category_count,
        'counts': counts,
    }
