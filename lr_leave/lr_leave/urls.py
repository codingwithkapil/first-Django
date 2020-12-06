"""lr_leave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('invoice/<str:d>/',views.invoice,name='invoice'),
    path('quotation',views.quotation,name='quotation'),
    path('add_client',views.add_client,name='add_client'),
    path('view_quotation',views.view_quotation,name='view_quotation'),
    path('update',views.update,name='update'),
    path('view_invoices',views.view_invoices,name='view_invoices'),
    path('view_invoice',views.view_invoice,name='view_invoice'),
    path('create_quotation',views.create_quotation,name='create_quotation')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)