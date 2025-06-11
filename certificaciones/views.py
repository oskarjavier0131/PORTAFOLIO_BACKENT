from django.shortcuts import render, get_object_or_404
from .models import Certificacion

def certifications_post(request):
    certifications = Certificacion.objects.all()
    return render(request, 'certifications_list.html', {'certifications': certifications})

def certification_detail(request, certification_id):
    certification = get_object_or_404(Certificacion, pk=certification_id)
    return render(request, 'certification_detail.html', {'certification': certification})