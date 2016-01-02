from django.shortcuts import render
from forms import MortgageCalculatorForm
from django import forms
import re
# Create your views here.
def list_tools(request):
    context = {}

    return render(request, 'finance_tools_list.html', context)


def mortgage_calculator(request):
    form = MortgageCalculatorForm(request.POST or None)
    pattern = re.compile(r'^[0-9]{1,15}$')

    context ={
                "form":form,
    }
    print form.is_valid()
    if form.is_valid():

        cleaned_loan_value = form.cleaned_data['loan_value'].replace(',','')
        valid_loan_value = re.search(pattern, cleaned_loan_value)
        if valid_loan_value:
            form.cleaned_data['loan_value'] = cleaned_loan_value
        else:
            raise forms.ValidationError("Must contain numbers between 0-9")
        context = {
                    "form": form,
                    "generate_report": True,
                    }


    return render(request, 'finance_mortgage_calculator.html', context)
