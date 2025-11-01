from django.urls import path  # --- To create url
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('display/',views.display,name="display"),
    path('specific/<int:key>/',views.specific,name="specific"),
    path('update/<int:key>/',views.update,name="update"),
    path('delete/<int:key>/',views.deleteDestination,name="delete"),
    path('create/',views.create,name='create'),


    path('createCarteg/',views.create_country,name='create_country'),
    path('displayCarteg/',views.read_country,name='read_country'),
    path('updateCarteg/<int:key>/',views.update_country,name='update_country'),
    path('deleteCarteg/<int:key>/',views.delete_country,name='delete_country'),
    path('restore/<int:key>/',views.restore_Destination,name='restore'),
    path('history/',views.Destination_history,name='history'),
]