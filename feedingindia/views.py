from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from feedingindia.models import Volunteer



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



