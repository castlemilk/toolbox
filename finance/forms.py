from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText, FormActions
import re
pattern = re.compile(r'^[0-9]{1,15}$')
class MortgageCalculatorForm(forms.Form):
    # loan_value = forms.FloatField(max_value=10000000000,min_value=1,required=True)
    # class Meta:
    # #     model = MortgageInputs
    #     fields = ['loan_value', 'interest_rate', 'loan_period']

    loan_value = forms.CharField(max_length=15,required=True)
    interest_rate = forms.FloatField(max_value=100, min_value=1, required=True)
    loan_period = forms.IntegerField(min_value=1, max_value=99, required= True)


    #
    # def clean_loan_value(self):
    #
    #     cleaned_loan_value = self.cleaned_data['loan_value'].replace(',','')
    #     valid_loan_value = re.search(pattern, cleaned_loan_value)
    #     if valid_loan_value:
    #         self.cleaned_data['loan_value'] = cleaned_loan_value
    #     else:
    #         raise forms.ValidationError("Must contain numbers between 0-9")
    #
    #     return cleaned_loan_value

    def __init__(self, *args, **kwargs):
        super(MortgageCalculatorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            # Fieldset(
            #         'loan_value',
            #         'interest_rate',
            #         'loan_period',
            #         ),
            AppendedText('loan_value', '$', active=True),
            AppendedText('interest_rate', '%', active=True),
            AppendedText('loan_period', 'years', active=True),
            FormActions(
                        Submit('submit', 'Calculate'),
                        ),
                                    )

    # interest_rate = forms.CharField(max_length=2, required=True)
    # loan_period = forms.CharField(max_length=2, required= True)

    # def clean_loan_value(self):
    #     loan_value = self.clean_data.get('loan_value')
    #     print loan_value
    # def clean_interest_rate(self):
    #     interest_rate = self.cleaned_data.get('interest_rate')
    #     print interest_rate
    #
    # def clean_loan_period(self):
    #     loan_period = self.cleaned_data.get('loan_period')
    #     print loan_period
# email = self.cleaned_data.get('email')
