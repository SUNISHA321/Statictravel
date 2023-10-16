from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def index(request):

    obj=Place.objects.all()
    team_obj = Team.objects.all()
    return render(request,"index.html",{'result':obj,'teamresult':team_obj})