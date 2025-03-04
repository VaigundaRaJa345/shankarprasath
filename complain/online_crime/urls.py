from django.urls import path
from . import views

# Define URL patterns for the complaints app
urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # About page
    path('about/', views.about, name='about'),

    # Track Complaint page
    path("track_complaint", views.track_complaint, name="track_complaint"),
    path("about/track", views.track_complaint, name="track_complaint"),
    path("about/register", views.register, name='register_complaint'),


    # Register Complaint page
    path('register',views.register, name='register_complaint'),

    # Help page
    path('help/', views.help_page, name='help'),

     path('register_complaint/', views.register_complaint, name='register_complaint'),

    

]
