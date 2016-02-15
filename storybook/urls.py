from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views.login import *
from api.views.logout import *
from api.views.user import *
from api.views.dog import *
from api.views.breed import *

router = DefaultRouter()
router.register(r"login", LoginViewSet, "login")
router.register(r"logout", LogoutViewSet, "logout")
router.register(r"users", UserViewSet, "users")
router.register(r"dogs", DogViewSet, "dogs")
router.register(r"breeds", BreedViewSet, "breeds")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]