from django.conf.urls.defaults import *

from django.views.generic import list_detail
from webshop.views import *
from webshop.models import Product

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

prod = {
    "queryset" : Product.objects.all(),
    "template_name" : "product_list.html",
    }

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    ('^$', index),
    ('^p/$', list_detail.object_list, prod),
)
