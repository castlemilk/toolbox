from django.shortcuts import render
from difflib.diff_match_patch import diff_match_patch

# Create your views here.
from forms import TextDifferenceForm
def list_tools(request):

    context = {}

    return render(request, 'difference_tools_list.html', context)


def text_diff(request):
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
        # result_output = []
        # for item in difference:
        #     result_output.append((item[0],item[1].replace('\r\n','</br>')))
        print difference
        # print result_output
        context = {
                    "form": form,
                    "result": difference,
                    }

    return render(request, 'difference_text_diff.html', context)
