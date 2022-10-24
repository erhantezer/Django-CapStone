
from django.urls import path,include

from .views import (
    RegisterView, 
    # logout
    )

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')), #!users / auth tan sonraki login  logout password/reset/ vb işlemleri otomatik gelecek
    path("register/", RegisterView.as_view()),
    # path("logouts/",logout,name="logout_user"),
]