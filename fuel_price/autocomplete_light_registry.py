import autocomplete_light.shortcuts as al
from models import AAAData

# # This will generate a PersonAutocomplete class
# ----------------------- Working Autocomplete -------------------------------
al.register(AAAData,
            search_fields=['location'],
            name='AAADataAutocomplete',
            choices=AAAData.objects.all(),
            attrs={
                    'placeholder': 'Type to search location`',
                    'data-autocomplete-minimum-characters': 1,
                    }
            )
# ----------------------------------------------------------------------------


# ------------------------------------------------------
# al.register(AAAData,
#     # Just like in ModelAdmin.search_fields
#     search_fields=['location'],
#     attrs={
#         # This will set the input placeholder attribute:
#         # 'placeholder': 'Other model name ?',
#         # This will set the yourlabs.Autocomplete.minimumCharacters
#         # options, the naming conversion is handled by jQuery
#         'data-autocomplete-minimum-characters': 3,
#     },
#     # This will set the data-widget-maximum-values attribute on the
#     # widget container element, and will be set to
#     # yourlabs.Widget.maximumValues (jQuery handles the naming
#     # conversion).
#     widget_attrs={
#         'data-widget-maximum-values': 20,
#         # Enable modern-style widget !
#         'class': 'modern-style',
#     },
# )
# ------------------------------------------------------


# al.register(AAAData)
# ------------------------------------------------------
# class AAADataAutocomplete(al.AutocompleteModelBase):
#     choices = AAAData.objects.all()
#
#     def autocomplete_html(self):
#         html = super(AAADataAutocomplete, self).autocomplete_html()
#         q = self.request.REQUEST.get('q')
#         if q and not self.choices.filter(name=q).exists():
#             html += '<span data-value="create">Create "{}"</span>'.format(q)
#         return html
#
#     def post(self, request, *args, **kwargs):
#         return http.HttpResponse(
#             AAAData.objects.create(name=request.POST['location']).pk
#         )
# ------------------------------------------------------
