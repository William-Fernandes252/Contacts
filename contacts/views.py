from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    context = {}
    
    contacts = Contact.objects.filter(show = True)
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

def search(request):
    context = {}
    
    fields = Concat('name', Value(' '), 'surname')
    context['search'] = request.GET.get('term')
    if context['search'] is None or not context['search']:
        raise Http404()
    
    contacts = Contact.objects.annotate(
        full_name = fields
    ).filter(
        Q(full_name__icontains = context['search']) | 
        Q(phone__icontains = context['search'])
    )
    
    paginator = Paginator(contacts, 20)
    page_number = request.GET.get('page')
    context['contacts'] = paginator.get_page(page_number)
    
    return render(request, 'contacts/search.html', context)