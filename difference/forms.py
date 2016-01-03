from django import forms
from .models import TextDifferenceModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from crispy_forms.bootstrap import AppendedText, FormActions
class TextDifferenceForm(forms.ModelForm):
    class Meta:
        model = TextDifferenceModel
        fields = ['original','changed']


    def __init__(self, *args, **kwargs):
        super(TextDifferenceForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div('original', css_class='col-sm-6',),
                Div('changed', css_class='col-sm-6',),
                css_class='row',
                ),
            FormActions(),
                                    )
        # self.fields['original'].widget.attrs['style'] = 'width:500px; height:400px; resize: none;'
        # self.fields['changed'].widget.attrs['style'] = 'width:540px; height:400px; resize: none;'
