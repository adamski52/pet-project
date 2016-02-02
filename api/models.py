from django.db import models
import uuid

class Human(models.Model):
    humanUUID = models.UUIDField(
                    primary_key=True,
                    default=uuid.uuid4,
                    editable=False)
    familyUUID = models.ForeignKey("Family",
                    on_delete=models.DO_NOTHING,
                    null=True)
    dateCreated = models.DateTimeField(
                    auto_now_add=True)
    dateModified = models.DateTimeField(
                    auto_now=True,
                    null=True)
    dateDeleted = models.DateTimeField(
                    null=True)
    email = models.EmailField()
    firstName = models.CharField(
                    max_length=40)
    lastName = models.CharField(
                    max_length=40)
    address = models.CharField(
                    max_length=40)
    address2 = models.CharField(
                    max_length=40,
                    null=True)
    city = models.CharField(
                    max_length=40)
    state = models.CharField(
                    max_length=2)
    zipCode = models.CharField(
                    max_length=10)
    homePhone = models.CharField(
                    max_length=10,
                    null=True)
    cellPhone = models.CharField(
                    max_length=10,
                    null=True)
    gender = models.CharField(
                    max_length=1)
    deleted = models.BooleanField(
                    default=False)

    def __str__(self):
        return self.lastName + ", " + self.firstName


class Family(models.Model):
    familyUUID = models.UUIDField(
                    primary_key=True,
                    default=uuid.uuid4,
                    editable=False)
    dateCreated = models.DateTimeField(
                    auto_now_add=True)
    dateModified = models.DateTimeField(
                    auto_now=True,
                    null=True)
    dateDeleted = models.DateTimeField(
                    null=True)
    name = models.CharField(
                    max_length=40)

    def __str__(self):
        return self.name


