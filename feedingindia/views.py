from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from feedingindia.models import Volunteer, Donater



def volunteer(request):
	return render(request, 'feedingindia/volunteer.html')

@csrf_exempt
def data_add_volunteer(request):
	context_dict = {}
	context_dict["name"] = request.POST.get("name")
	context_dict["email"] = request.POST.get("email")
	context_dict["contact"] = request.POST.get("contact")
	context_dict["address"] = request.POST.get("address")
	context_dict["pincode"] = request.POST.get("pincode")
	context_dict["age"] = request.POST.get("age")
	context_dict["institution"] = request.POST.get("institution")
	context_dict["educational_background"] = request.POST.get("educational_background")
	context_dict["contribution_time"] = request.POST.get("contribution_time")
	context_dict["why_join"] = request.POST.get("why_join")
	context_dict["latitude"] = request.POST.get("lat")
	context_dict["longitude"] = request.POST.get("lng")
	volunteer_instance = Volunteer.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            contact=request.POST.get("contact"),
            address=request.POST.get("address"),
            pincode=request.POST.get("pincode"),
            age=request.POST.get("age"),
            institution=request.POST.get("institution"),
            educational_background=request.POST.get("educational_background"),
            contribution_time=request.POST.get("contribution_time"),
            why_join=request.POST.get("why_join"),
            latitude=request.POST.get("lat"),
            longitude=request.POST.get("lng")
            )
	print(context_dict)

def donater(request):
	return render(request, 'feedingindia/donater.html')

@csrf_exempt
def data_add_donater(request):
	context_dict = {}
	context_dict["partnering_entity"] = request.POST.get("partnering_entity")
	context_dict["institution"] = request.POST.get("institution")
	context_dict["name"] = request.POST.get("name")
	context_dict["contact"] = request.POST.get("contact")
	context_dict["email"] = request.POST.get("email")
	context_dict["designation"] = request.POST.get("designation")
	context_dict["address"] = request.POST.get("address")
	context_dict["pincode"] = request.POST.get("pincode")
	context_dict["additional"] = request.POST.get("additional")
	context_dict["latitude"] = request.POST.get("lat")
	context_dict["longitude"] = request.POST.get("lng")
	donater_instance = Donater.objects.create(
            partnering_entity=request.POST.get("partnering_entity"),
            institution=request.POST.get("institution"),
            name=request.POST.get("name"),
            contact=request.POST.get("contact"),
            email=request.POST.get("email"),
            designation=request.POST.get("designation"),
            address=request.POST.get("address"),
            pincode=request.POST.get("pincode"),
            additional=request.POST.get("additional"),
            latitude=request.POST.get("lat"),
            longitude=request.POST.get("lng")
            )
	print(context_dict)
