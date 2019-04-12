from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from feedingindia.models import Volunteer, Donater, Shelter, Donation, Pickup
from feedingindia.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve
from time import gmtime, strftime

@csrf_exempt
def upvoter1(request, uid):
    delivery_instance = Pickup.objects.get(contact_donator=uid)
    delivery_instance.counter = delivery_instance.counter + 1
    delivery_instance.save()
    return redirect("all_delivery")

def pickup(request):
  return render(request, 'feedingindia/Volunteer/pickup.html')

def all_delivery(request):
  date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(" ")
  date = date_time[0].split("-")
  time = date_time[1]
  instance = Pickup.objects.all()
  context_dict={}
  arr = []
  for i in instance:
    volunteer_data = []
    vol_date = i.date_delivery.split("-")
    if(int(vol_date[0])>int(date[0])):
      if(int(vol_date[1])>int(date[1])):
        if(int(vol_date[2])>int(date[2])):
          volunteer_data = {}
          volunteer_data['name_donator'] = i.name_donator
          volunteer_data['contact_donator'] = i.contact_donator
          volunteer_data['name_shelter'] = i.name_shelter
          volunteer_data['address_shelter'] = i.address_shelter
          volunteer_data['time_delivery'] = i.time_delivery
          volunteer_data['date_delivery'] = i.date_delivery
          volunteer_data['food_for_donate'] = i.food_for_donate
          volunteer_data['counter'] = i.counter
          arr.append(volunteer_data)
  context_dict['volunteer_arr'] = arr
  # print(context_dict)
  return render(request, 'feedingindia/Volunteer/all_delivered.html', context_dict)

def add_data_pickup(request):
  Pickup.objects.create(
        name_donator=request.POST.get("name_donator"),
        contact_donator=request.POST.get("contact_donator"),
        name_shelter=request.POST.get("name_shelter"),
        address_shelter=request.POST.get("address_shelter"),
        time_delivery=request.POST.get("time_delivery"),
        date_delivery=request.POST.get("date_delivery"),
        food_for_donate=request.POST.get("food_for_donate"),
        counter=0
        )
  return render(request, 'feedingindia/thankyou_donation.html')





@csrf_exempt
def upvoter(request, uid):
    donation_instance = Donation.objects.get(contact=uid)
    donation_instance.counter = donation_instance.counter + 1
    donation_instance.save()
    return redirect("all_donating")

def donating(request):
  return render(request, 'feedingindia/Donator/donating.html')

def all_donating(request):
  date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(" ")
  date = date_time[0].split("-")
  time = date_time[1]
  instance = Donation.objects.all()
  context_dict={}
  arr = []
  for i in instance:
    volunteer_data = []
    vol_date = i.date_donate.split("-")
    if(int(vol_date[0])>int(date[0])):
      if(int(vol_date[1])>int(date[1])):
        if(int(vol_date[2])>int(date[2])):
          volunteer_data = {}
          volunteer_data['name'] = i.name
          volunteer_data['contact'] = i.contact
          volunteer_data['address'] = i.address
          volunteer_data['type_of_donation'] = i.type_of_donation
          volunteer_data['time_donate'] = i.time_donate
          volunteer_data['date_donate'] = i.date_donate
          volunteer_data['food_for_donate'] = i.food_for_donate
          volunteer_data['counter'] = i.counter
          arr.append(volunteer_data)
  context_dict['volunteer_arr'] = arr
  # print(context_dict)
  return render(request, 'feedingindia/volunteer_pickup.html', context_dict)


def add_data_donating(request):
  instance = Donation.objects.create(
        name=request.POST.get("name"),
        contact=request.POST.get("contact"),
        address=request.POST.get("address"),
        type_of_donation = request.POST.get("type_of_donation"),
        time_donate=request.POST.get("time"),
        date_donate=request.POST.get("date"),
        food_for_donate=request.POST.get("food_for"),
        counter=0,
        )
   
  return render(request, 'feedingindia/thankyou_donation.html')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    dictionary = {'form': form}
    return render(request, 'folder/signup.html', dictionary)


@csrf_exempt
def login(request):
    form = LoginForm()
    context_dict = {}
    context_dict['form'] = form
    error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            current_url = resolve(request.path_info).url_name
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            error_message = "Incorrect username or password"
            form = LoginForm()
            context_dict['form'] = form
            context_dict['error_message'] = error_message
    return render(request, 'folder/login.html', context_dict)


@csrf_exempt
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def dashboard(request):
  volunteer_instance = Volunteer.objects.all()
  context_dict={}
  arr = []
  for i in volunteer_instance:
    volunteer_data = []
    volunteer_data.append(float(i.latitude))
    volunteer_data.append(float(i.longitude))
    arr.append(volunteer_data)
  context_dict['volunteer_coordinate'] = arr

  donater_instance = Donater.objects.all()
  arr1 = []
  for i in donater_instance:
    donater_data = []
    donater_data.append(float(i.latitude))
    donater_data.append(float(i.longitude))
    arr1.append(donater_data)
  context_dict['donater_coordinate'] = arr1 

  shelter_instance = Shelter.objects.all()
  arr2 = []
  for i in shelter_instance:
    shelter_data = []
    shelter_data.append(float(i.latitude))
    shelter_data.append(float(i.longitude))
    arr2.append(shelter_data)
  context_dict['shelter_coordinate'] = arr2 
  print(context_dict)
  return render(request, 'folder/dashboard.html',context_dict)









def volunteer(request):
  return render(request, 'feedingindia/Volunteer/volunteer.html')

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
  return render(request, 'feedingindia/thankyou_register.html')


