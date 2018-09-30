from django.conf.urls import url
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('staff/register', views.StaffProfileViewSet)
router.register('admin/bus/register', views.AdminBusProfileViewSet)
router.register('admin/register', views.AdminProfileViewSet)
router.register('customer/register', views.CustomerProfileViewSet)
router.register('login', views.LoginViewSet, base_name= 'login') #because it is not a modelviewset
router.register('feedback',views.FeedbackViewSet)
router.register('bus', views.BusinessViewSet)
router.register('analyzecomplain', views.AnalyzeComplainViewSet, base_name='analyzecomplain') #because it is not a modelviewset
# router.register('bus/feedback',)
router.register('complain', views.ComplainViewSet)


urlpatterns=[
    url(r'', include(router.urls))
]
