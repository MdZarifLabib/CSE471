from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.home,name = 'home'),
    path("spots/",views.touristSpots ,name = 'touristSpots'),
    path("<int:pk>/",views.details , name = 'detail_view'),
    path("viewAbout/",views.about , name = 'about'),
    path("viewContact/",views.contact , name = 'contact'),
    path("contactReply/",views.contactReply , name = 'contact'),
    path("viewPackages/", views.viewPackages, name = 'viewPackages'),
    path("ultimate/", views.ultimatePackageView, name = 'ultimatePackageView'),
    path("luxury/", views.luxuryPackageView, name = 'luxuryPackageView'),
    path("budget/", views.budgetPackageView, name = 'budgetPackageView'),
    path("item1/<int:pk>/",views.ultimateSpotView , name = 'ultimateSpotView'),
    path("item2/<int:pk>/",views.luxurySpotView , name = 'luxurySpotView'),
    path("item3/<int:pk>/",views.budgetSpotView , name = 'luxurySpotView'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)