def donater(request):
  return render(request, 'feedingindia/Donator/donater.html')


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
  return render(request, 'feedingindia/thankyou_register.html')

@login_required
def render_donator_data(request):
  donater_instance = Donater.objects.all()
  context_dict={}
  arr = []
  for i in donater_instance:
    donater_data = {}
    donater_data['partnering_entity'] = i.partnering_entity
    donater_data['institution'] = i.institution
    donater_data['name'] = i.name
    donater_data['contact'] = i.contact
    donater_data['email'] = i.email
    donater_data['designation'] = i.designation
    donater_data['address'] = i.address
    donater_data['pincode'] = i.pincode
    donater_data['additional'] = i.additional
    arr.append(donater_data)
  context_dict['arr'] = arr
  print(context_dict)
  return render(request, 'folder/dashboard/all_donators.html', context_dict)


def shelter(request):
  return render(request, 'feedingindia/Shelter/shelter.html')


@csrf_exempt
def data_add_shelter(request):
  s = ''
  for i in request.POST.getlist("support[]"):
    s = s + i + ","
  r = ''
  for i in request.POST.getlist("reg_status[]"):
    r = r + i + ","
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
            support=s,
            reg_status=r,
            name_incharge=request.POST.get("name_incharge"),
            contact_incharge=request.POST.get("contact_incharge"),
            email_incharge=request.POST.get("email_incharge"),
            latitude=request.POST.get("lat"),
            longitude=request.POST.get("lng")
            )
  return render(request, 'feedingindia/thankyou_register.html')

@login_required
def render_shelter_data_private(request):
  shelter_instance = Shelter.objects.all()
  context_dict={}
  arr = []
  for i in shelter_instance:
    shelter_data = {}
    shelter_data['name_hunger_spot'] = i.name_hunger_spot
    shelter_data['address'] = i.address
    shelter_data['pincode'] = i.pincode
    shelter_data['total_benefitiaries'] = i.total_benefitiaries
    shelter_data['type_shelter'] = i.type_shelter
    shelter_data['raw_food'] = i.raw_food
    shelter_data['cooked_food'] = i.cooked_food
    shelter_data['preference'] = i.preference
    shelter_data['time_range'] = i.time_range
    shelter_data['heat_food'] = i.heat_food
    shelter_data['refrigerate_food'] = i.refrigerate_food
    shelter_data['external_support'] = i.external_support
    shelter_data['support'] = i.support
    shelter_data['reg_status'] = i.reg_status
    shelter_data['name_incharge'] = i.name_incharge
    shelter_data['contact_incharge'] = i.contact_incharge
    shelter_data['email_incharge'] = i.email_incharge
    arr.append(shelter_data)
  context_dict['arr'] = arr
  print(context_dict)
  return render(request, 'folder/dashboard/all_shelter.html', context_dict)

def render_shelter_data_public(request):
  shelter_instance = Shelter.objects.all()
  context_dict={}
  arr = []
  for i in shelter_instance:
    shelter_data = {}
    shelter_data['name_hunger_spot'] = i.name_hunger_spot
    shelter_data['address'] = i.address
    shelter_data['pincode'] = i.pincode
    shelter_data['total_benefitiaries'] = i.total_benefitiaries
    shelter_data['type_shelter'] = i.type_shelter
    shelter_data['raw_food'] = i.raw_food
    shelter_data['cooked_food'] = i.cooked_food
    shelter_data['preference'] = i.preference
    shelter_data['time_range'] = i.time_range
    shelter_data['heat_food'] = i.heat_food
    shelter_data['refrigerate_food'] = i.refrigerate_food
    shelter_data['external_support'] = i.external_support
    shelter_data['support'] = i.support
    shelter_data['reg_status'] = i.reg_status
    shelter_data['name_incharge'] = i.name_incharge
    shelter_data['contact_incharge'] = i.contact_incharge
    shelter_data['email_incharge'] = i.email_incharge
    arr.append(shelter_data)
  context_dict['arr'] = arr
  print(context_dict)
  return render(request, 'feedingindia/Shelter/all_shelter.html', context_dict)

@login_required
def render_volunteer_data(request):
  volunteer_instance = Volunteer.objects.all()
  context_dict={}
  arr = []
  for i in volunteer_instance:
    volunteer_data = {}
    volunteer_data['name'] = i.name
    volunteer_data['email'] = i.email
    volunteer_data['contact'] = i.contact
    volunteer_data['address'] = i.address
    volunteer_data['pincode'] = i.pincode
    volunteer_data['age'] = i.age
    volunteer_data['institution'] = i.institution
    volunteer_data['educational_background'] = i.educational_background
    volunteer_data['contribution_time'] = i.contribution_time
    volunteer_data['why_join'] = i.why_join
    volunteer_data['latitude'] = i.latitude
    volunteer_data['longitude'] = i.longitude
    arr.append(volunteer_data)
  context_dict['arr'] = arr
  print(context_dict)
  return render(request, 'folder/dashboard/all_volunteer.html', context_dict)


def index(request):
  return render(request, 'feedingindia/index.html')


def donator_public(request):
  return render(request, 'feedingindia/donate.html')


def shelter_public(request):
  return render(request, 'feedingindia/shelter.html')


def volunteer_public(request):
  return render(request, 'feedingindia/volunteer.html')


def volunteer_cards(request):
  return render(request, 'feedingindia/Volunteer/volunteer_cards.html')


def donator_cards(request):
  return render(request, 'feedingindia/Donator/donator_cards.html')


def thankyou_register(request):
  return render(request, 'feedingindia/thankyou_register.html')

def thankyou_donation(request):
  return render(request, 'feedingindia/thankyou_donation.html')