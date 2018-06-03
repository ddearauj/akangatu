from django import forms
from .models import Proj
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProjForm(forms.ModelForm):
	publish = forms.DateField(widget=forms.SelectDateWidget)
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Proj
		fields = [
			"title",
			"projectPicture",
			"description",
			"github",
			"members",
			"category",
			"date",
		]