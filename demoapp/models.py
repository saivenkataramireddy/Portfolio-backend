import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400)
    self_introduction = models.FileField(upload_to="uploads/", storage=RawMediaCloudinaryStorage(), blank=True, null=True)
    iam = models.CharField(max_length=500)
    resume = models.FileField(upload_to="uploads/", storage=RawMediaCloudinaryStorage(), blank=True, null=True)
    about_you = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.name

class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    technologies = models.CharField(max_length=500)
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    github_link = models.URLField(max_length=500, blank=True, null=True)
    live_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectMedia(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="media")
    image = models.ImageField(upload_to="project_gallery/", blank=True, null=True)

class Certifications(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Certifications"

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Journey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.title}"
