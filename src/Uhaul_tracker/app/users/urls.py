from django.urls import path 
from . import views 

urlpatterns = [ 
    path('create_user/', views.add_user), 
    path('delete_user/<user_id>', views.remove_user)
]