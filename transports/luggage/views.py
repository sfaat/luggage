from django.http import response
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Notification, Price,Customer,FormField
from django.views import View

def notification(request):
    if request.method == "POST":
        date = request.POST.get('date')
        email = request.POST.get('email')
        reg = Notification(
            date =  date,
            email = email    
        )
        reg.save()
        messages.success(request, 'your request is submitted!!!')
        return redirect('/')
    else:
        return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def price(request):
    # trip_type=request.COOKIES["trip_type"]
    # laguage_type=request.COOKIES["laguage_type"]
    # from1=request.COOKIES["from1"]
    # to=request.COOKIES["to"]
    # inputCheckIn=request.COOKIES["inputCheckIn"]
    # frmDateReg=request.COOKIES["frmDateReg"]
    # contaxt={"trip_type":trip_type,"laguage_type":laguage_type,"from1":from1,"to":to,"inputCheckIn":inputCheckIn,"frmDateReg":frmDateReg}
    return render(request, 'price.html')


def booknow1(request):
    return render(request, 'book1.html')
    


def booknow(request):
    # trip_type=request.COOKIES["trip_type"]
    # laguage_type=request.COOKIES["laguage_type"]
    # from1=request.COOKIES["from1"]
    # to=request.COOKIES["to"]
    # inputCheckIn=request.COOKIES["inputCheckIn"]
    # frmDateReg=request.COOKIES["frmDateReg"]
    # contaxt={"trip_type":trip_type,"laguage_type":laguage_type,"from1":from1,"to":to,"inputCheckIn":inputCheckIn,"frmDateReg":frmDateReg}
    return render(request,'book.html')


def search(request):
    if request.method=="POST":  
        trip_type=request.POST['trip_type']
        laguage_type=request.POST['laguage_type']
        from1=request.POST['from1']
        to=request.POST['to']
        inputCheckIn=request.POST['inputCheckIn']
        frmDateReg=request.POST['frmDateReg']
        c=Customer.objects.get(id=11)
        form=FormField(tripe_type=trip_type, laguage_type=laguage_type,From=from1 ,To=to,arrival=inputCheckIn,Return=frmDateReg, user=c)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(frmDateReg,inputCheckIn,to,from1,laguage_type,trip_type)
        form.save()
        contaxt={"trip_type":trip_type,"laguage_type":laguage_type,"from1":from1,"to":to,"inputCheckIn":inputCheckIn,"frmDateReg":frmDateReg}
        response=render(request,'book.html',contaxt)
        response.set_cookie('trip_type',trip_type)
        response.set_cookie('laguage_type',laguage_type)
        response.set_cookie('from1',from1)
        response.set_cookie('to',to)
        response.set_cookie('inputCheckIn',inputCheckIn)
        response.set_cookie('frmDateReg',frmDateReg)
    return response

class superadmin(View): 
    def get(self,request):
        return render(request, 'adminpanel/index.html')

def buttons(request):
    return render(request,'adminpanel/buttons.html')

def cards(request):
    return render(request,'adminpanel/cards.html')

def charts(request):
    return render(request,'adminpanel/charts.html')

def register(request):
    return render(request,'adminpanel/register.html')

def tables(request):
    return render(request,'adminpanel/tables.html')

def utilities_animation(request):
    return render(request,'adminpanel/utilities-animation.html')

def utilities_border(request):
    return render(request,'adminpanel/utilities-border.html')

def utilities_color(request):
    return render(request,'adminpanel/utilities-color.html')

def customerdashboard(request):
    if 'email' in request.session:
        return render(request,'adminpanel/customerdashboard.html')
    else:
        return redirect('/customerlogin/')


def utilities_other(request):
    return render(request,'adminpanel/utilities-other.html')
    
def how_it_works(request):
    return render(request,'adminpanel/how_it_works.html')
    
def features(request):
    return render(request,'adminpanel/features.html')

def updateprofile(request):
    return render(request, 'adminpanel/customerprofile.html')


def customerlogout(request):
	if request.method == 'GET':
		request.session.flush()
		return redirect('/customerlogin/')

def updateprofile(request):
    if request.method == "POST":
        nm = request.POST.get('Name')
        Address = request.POST.get('Address')
        Emailid = request.POST.get('Emailid')
        mobileno = request.POST.get('mobileno')
        Password = request.POST.get('Password')
        Postcode = request.POST.get('Postcode')
        email = request.session['email']
        data = Customer.objects.get(emailid=email)
        data.name = nm,
        data.address = Address,
        data.mobile = mobileno,
        data.emailid = Emailid,
        data.postcode = Postcode,
        data.password = Password,
        data.save()
        return render(request,'adminpanel/customerprofile.html',{'data':data})
    else:
        email = request.session['email']
        data = Customer.objects.get(emailid=email)
        return render(request,'adminpanel/customerprofile.html',{'data':data})


def customerlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Customer.objects.get(emailid=email,password=password)
            user.save()
        except:
            messages.success(request, 'Password or Username is incorrect!!!')
            return redirect('/customerlogin/')
        request.session['email'] = email
        return redirect('/customerdashboard/')
    else:
        return render(request,'adminpanel/customerlogin.html')

def customer(request):
    if request.method == "POST":
        nm = request.POST.get('Name')
        Address = request.POST.get('Address')
        Emailid = request.POST.get('Emailid')
        mobileno = request.POST.get('mobileno')
        Password = request.POST.get('Password')
        Postcode = request.POST.get('Postcode')
        reg = Customer(
            name = nm,
            address = Address,
            mobile = mobileno,
            emailid = Emailid,
            postcode = Postcode,
            password = Password,
        )
        reg.save()
        messages.success(request,'Registration is succesfully!!!!!')
        return render(request,'adminpanel/customerlogin.html')
    else:
        return render(request,'adminpanel/register.html')

def checkout(request):
    return render(request,"checkout.html")
def checkout1(request):
    return render(request,"checkout1.html")


def calculator(request):
    return render(request,"calculator.html")    


def cookie(request):
    
    return render(request,"cookie.html")
      

    