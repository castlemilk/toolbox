from django.shortcuts import render

# Create your views here.
from forms import TextDifferenceForm
def list_tools(request):
    context = {}

    return render(request, 'difference_tools_list.html', context)


def text_diff(request):
    form = TextDifferenceForm(request.POST or None)

    context = {
                "form": form,
                }
    print form.is_valid()
    if form.is_valid():
        print form.cleaned_data['original']
        print form.cleaned_data['changed']

        context = {
                    "form": form,
                    }

    return render(request, 'difference_text_diff.html', context)
