from django.shortcuts import render
from base import models
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    post_Objects = models.district.objects.all()
    destination_Objects = models.popular_Destination.objects.all()
    packages_objects = models.packages.objects.all()
    
    return render(request,'index.html',{"post_Objects":post_Objects,"destination_Objects":destination_Objects,"packages_objects":packages_objects})
    

#view for all packages page:
def touristSpots(request):
    packages_objects = models.packages.objects.all()
    return render(request,'touristSpots.html',{"packages_objects":packages_objects})

#view for detail:
def details(request,pk):
    spot_Object = models.packages.objects.get(id = pk)
    return render(request,'spotDetails.html',{"spot_Object":spot_Object})

#views for packages:
@login_required
def viewPackages(request):
    return render(request,'allPackages.html')
@login_required
def ultimatePackageView(request):
    packages_objects = models.packages.objects.all()
    return render(request,'UltimatePackage.html',{"packages_objects":packages_objects})
@login_required
def luxuryPackageView(request):
    packages_objects = models.packages.objects.all()
    return render(request,'LuxuryPackage.html',{"packages_objects":packages_objects})
@login_required
def budgetPackageView(request):
    packages_objects = models.packages.objects.all()
    return render(request,'BudgetPackage.html',{"packages_objects":packages_objects})
def ultimateSpotView(request,pk):
    spot_Object = models.packages.objects.get(id = pk)
    return render(request,'ultimateSpot.html',{"spot_Object":spot_Object})
@login_required
def luxurySpotView(request,pk):
    spot_Object = models.packages.objects.get(id = pk)
    return render(request,'luxurySpot.html',{"spot_Object":spot_Object})
@login_required
def budgetSpotView(request,pk):
    spot_Object = models.packages.objects.get(id = pk)
    return render(request,'budgetSpot.html',{"spot_Object":spot_Object})


def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request, 'contact.html')
def contactReply(request):
    return render(request, 'contact reply.html')