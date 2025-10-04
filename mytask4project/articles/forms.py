from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Article Title'}),
    )
    content = forms.CharField(
        label='Content',
        widget = forms.Textarea(attrs={'placeholder': 'Article Content'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if not title and not content:
            raise forms.ValidationError("Title and Content can't be both empty")
        return cleaned_data

