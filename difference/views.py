from django.shortcuts import render
from difflib.diff_match_patch import diff_match_patch

# Create your views here.
from forms import TextDifferenceForm
def list_tools(request):

    context = {}

    return render(request, 'difference_tools_list.html', context)


def text_diff_simple(request):
    form = TextDifferenceForm(request.POST or None)

    context = {
                "form": form,
                "result": None,
                }
    if form.is_valid():
        original = form.cleaned_data['original']
        changed = form.cleaned_data['changed']
        differ = diff_match_patch()
        difference = differ.diff_main(original, changed)
        context = {
                    "form": form,
                    "result": difference,
                    }

    return render(request, 'difference_text_diff_simple.html', context)


def text_diff_advanced(request):
    form = TextDifferenceForm(request.POST or None)

    context = {
                "form": form,
                "result": None,
                "advanced_search": True,
                }
    if form.is_valid():
        original = form.cleaned_data['original']
        changed = form.cleaned_data['changed']
        differ = diff_match_patch()
        difference = differ.diff_main(original, changed)
        print difference
        line_number_diff = differ.diff_cleaned(difference)
        if len(line_number_diff) > 1:
            context = {
                        "form": form,
                        "result": line_number_diff,
                        "advanced_search": True,
                        }
        else:
            context = {
                        "form": form,
                        "result": line_number_diff,
                        "advanced_search": False,
                        }


    return render(request, 'difference_text_diff_advanced.html', context)
