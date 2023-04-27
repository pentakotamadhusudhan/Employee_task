from django.urls import reverse_lazy,path,include
from .views import *
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register("Employee",popllview)


urlpatterns = [
    path("reg/",include(router.urls)),
   ]
