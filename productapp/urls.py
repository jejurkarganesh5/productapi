from rest_framework.routers import SimpleRouter
from .views import BrandOps,ProductOps
router = SimpleRouter()
router.register('brand', BrandOps)
router.register('product',ProductOps)
urlpatterns= router.urls
