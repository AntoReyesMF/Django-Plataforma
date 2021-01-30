from django.urls import path
from .views import HomePageView, NosotrosPageView, TyCPageView, ContactoPageView, FriendPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('nosotros', NosotrosPageView.as_view(), name="nosotros"),
    path('terminosycondiciones', TyCPageView.as_view(), name="tyc"),
    path('contacto', ContactoPageView.as_view(), name="contacto"),
    path('friends', FriendPageView.as_view(), name='friend')
]