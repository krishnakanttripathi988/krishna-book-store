from rest_framework import routers
from inventory.api import BooksViewSet

router = routers.DefaultRouter()
router.register('inventory', BooksViewSet, 'inventory')
