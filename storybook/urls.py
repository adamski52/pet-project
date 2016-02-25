from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.authentication.views import LoginViewSet, LogoutViewSet
from api.user.views import UserViewSet
from api.dog.views import DogViewSet
from api.breed.views import BreedViewSet
from api.invite.views import InviteViewSet
from api.generic.views import FormatViewSet, PropertyViewSet
from api.room.views import RoomViewSet
from api.appointment.views import AppointmentViewSet
from api.schedule.views import ScheduleViewSet

router = DefaultRouter()
router.register(r"login", LoginViewSet, "login")
router.register(r"logout", LogoutViewSet, "logout")
router.register(r"users", UserViewSet, "users")
router.register(r"dogs", DogViewSet, "dogs")
router.register(r"breeds", BreedViewSet, "breeds")
router.register(r"invites", InviteViewSet, "invites")
router.register(r"formats", FormatViewSet, "formats")
router.register(r"properties", PropertyViewSet, "properties")
router.register(r"rooms", RoomViewSet, "rooms")
router.register(r"appointments", AppointmentViewSet, "appointments")
router.register(r"schedule", ScheduleViewSet, "schedule")
router.register(r"schedule/(?P<start>[0-9]{4}-[0-9]{2}-[0-9]{2})/(?P<end>[0-9]{4}-[0-9]{2}-[0-9]{2})", ScheduleViewSet, "appointments")


urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
