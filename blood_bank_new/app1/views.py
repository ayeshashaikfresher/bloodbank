from django.shortcuts import render
from .models import InboxModel,OrganizationModel,DonorModel
from .forms import OrganizationForm
def indexPage(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request, "login.html")
def checkUser(request):
    user = request.POST.get("username")
    password = request.POST.get("password")
    if user == "admin" and password == "admin":
        return render(request,"welcome.html")
    else:
        return render(request, "login.html", {"error": "Invalid Details"})
def inboxPage(request):
    inbox_data = InboxModel.objects.all()
    return render(request, "inboxpage.html",{"data":inbox_data})
def organizationPage(request):
    org_form = OrganizationForm()
    return render(request,"organizationReg.html",{"data":org_form})
def saveOrganization(request):
    id = request.POST.get("org_id")
    name = request.POST.get("org_name")
    address = request.POST.get("org_address")
    country = request.POST.get("org_country")
    state = request.POST.get("org_state")
    city = request.POST.get("org_city")
    email =  request.POST.get("org_email")
    password = request.POST.get("org_password")
    contact = request.POST.get("org_contact")
    OrganizationModel(org_id=id, org_name=name, org_address=address,
                      org_country=country, org_state=state, org_city=city, org_email=email,
                      org_password=password, org_contact=contact).save()
    return render(request,"organizationReg.html",{"msg":"Organization Added Successfully"})

def viewOrg(request):
    org_data = OrganizationModel.objects.all()
    return render(request,"vieworg.html",{"org":org_data})

def deleteEmployee(request):
    id = request.GET.get("x")
    OrganizationModel.objects.filter(org_id=id).delete()
    org_data = OrganizationModel.objects.all()
    return render(request, "vieworg.html",{"org":org_data,"msg":"Organization Deleted Successfully"})

def logOut(request):
    return render(request, "login.html", {"message": "Logout Succesfully"})

def donorPage(request):
    return render(request,"donorpage.html")

def checkDonor(request):
    userid = request.POST.get("d1")
    upass = request.POST.get("d2")
    try:
        login1 = DonorModel.objects.filter(donor_userid=userid, donor_password=upass)
        d1 = {
            "message": "Welcome User", "logindata": userid
        }
        return render(request, "welcome.html", d1)
    except DonorModel.DoesNotExist:
        return render(request, "index.html", {"message": "invalid user"})
def donorReg(request):
    return render(request,"donorregistration.html")
def saveDonor(request):
    name = request.POST.get("d1")
    userid = request.POST.get("d2")
    password = request.POST.get("d3")
    gender = request.POST.get("d4")
    email = request.POST.get("d5")
    contact = request.POST.get("d6")
    bloddgroup = request.POST.get("d7")
    state = request.POST.get("d8")
    city = request.POST.get("d9")
    age = request.POST.get("d10")
    weight = request.POST.get("d11")
    donate_date = request.POST.get("d12")
    DonorModel(donor_name=name,donor_userid=userid,donor_password=password,
               donor_gender=gender,donor_email=email,donor_contact=contact,donor_bloodgroup=bloddgroup,
               donor_state=state,donor_city=city,donor_age=age,donor_weight=weight,donor_donatedate=donate_date).save()
    return render(request,"donorregistration.html", {"msg": "Donor Added Successfully"})

def updateDonor(request):
    return render(request,"updatedonor.html")

def viewDonor(request):
    return None

def orgLogin(request):
    return render(request,"orgLogin.html")

def checkOrg(request):
    username = request.POST.get("d1")
    upass = request.POST.get("d2")
    try:
        login1 = OrganizationModel.objects.filter(org_name=username, org_password=upass)
        return render(request, "welcome.html", {"message": "Welcome User", "logindata": username})
    except OrganizationModel.DoesNotExist:
        return render(request, "orgLogin.html", {"message": "invalid user"})

def logoutDonor(request):
    return render(request, "donorpage.html", {"message": "Logout Succesfully"})

def logoutOrg(request):
    return render(request, "orgLogin.html", {"message": "Logout Succesfully"})
