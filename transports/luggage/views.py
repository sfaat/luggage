from django.http import response
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Notification, Price,Customer,FormField
from django.views import View
from django.core.mail import send_mail
from django.conf import settings

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
    
    return render(request, 'price.html')


def booknow1(request):
    return render(request, 'book1.html')
    


def booknow(request):
    
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


import ipdb
def updateprofile(request):
    if request.method == "POST":
        # ipdb.set_trace()
        nm = request.POST.get('Name')
        Address = request.POST.get('Address')
        Emailid = request.POST.get('Emailid')
        mobileno = request.POST.get('mobileno')
        Password = request.POST.get('Password')
        Postcode = request.POST.get('Postcode')
        email = request.session['email']
        data = Customer.objects.get(emailid=email)
        data.name = nm
        data.address = Address
        data.mobile = mobileno
        data.emailid = Emailid
        data.postcode = Postcode
        data.password = Password
        data.save()
        return render(request,'adminpanel/customerprofile.html',{'data':data})
    else:
        email = request.session['email']
        data = Customer.objects.get(emailid=email)
        return render(request,'adminpanel/customerprofile.html',{'data':data})


def customerlogin(request):
    if request.method == "POST":
        # email = request.POST['email']
        # password = request.POST['password']
        try:
            # user = Customer.objects.get(emailid=email,password=password)
            # request.session['email'] = email
            login = Customer.objects.get(emailid=request.POST['email'], password=request.POST['password']) 
            request.session['email'] = request.POST['email']
            return redirect('/customerdashboard/')
        except:
            messages.success(request, 'Password or Username is incorrect!!!')
            return redirect('/customerlogin/')
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

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        # email = settings.EMAIL_HOST_USER
        data={
            'name':name,
            'email':email,
            'phone':phone,
            'subject':subject,
            'message':message
        }

        message= '''
        Name: {}
        Phone No :{}
        message: {}
        From: {}
        subject :{}
        '''.format(data['name'],data['phone'],data['message'],data['email'],data['subject'])
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email,],fail_silently=False)
        
    
    
    return render(request,'index.html')

def table1(request):
    return render(request,"table1.html")


def adminetable(request):
    return render(request,"adminpanel/adminetable.html")

        
      

    