from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def about(request):
    return render(request, 'site/about.html', {})


def home(request):
    return render(request, 'site/home.html', {})

def contact(request):
    form  = ContactForm(request.POST or None)
    title = "Contact"
    context = {
                "form": form,
                "title": title,
                }
    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value


        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')
        subject = "Site Contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, form_email]
        contact_message = "%s: %s via %s" % (form_full_name,
                                             form_message,
                                             form_email)
        send_mail(subject,
                   contact_message,
                   from_email,
                   to_email,
                   fail_silently = False)

        context = {
                    "title": "Thank You",
                    "sent": True,
                    }




    return render(request, 'site/contact.html', context)
