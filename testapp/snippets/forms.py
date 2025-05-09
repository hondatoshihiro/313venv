from django import forms

from snippets.models import Snippet

#実践Django Pythonによる本格Webアプリケーション開発 1.4.4
class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')