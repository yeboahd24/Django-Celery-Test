from django.shortcuts import render,reverse
from .forms import NewsLetterForm
from django.http import HttpResponse
from .tasks import send_message
from django.views.generic.edit import FormView


# Create your views here.
class NewsletterView(FormView):
    template_name = 'newsletter/newsletter.html'
    form_class = NewsLetterForm
    success_url = '/'
    success_message = 'Thank you for subscribing to our newsletter'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_message.delay(email, subject, message)
        return HttpResponse('Thank you for subscribing to our newsletter')