from django.urls import path  # --- To create url
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('display/',views.display,name="display"),
    path('specific/<int:key>/',views.specific,name="specific"),
    path('update/<int:key>/',views.update,name="update"),
    path('delete/<int:key>/',views.deleteDestination,name="delete"),
    path('create/',views.create,name='create'),
]