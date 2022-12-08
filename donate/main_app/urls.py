from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('index/', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('contactus/', views.contactus, name='contactus'),
  path('signup-donor/', views.signup_donor, name='signup_donor'),
  path('Donate/', views.Donate_index, name='index'),
  path('Donate/<int:Donate_id>/', views.Donate_detail, name='detail'),
  path('Donate/create/', views.DonateCreate.as_view(), name='Donate_create'),
  path('Donate/<int:pk>/update/', views.DonateUpdate.as_view(), name='Donate_update'),
  path('Donate/<int:pk>/delete/', views.DonateDelete.as_view(), name='Donate_delete'),
   #USER SINGUP
  path('accounts/signup/', views.signup, name='signup'),
  path('index/all/', views.index_donate, name='index_donate'),
  path('Donate/<int:pk>/collect/', views.donate_collect, name='donate_collect'),
  path('Donate/<int:Donate_id>/add_photo/', views.add_photo, name='add_photo'),
 
]