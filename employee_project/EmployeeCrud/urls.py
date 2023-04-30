
from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import *
from .Crud.Employee_delete import *


# router = SimpleRouter()
# router.register("project",projectupdateview)

urlpatterns = [
    path('employeeRegistration',employeeRegistration.as_view()),
    path('get',Employee_get.as_view(), name='get'),
    path('project/',projectmodel_view().as_view(), name='post'),
    path('work/',workingview().as_view(), name='post'),
    path('qualification/',qualificationview().as_view(), name='post'),
    path('employeeUpdate/<str:regId>',Updateview().as_view(), name='put'),
    path('workUpdate/',WorkUpdate().as_view(), name='put'),
    path('qualificationUpdate/',qualificationupdateview().as_view(), name='put'),
    path('projectUpdate/',ProjectUpdate().as_view(), name='put'),
    path('delete/<str:regId>',Employee_delete().as_view(), name='put'),
    # path('project',include(router.urls))
]