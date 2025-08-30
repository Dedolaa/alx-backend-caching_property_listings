from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

# Cache for 15 minutes
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values(
        "id", "title", "description", "price", "location", "created_at"
    )
    return JsonResponse({
        "data": list(properties)
    })
