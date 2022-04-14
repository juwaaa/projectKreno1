from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='Index'),
    path('booking/<int:booking_id>', views.booking_by_id, name='booking_by_id'),
    path('account/register/',views.register,name='register'),

]