from django import forms
from .models import Developer, Project, Skill

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name','last_name','email','age']

class ProjectForm(forms.ModelForm):
    developers = forms.ModelMultipleChoiceField(
        queryset=Developer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Project
        fields = ['title','description','developers']
