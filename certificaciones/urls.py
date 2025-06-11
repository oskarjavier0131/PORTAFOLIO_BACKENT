from django.urls import path
from .views import certifications_post, certification_detail
app_name = 'certificaciones'

urlpatterns = [
    path('', certifications_post, name='certifications'),
    path('<certification_id>', certification_detail, name="certification_detail"),
]