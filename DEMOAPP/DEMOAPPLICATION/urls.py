from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('hi', views.hi, name='home-page'),
    path('news', views.news, name='news-page'),
    path('guestform', views.guestform, name='Guest-form'),
    path('about', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
