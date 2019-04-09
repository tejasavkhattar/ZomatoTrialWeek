from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from feedingindia.models import Volunteer, Donater, Shelter



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


def shelter(request):
	return render(request, 'feedingindia/shelter.html')


@csrf_exempt
def data_add_shelter(request):
	context_dict = {}
	context_dict["name_hunger_spot"] = request.POST.get("name_hunger_spot")
	context_dict["address"] = request.POST.get("address")
	context_dict["pincode"] = request.POST.get("pincode")
	context_dict["total_benefitiaries"] = request.POST.get("total_benefitiaries")
	context_dict["type_shelter"] = request.POST.get("type_shelter")
	context_dict["raw_food"] = request.POST.get("raw_food")
	context_dict["cooked_food"] = request.POST.get("cooked_food")
	context_dict["preference"] = request.POST.get("preference")
	context_dict["time_range"] = request.POST.get("time_range")
	context_dict["heat_food"] = request.POST.get("heat_food")
	context_dict["refrigerate_food"] = request.POST.get("refrigerate_food")
	context_dict["external_support"] = request.POST.get("external_support")
	context_dict["support"] = request.POST.get("support")
	context_dict["reg_status"] = request.POST.get("reg_status")
	context_dict["name_incharge"] = request.POST.get("name_incharge")
	context_dict["contact_incharge"] = request.POST.get("contact_incharge")
	context_dict["email_incharge"] = request.POST.get("email_incharge")
	context_dict["latitude"] = request.POST.get("lat")
	context_dict["longitude"] = request.POST.get("lng")
	shelter_instance = Shelter.objects.create(
            name_hunger_spot=request.POST.get("name_hunger_spot"),
            address=request.POST.get("address"),
            pincode=request.POST.get("pincode"),
            total_benefitiaries=request.POST.get("total_benefitiaries"),
            type_shelter=request.POST.get("type_shelter"),
            raw_food=request.POST.get("raw_food"),
            cooked_food=request.POST.get("cooked_food"),
            preference=request.POST.get("preference"),
            time_range=request.POST.get("time_range"),
            heat_food=request.POST.get("heat_food"),
            refrigerate_food=request.POST.get("refrigerate_food"),
            external_support=request.POST.get("external_support"),
            support=request.POST.get("support"),
            reg_status=request.POST.get("reg_status"),
            name_incharge=request.POST.get("name_incharge"),
            contact_incharge=request.POST.get("contact_incharge"),
            email_incharge=request.POST.get("email_incharge"),
            latitude=request.POST.get("lat"),
            longitude=request.POST.get("lng")
            )
	print(context_dict)


	
