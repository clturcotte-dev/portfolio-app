from django.urls import path
from portfolioapp import views

urlpatterns = [
    #path('portfolioapp/', views.test, name='test'),
    path('portfolioapp/', views.project, name='project'),
]