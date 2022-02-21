from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.core.paginator import Paginator
from django.http import Http404


def index(request):
    context = {}
    
    contacts = Contact.objects.filter(show = True).all()
    paginator = Paginator(contacts, 20)
    page_number = request.GET.get('page')
    context['contacts'] = paginator.get_page(page_number)
    
    return render(request, 'contacts/index.html', context)


def contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    if not contact.show:
        raise Http404
    
    context = {'contact': get_object_or_404(Contact, id=contact_id)}
    return render(request, 'contacts/contact.html', context)