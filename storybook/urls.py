from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name="user")
router.register(r'signup', views.SignUpViewSet, base_name="signup")
router.register(r'userprofiles', views.UserProfileViewSet, base_name="profile")
router.register(r'families', views.FamilyViewSet, base_name="family")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^api/authenticate/$', views.AuthView.as_view(), name='authenticate'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]