from bloging.models import Post,Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=['author','title','text']

        widgets={
            'text':forms.Textarea(attrs={'class':'medium-editor-textarea editable postclass'}),
            'title':forms.Textarea(attrs={'class': 'title-class'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=['author','text']

        widgets={
            'text':forms.Textarea(attrs={'class':'medium-editor-textarea editable'}),
        }
