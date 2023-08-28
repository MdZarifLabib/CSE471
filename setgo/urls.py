from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from setgo import settings

from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('home/', include('base.urls')),
    path('tourist/', include('base.urls')),
    path('details/', include('base.urls')),
    path('about/', include('base.urls')),
    path('contact/', include('base.urls')),
    path('packages/', include('base.urls')),
    path('ultimateitem/', include('base.urls')),
    path('luxuryitem/', include('base.urls')),
    path('budgetitem/', include('base.urls')),
   
    

    #Class base view
    
    #path for login:
    path('auth/',include('django.contrib.auth.urls')),

    #path for logout:
    path('auth/logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='myapp_logout'),

    #path for signup:
    path('', include('account.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
