from django import forms
from app.models import Post,Hostel,Problem

class HostelForm(forms.ModelForm):
    class Meta():
        model=Hostel
        fields=('hostel',)

class ProblemForm(forms.ModelForm):
    class Meta():
        model=Problem
        fields=('problem',)

class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('name','roll','phone','hall','issue','description','create_date',)
