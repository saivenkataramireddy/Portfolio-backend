from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.get_portfolio_data, name='get_portfolio_data'),
    path('projects/<uuid:project_id>/', views.project_detail, name='api_project_detail'),
    path('contact/', views.contact_submit, name='api_contact_submit'),
]
