from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:car_id>',views.car_detail, name= 'details'),
    path('postupdate/<int:id>',views.postupdate, name= 'postupdate'),
]