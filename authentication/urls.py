from django.urls import path
from authentication.views import login, signup, test_token, logout





urlpatterns = [
    path('login/', login ),
    path('signup/',signup),
    path('test_token',test_token),
    path('logout/', logout),
    
]
