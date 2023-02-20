from main.views import StudentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', StudentView, basename='student')
# router.register(r'', StudentView, basename='student')
urlpatterns = router.urls