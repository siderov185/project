from django.shortcuts import render
from haystack.query import SearchQuerySet
from django.core.paginator import Paginator
from company.models import Company
from faqs.models import Faqs
from contacts.models import Contacts
from externallinks.models import ExternalLinks
from textpages.models import TextPages


def search_view(request):

    query = request.GET.get('q', None)
    context = {
        'results': [],
        'search': query,
    }
    if query:
        context['results'] = SearchQuerySet().filter(content=query)
        for item in context['results']:
            print(item)
    paginator = Paginator(context['results'], 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'search/search.html', context)


def sitemap_view(request):
    companies_all = Company.objects.filter(active=True)
    company = Company.objects.filter(active=True)
    faqs = Faqs.objects.filter(active=True)
    contacts = Contacts.objects.filter(active=True)
    externallinks = ExternalLinks.objects.filter(active=True)
    textpages = TextPages.objects.filter(active=True)
    context = {
        'companies_all': companies_all,
        'company': company,
        'contacts': contacts,
        'faqs': faqs,
        'externallinks': externallinks,
        'textpages': textpages,
    }

    return render(request, 'pages/sitemap.html', context)