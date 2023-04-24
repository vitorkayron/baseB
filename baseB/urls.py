from .views import ClienteViewSet
from rest_framework.routers import DefaultRouter

app_name = 'baseB'

router = DefaultRouter(trailing_slash=False)
router.register(f'baseB', ClienteViewSet)

urlpatterns = router.urls