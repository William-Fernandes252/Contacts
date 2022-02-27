from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contact, Category
from .forms import ContactForm


def index(request):
    context = {}
    
    contacts = Contact.objects.filter(show = True)
        
    paginator = Paginator(contacts, 20)
    page_number = request.GET.get('page')
    context['contacts'] = paginator.get_page(page_number)
    context['categories'] = [category['name'] for category in Category.objects.values('name')]
    
    context['contact_form'] = ContactForm()
    
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
    context['categories'] = Category.objects.all()
    
    return render(request, 'contacts/search.html', context)


def add(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "New Contact has been added!")
    else:
        messages.error(request, "Invalid contact.")
    return HttpResponseRedirect(reverse('index'))


def delete(request):
    ids = request.POST.get('contacts')
    if ids:
        Contact.objects.filter(pk__in = ids).delete()
        messages.success(request, "Contacts deleted.")  
    return HttpResponseRedirect(reverse('index'))


def filter(request, category):
    context = {}
    
    contacts = Contact.objects.filter(show = True, category__name = category)
        
    paginator = Paginator(contacts, 20)
    page_number = request.GET.get('page')
    context['contacts'] = paginator.get_page(page_number)
    context['categories'] = [category['name'] for category in Category.objects.values('name')]
    
    context['contact_form'] = ContactForm()
    
    return render(request, 'contacts/index.html', context)