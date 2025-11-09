from django import forms
from home.models import Todo


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm): # forms for models
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created') # if you want all fields -> __all__  