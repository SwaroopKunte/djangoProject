from rest_framework_mongoengine import routers
from crmsystem.views import EmployeesView

router = routers.DefaultRouter()
router.register(r'crmsystem', EmployeesView)

urlpatterns = []
urlpatterns += router.urls
