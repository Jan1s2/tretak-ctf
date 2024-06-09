from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button
from django import forms
from .models import Writeup

class WriteupForm(forms.ModelForm):
    class Meta:
        model = Writeup
        fields = "__all__"
