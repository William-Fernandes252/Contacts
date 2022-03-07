from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contact, Category
from .forms import ContactForm
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView


class IndexView(TemplateView):
    template_name = 'contacts/index.html'
    search = False

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        if kwargs.get('category'):
            contacts = Contact.objects.filter(show = True, category__name = kwargs.get('category'))
            
        elif self.search:
            fields = Concat('name', Value(' '), 'surname')
    
            context['search'] = self.request.GET.get('term')        
            if context['search'] is None or not context['search']:
                messages.error(self.request, 'Search field cannot be empty.')
                contacts = Contact.objects.filter(show = True)
            
            contacts = Contact.objects.annotate(
                full_name = fields
            ).filter(
                Q(full_name__icontains = context['search']) | 
                Q(phone__icontains = context['search'])
            )
            
        else:
            contacts = Contact.objects.filter(show = True)
            
        paginator = Paginator(contacts, 20)
        page_number = self.request.GET.get('page')
        context['contacts'] = paginator.get_page(page_number)
        context['categories'] = [category['name'] for category in Category.objects.values('name')]
        
        context['form'] = ContactForm()
        
        return context
        

class ContactView(DetailView):
    template_name = 'contacts/contact.html'
    model = Contact
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        
        context['contact'] = super().get_object()
        if not context['contact'].show:
            raise Http404
        
        context['form'] = ContactForm(instance=context['contact'])
        return context
        
    
def add(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "New contact has been added!")
    else:
        messages.error(request, "Invalid contact.")
    return HttpResponseRedirect(reverse('index'))


def edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
        form.save()
        messages.success(request, "Contact updated!")
    else:
        messages.error(request, "Invalid input.")
    return HttpResponseRedirect(reverse('index'))


def delete(request):
    ids = request.POST.get('contacts')
    if ids:
        Contact.objects.filter(pk__in = ids).delete()
        messages.success(request, "Contacts deleted.")  
    return HttpResponseRedirect(reverse('index'))