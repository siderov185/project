from django.contrib.sitemaps import Sitemap
from company.models import Company
from faqs.models import Faqs
from contacts.models import Contacts
from externallinks.models import ExternalLinks
from textpages.models import TextPages
from django.urls import reverse


class CompanySitemap(Sitemap):
    def items(self):
        return Company.objects.filter(active=True)


class TextPagesSitemap(Sitemap):
    def items(self):
        return TextPages.objects.filter(active=True)


class StaticSitemap(Sitemap):
    def items(self):
        return ['faqs', 'externallinks', 'contacts',]

    def location(self, item):
        return reverse(item)

