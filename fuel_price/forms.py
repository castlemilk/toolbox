from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText, FormActions
import re
pattern = re.compile(r'^[0-9]{1,15}$')
class PostalCodeForm(forms.Form):
    area_code = forms.IntegerField(max_value=9999)



    def __init__(self, *args, **kwargs):
        super(PostalCodeForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
