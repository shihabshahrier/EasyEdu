from django.shortcuts import render
from users.models import STUDENT, FACULTY, ORG, User
from orgAdmin.models import Announcement

# Create your views here.
def studentHome(request):
    # user = ORG.objects.get(user=User.objects.get(username=request.user))
    # obj = Announcement.objects.filter(org=user)
    return render(request, './student/navbar.html')
