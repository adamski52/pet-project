from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.authentication.views import LoginViewSet, LogoutViewSet
from api.user.views import UserViewSet
from api.dog.views import DogViewSet
from api.breed.views import BreedViewSet
from api.invite.views import InviteViewSet
from api.room.views import RoomViewSet
from api.appointment.views import AppointmentViewSet

router = DefaultRouter()
router.register(r"login", LoginViewSet, "login")
router.register(r"logout", LogoutViewSet, "logout")
router.register(r"users", UserViewSet, "users")
router.register(r"dogs", DogViewSet, "dogs")
router.register(r"breeds", BreedViewSet, "breeds")
router.register(r"invites", InviteViewSet, "invites")
router.register(r"rooms", RoomViewSet, "rooms")
router.register(r"appointments", AppointmentViewSet, "appointments")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]