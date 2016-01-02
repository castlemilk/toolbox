from django import forms
from .models import TextDifferenceModel
class TextDifferenceForm(forms.ModelForm):
    class Meta:
        model = TextDifferenceModel
        fields = ['original','changed']


    def __init__(self, *args, **kwargs):
        super(TextDifferenceForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        # self.fields['original'].widget.attrs['cols'] = 40
        # self.fields['original'].widget.attrs['rows'] = 20
        # self.fields['changed'].widget.attrs['cols'] = 40
        # self.fields['changed'].widget.attrs['rows'] = 20
        self.fields['original'].widget.attrs['style'] = 'width:400px; height:300px;'
        self.fields['changed'].widget.attrs['style'] = 'width:400px; height:300px;'
