from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
def upload_location(proj, filename):
	return "%s/%s" % (prok.title, filename)

class Proj(models.Model):
	projectPicture = models.ImageField(upload_to=upload_location, blank=True, null = True)
	title = models.CharField(max_length = 120)
	slug = models.SlugField(('slug'), max_length=60, blank=True, unique=True)
	description = models.TextField()
	github = models.URLField(default='', blank=True)
	members = models.URLField(default='', blank=True)
	category = models.CharField(max_length = 120)
	date = models.DateTimeField(auto_now = False, auto_now_add = False)

	def __str__(self):
		return self.title