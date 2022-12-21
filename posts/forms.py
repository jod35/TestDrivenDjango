from django import forms
from .models import Post

class PostCreationForm(forms.ModelForm):
    title = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    body = forms.CharField(max_length=50,widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Post
        fields =['title','body']