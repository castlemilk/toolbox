from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText, FormActions, PrependedText
from models import AAAData
from autocomplete_light.widgets import ChoiceWidget
import autocomplete_light
import re
pattern = re.compile(r'^[0-9]{1,15}$')

 # ---------------------- working autocomplete ---------------------------------
# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = AAAData
#         fields = ['location']
#         choices = AAAData.objects.all()
#
#
#     location = forms.ModelChoiceField(
#         required=True,
#         queryset=AAAData.objects.all(),
#         widget=autocomplete_light.fields.ChoiceWidget('AAADataAutocomplete')
#           )
# ------------------------------------------------------------------------------
# ----------------------- working autocomplete --------------------------------
# class LocationForm(forms.Form):
    # location = forms.ModelChoiceField(
    #         required=True,
    #         queryset=AAAData.objects.all(),
    #         widget=autocomplete_light.fields.ChoiceWidget('AAADataAutocomplete')
    #           )
    #
    # def __init__(self, *args, **kwargs):
    #     super(LocationForm,self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     # self.helper.form_class = 'form-horizontal'
    #     # self.helper.label_class='col-sm-2'
    #     # self.helper.field_class= 'col-sm-8'
    #     self.helper.layout = Layout(
    #                 # PrependedText('location',
    #                 #   '<i class="fa fa-location-arrow"></i>',
    #                 #   css_class='input-small'),
    #                 PrependedText('location',
    #                   '$',
    #                   ),
    #                 # FormActions(
    #                 #     Submit('submit', 'get_xyz', css_class="btn-primary"),
    #                 #             )
    #                   )


# ------------------------------------------------------------------------------
# ----------------------- need to get charfield working? -----------------------
class LocationForm(forms.Form):
    location = forms.CharField(
        required=True,
        widget=autocomplete_light.fields.ChoiceWidget('AAADataAutocomplete')
          )


    def __init__(self, *args, **kwargs):
        super(LocationForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # Edit by bryan
        self.fields['location'].widget.attrs['style'] = 'width:200px; height:30px;'
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class='col-sm-2'
        # self.helper.field_class= 'col-sm-8'
        # self.helper.layout = Layout(
        #             # PrependedText('location',
        #             #   '<i class="fa fa-location-arrow"></i>',
        #             #   css_class='input-small'),
        #             PrependedText('location',
        #               '$',
        #               ),
                    # FormActions(
                    #     Submit('submit', 'get_xyz', css_class="btn-primary"),
                    #             )
                    #   )
