import itertools

from userProfile.models import UserProfile


from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.


class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False)


def upload_location(instance, filename):
	return "%s/%s" % (instance.slug, filename)
	
class Post(models.Model):
	user = models.ForeignKey(UserProfile)
	title = models.CharField(max_length = 120)
	leadImage = models.FileField(upload_to=upload_location, null = True, blank = True)
	content = models.TextField()
	slug = models.SlugField(('slug'), max_length=60, blank=True, unique=True)
	draft = models.BooleanField(default=False)
	timeStamp = models.DateTimeField(auto_now = False, auto_now_add = True)
	updatedTimeStamp = models.DateTimeField(auto_now = True, auto_now_add = False)
	publish = models.DateField(auto_now = False, auto_now_add = False)
	category = models.CharField(max_length = 120)
	lang = models.CharField(max_length = 120)
	tags = models.CharField(max_length = 200)

	def get_tag_list(self):
		return re.split(" ", self.tags)




	objects = PostManager()

	#Then override models save method:
	def save(self, *args, **kwargs):
		if not self.id:
			#Only set the slug when the object is created.
			self.slug = orig = slugify(self.title) #Or whatever you want the slug to use
			for x in itertools.count(1):
				if not Post.objects.filter(slug=self.slug).exists():
					break
				self.slug = '%s-%d' % (orig, x)
		super(Post, self).save(*args, **kwargs)


	def __str__(self):
		return self.title

	def get_abs_url(self):
		return reverse("blog:detail", kwargs={"slug" : self.slug})
		#return "/blog/%s/" % (self.slug)

	class Meta:
		ordering = ["-timeStamp", "-updatedTimeStamp"]