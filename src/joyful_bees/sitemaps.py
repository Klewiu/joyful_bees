from django.contrib import sitemaps
from django.urls import reverse


class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    # The below method returns all urls defined in urls.py file

    def items(self):

        return [
            'page-home', 
            'page-about', 
            'page-contact', 
            'page-privacy', 
            'page-terms', 
            'page-faq', 
            'page-news', 
            'page-info', 
            'page-products', 
            # 'newsletter' removed while newsletter is disabled
            ]

    def location(self, item):
        return reverse(item)
