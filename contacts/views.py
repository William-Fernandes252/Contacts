from django.shortcuts import render, get_object_or_404
from .models import Contact


def index(request):
    context = {}
    context['contacts'] = Contact.objects.all()
    return render(request, 'contacts/index.html', context)


def contact(request, contact_id):
    context = {'contact': get_object_or_404(Contact, id=contact_id)}
    return render(request, 'contacts/contact.html', context)