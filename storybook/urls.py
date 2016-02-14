from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r"login", views.LoginViewSet, "Login")
router.register(r"logout", views.LogoutViewSet, "Logout")
router.register(r"user", views.UserViewSet, "User")
router.register(r"family", views.FamilyViewSet, "Family")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]