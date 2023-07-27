from django.shortcuts import render

# Create your views here.
def facultyHome(request):
    return render(request, './faculty/navbar.html')