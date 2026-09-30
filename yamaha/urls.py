from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ListView, CreateView, UpdatedeleteView, GetbyId, RegisterView,LoginView
urlpatterns = [
    # path('login', LoginView.as_view()),
    path('list/',ListView.as_view()),
    path('list/<int:pk>/',GetbyId.as_view()),
    path('post/', CreateView.as_view()),
    path('update/<int:pk>/', UpdatedeleteView.as_view()),
    path('register/', RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    #path('del/<int:id>', DeleteView.as_view()),
    #path('update/<int:id>',UpdateView.as_view()),
    path('login/', LoginView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]


