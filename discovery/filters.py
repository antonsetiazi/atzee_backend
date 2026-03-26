# discovery/filters.py

def apply_common_filters(queryset, params):
    search = params.get("search")
    category = params.getlist("category")
    location = params.getlist("location")
    min_price = params.get("min_price")
    max_price = params.get("max_price")

    if search:
        queryset = queryset.filter(name__icontains=search)

    if category:
        queryset = queryset.filter(category__in=category)

    if location:
        queryset = queryset.filter(location__in=location)

    if min_price:
        queryset = queryset.filter(price__gte=min_price)

    if max_price:
        queryset = queryset.filter(price__lte=max_price)

    return queryset