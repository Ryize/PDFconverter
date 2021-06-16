from django.urls import path

from PDFconverter.views import index_page

urlpatterns = [
    path('', index_page, name='index')
]