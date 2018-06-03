from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
def upload_location(profile, filename):
	return "%s/%s" % (profile.user.username, filename)

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	website = models.URLField(default='', blank=True)
	bio = models.TextField(default='', blank=True)
	#miniBio = models.TextField(default='', blank=True)
	github = models.URLField(default='', blank=True)
	linkedin = models.URLField(default='', blank=True)
	medium = models.URLField(default='', blank=True)
	profilePicture = models.ImageField(upload_to=upload_location, blank=True, null = True)

	def __str__(self):
		return self.user.username

	def get_name(self):
		return self.user.first_name + " " + self.user.last_name