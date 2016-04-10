from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.authentication.views import LoginViewSet, LogoutViewSet
from api.user.views import UserViewSet, UserAttachmentViewSet
from api.dog.views import DogViewSet, DogAttachmentViewSet
from api.breed.views import BreedViewSet
from api.invite.views import InviteViewSet
from api.generic.views import FormatViewSet, PropertyViewSet
from api.room.views import RoomViewSet
from api.appointment.views import AppointmentViewSet
from api.schedule.views import ScheduleViewSet
from api.camera.views import CameraViewSet
from api.csrftoken.views import TokenViewSet
from api.collage.views import CollageViewSet


router = DefaultRouter()
#router.register(r"token", TokenViewSet, "token")
router.register(r"login", LoginViewSet, "login")
router.register(r"logout", LogoutViewSet, "logout")
router.register(r"users", UserViewSet, "users")
router.register(r"users/(?P<user_id>[0-9]+)/attachments", UserAttachmentViewSet, "users-attachments")
router.register(r"dogs", DogViewSet, "dogs")
router.register(r"dogs/(?P<dog_id>[0-9]+)/attachments", DogAttachmentViewSet, "dogs-attachments")
router.register(r"breeds", BreedViewSet, "breeds")
router.register(r"invites", InviteViewSet, "invites")
router.register(r"formats", FormatViewSet, "formats")
router.register(r"properties", PropertyViewSet, "properties")
router.register(r"rooms", RoomViewSet, "rooms")
router.register(r"appointments", AppointmentViewSet, "appointments")
router.register(r"schedule", ScheduleViewSet, "schedule")
router.register(r"schedule/(?P<start>[0-9]{4}-[0-9]{2}-[0-9]{2})/(?P<end>[0-9]{4}-[0-9]{2}-[0-9]{2})", ScheduleViewSet, "appointments")
router.register(r"cameras", CameraViewSet, "cameras")
router.register(r"collages", CollageViewSet, "collages")

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
