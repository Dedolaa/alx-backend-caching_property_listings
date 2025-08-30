from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to fetch from cache
    properties = cache.get("all_properties")

    if properties is None:
        # Not in cache → fetch from DB
        properties = list(
            Property.objects.all().values(
                "id", "title", "description", "price", "location", "created_at"
            )
        )
        # Store in cache for 1 hour (3600 seconds)
        cache.set("all_properties", properties, timeout=3600)

    return properties
