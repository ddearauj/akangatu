from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
	publish = forms.DateField(widget=forms.SelectDateWidget)
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Post
		fields = [
			"title",
			"lang",
			"category",
			"content",
			"leadImage",
			"draft",
			"publish",
		]