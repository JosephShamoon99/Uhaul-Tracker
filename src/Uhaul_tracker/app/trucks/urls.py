from django.urls import path 
from . import views 

urlpatterns = [ 
    path('search/<locations_id>', views.trucks_by_location), 
    path('rent/<truck_id>', views.rent), 
    path('return/<truck_id>', views.return_truck)
    
    
]