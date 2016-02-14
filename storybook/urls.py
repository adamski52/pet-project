from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r"login", views.LoginViewSet, "login")
router.register(r"logout", views.LogoutViewSet, "logout")
router.register(r"user", views.UserViewSet, "user")
router.register(r"dog", views.DogViewSet, "dog")
router.register(r"breed", views.BreedViewSet, "breed")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]