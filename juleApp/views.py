from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from xhtml2pdf import pisa  
from django.template.loader import get_template
from datetime import date
import requests
import vonage
import random
import mysql.connector
from twilio.rest import Client


# Create your views here.


def homeApp(request):
    return render(request,'index.html')

def login(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def adminhome(request):
    return render(request,'adminhome.html')

def analyticalhome(request):
    return render(request,'analytical.html')



def dashboalhome(request):
    return render(request,'dashboard.html')



def roadhome(request):
    return render(request,'road.html')



def elechome(request):
    return render(request,'electrity.html')


def courthome(request):
    return render(request,'court.html')


def markethome(request):
    return render(request,'market.html')


def insdustryhome(request):
    return render(request,'indusstry.html')


def woterhome(request):
    return render(request,'Water.html')







def createaccount(request):
     if request.method=='POST':
        phoneNumber=request.POST['phone']
        amount=request.POST['amount']
        passowrd=request.POST['password']
        transactionid = "hLeOYrG1hTRtGmeJHqAs"
        url = f'http://localhost:9050/transaction/uriTrandaction/{phoneNumber}/{amount}/{passowrd}/{transactionid}'
        x = requests.post(url)
        if x.text =='SUCCESS':
            otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
            url = f'http://localhost:9050/transaction/phoneamount/{phoneNumber}'
            y = requests.get(url).json()
            balance = y['amount']
            accountSID = 'ACfb4fb93d2263b728c0e665fafc8f5fb6'
            tokens = 'e070002cfb3181ac094ca6ac0e8d569a'
            clients = Client(accountSID, tokens)

            messages = clients.messages.create(
            body='*164*S*Yello,Transaction of '+amount+' Frw has been successfully, Your Secret Number is: ' + otp +' and your New Balance is:' + str(balance)+' on Your MoMo Account.',    
            from_='+18149046986',
            to= "+250733915355"
             )
            password='0'
            saved=userdetail(username=phoneNumber,email=amount,password=password,repeatPassword=otp)
            saved.save()
            passworderror='Message sent,Check on your Phone.'
            return render(request,'signup.html', {"passworderror": passworderror})
        else:
            passworderror='Something went Wrong,try again.'
            return render(request,'signup.html', {"passworderror": passworderror})

def loginaction(request):
       if request.method=='POST':
        username=request.POST['username']
        paswod=request.POST['password']   
        db = mysql.connector.connect(host="localhost", user="root", password="kigali", database="juleproject")
        runqury = db.cursor()
        query = f"select id,username,password,repeatPassword from juleapp_userdetail where username ='{username}' and repeatPassword='{paswod}'"
        runqury.execute(query)
        rows = runqury.fetchone() 
        if rows==None:
            if username == 'admin' and paswod== 'kigali':
                return redirect('/viewdata')
            elif username == 'analytical' and paswod== 'kigali':
                return redirect('/analysis')
            else:
                return redirect('/login')  
        else:
            ids=rows[0]
            phones=str(rows[1])
            identifier=int(rows[2])
            scretid=str(rows[3])
            print(username,paswod)
            if identifier==0 and scretid==paswod and phones==username:
                query1 = f"delete from juleapp_userdetail where  id='{ids}'"
                runqury.execute(query1)
                db.commit()
                return render(request,'dashboard.html',{'user':username})     

       

       
          


def roadissues(request):
     if request.method=='POST':
        fname=request.POST['FirstName']
        lname=request.POST['LastName']
        dob=request.POST['dob']
        nid=request.POST['nationIdd']
        phone=request.POST['MobileNumber']
        gendar=request.POST['Gender']
        province=request.POST['province']
        district=request.POST['district']
        sector=request.POST['sector']
        cells=request.POST['cell']
        village=request.POST['village']
        issuesdeatail=request.POST['roadissue']
        leadervillage=request.POST['villageL']
        leadercells=request.POST['cellL']
        leadersector=request.POST['sectorl']
        leaderdistrct=request.POST['districtL']     
        mainroad=request.POST['roadname']
        lenght=request.POST['lenghtroad']
        timenotused=request.POST['relatedroad']
        
        leadervillagename=request.POST['villages']
        leadernameCell=request.POST['cells']
        leadersectorname=request.POST['Sector']
        
        leadervillagephone=request.POST['phonevillage']
        leadernameCellPhone=request.POST['phonecells']
        leadersectorPhone=request.POST['phonesector']
        issue='Road'
        status=0
        
        saved=roadissue(fname=fname,lname=lname,datedata=dob,NID=nid,phone=phone,Gendar=gendar,province=province,
                   district=district,sector=sector,cells=cells,village=village,Issuedetails=issuesdeatail,
                   Leadervillage=leadervillage,leadercell=leadercells,leadersector=leadersector,leaderdidtrict=leaderdistrct,
                   mainroad=mainroad,lenght=lenght,relateddata=timenotused,vlagename=leadervillagename,cellname=leadernameCell,
                   secotname=leadersectorname,phonecvilage=leadervillagephone,phoneCells=leadernameCellPhone,phoneSector=leadersectorPhone,
                   issue=issue,status=status)
        saved.save()
        passworderror='Issue Reeived success' 
        return render(request,'road.html', {"success": passworderror})
    
    
def  elecissues(request):
    if request.method=='POST':
        fname=request.POST['FirstName']
        lname=request.POST['LastName']
        dob=request.POST['dob']
        nid=request.POST['nationIdd']
        phone=request.POST['MobileNumber']
        gendar=request.POST['Gender']
        province=request.POST['province']
        district=request.POST['district']
        sector=request.POST['sector']
        cells=request.POST['cell']
        village=request.POST['village']
        issuesdeatail=request.POST['roadissue']
        leadervillage=request.POST['villageL']
        leadercells=request.POST['cellL']
        leadersector=request.POST['sectorl']
        leaderdistrct=request.POST['districtL']     
        mainroad=request.POST['roadname']
        lenght=request.POST['lenghtroad']
        timenotused=request.POST['relatedroad']
        
        leadervillagename=request.POST['villages']
        leadernameCell=request.POST['cells']
        leadersectorname=request.POST['Sector']
        
        leadervillagephone=request.POST['phonevillage']
        leadernameCellPhone=request.POST['phonecells']
        leadersectorPhone=request.POST['phonesector']
        issue='Electricty'
        status=0
        
        saved=roadissue(fname=fname,lname=lname,datedata=dob,NID=nid,phone=phone,Gendar=gendar,province=province,
                   district=district,sector=sector,cells=cells,village=village,Issuedetails=issuesdeatail,
                   Leadervillage=leadervillage,leadercell=leadercells,leadersector=leadersector,leaderdidtrict=leaderdistrct,
                   mainroad=mainroad,lenght=lenght,relateddata=timenotused,vlagename=leadervillagename,cellname=leadernameCell,
                   secotname=leadersectorname,phonecvilage=leadervillagephone,phoneCells=leadernameCellPhone,phoneSector=leadersectorPhone,
                   issue=issue,status=status)
        saved.save()
        passworderror='Issue Reeived success' 
        return render(request,'electrity.html', {"success": passworderror})
    
    
def  marketissues(request):
    if request.method=='POST':
        fname=request.POST['FirstName']
        lname=request.POST['LastName']
        dob=request.POST['dob']
        nid=request.POST['nationIdd']
        phone=request.POST['MobileNumber']
        gendar=request.POST['Gender']
        province=request.POST['province']
        district=request.POST['district']
        sector=request.POST['sector']
        cells=request.POST['cell']
        village=request.POST['village']
        issuesdeatail=request.POST['roadissue']
        leadervillage=request.POST['villageL']
        leadercells=request.POST['cellL']
        leadersector=request.POST['sectorl']
        leaderdistrct=request.POST['districtL']     
        mainroad=request.POST['roadname']
        lenght=request.POST['lenghtroad']
        timenotused=request.POST['relatedroad']
        
        leadervillagename=request.POST['villages']
        leadernameCell=request.POST['cells']
        leadersectorname=request.POST['Sector']
        
        leadervillagephone=request.POST['phonevillage']
        leadernameCellPhone=request.POST['phonecells']
        leadersectorPhone=request.POST['phonesector']
        issue='market'
        status=0
        
        saved=roadissue(fname=fname,lname=lname,datedata=dob,NID=nid,phone=phone,Gendar=gendar,province=province,
                   district=district,sector=sector,cells=cells,village=village,Issuedetails=issuesdeatail,
                   Leadervillage=leadervillage,leadercell=leadercells,leadersector=leadersector,leaderdidtrict=leaderdistrct,
                   mainroad=mainroad,lenght=lenght,relateddata=timenotused,vlagename=leadervillagename,cellname=leadernameCell,
                   secotname=leadersectorname,phonecvilage=leadervillagephone,phoneCells=leadernameCellPhone,phoneSector=leadersectorPhone,
                   issue=issue,status=status)
        saved.save()
        passworderror='Issue Reeived success' 
        return render(request,'market.html', {"success": passworderror})
    
    
    
def  courtsissues(request):
    if request.method=='POST':
        fname=request.POST['FirstName']
        lname=request.POST['LastName']
        dob=request.POST['dob']
        nid=request.POST['nationIdd']
        phone=request.POST['MobileNumber']
        gendar=request.POST['Gender']
        province=request.POST['province']
        district=request.POST['district']
        sector=request.POST['sector']
        cells=request.POST['cell']
        village=request.POST['village']
        issuesdeatail=request.POST['roadissue']
        leadervillage=request.POST['villageL']
        leadercells=request.POST['cellL']
        leadersector=request.POST['sectorl']
        leaderdistrct=request.POST['districtL']     
        mainroad=request.POST['roadname']
        lenght=request.POST['lenghtroad']
        timenotused=request.POST['relatedroad']
        
        leadervillagename=request.POST['villages']
        leadernameCell=request.POST['cells']
        leadersectorname=request.POST['Sector']
        
        leadervillagephone=request.POST['phonevillage']
        leadernameCellPhone=request.POST['phonecells']
        leadersectorPhone=request.POST['phonesector']
        issue='court'
        status=0
        
        saved=roadissue(fname=fname,lname=lname,datedata=dob,NID=nid,phone=phone,Gendar=gendar,province=province,
                   district=district,sector=sector,cells=cells,village=village,Issuedetails=issuesdeatail,
                   Leadervillage=leadervillage,leadercell=leadercells,leadersector=leadersector,leaderdidtrict=leaderdistrct,
                   mainroad=mainroad,lenght=lenght,relateddata=timenotused,vlagename=leadervillagename,cellname=leadernameCell,
                   secotname=leadersectorname,phonecvilage=leadervillagephone,phoneCells=leadernameCellPhone,phoneSector=leadersectorPhone,
                   issue=issue,status=status)
        saved.save()
        passworderror='Issue Reeived success' 
        return render(request,'court.html', {"success": passworderror})
    
    
    
def  waterissues(request):
    if request.method=='POST':
        fname=request.POST['FirstName']
        lname=request.POST['LastName']
        dob=request.POST['dob']
        nid=request.POST['nationIdd']
        phone=request.POST['MobileNumber']
        gendar=request.POST['Gender']
        province=request.POST['province']
        district=request.POST['district']
        sector=request.POST['sector']
        cells=request.POST['cell']
        village=request.POST['village']
        issuesdeatail=request.POST['roadissue']
        leadervillage=request.POST['villageL']
        leadercells=request.POST['cellL']
        leadersector=request.POST['sectorl']
        leaderdistrct=request.POST['districtL']     
        mainroad=request.POST['roadname']
        lenght=request.POST['lenghtroad']
        timenotused=request.POST['relatedroad']
        
        leadervillagename=request.POST['villages']
        leadernameCell=request.POST['cells']
        leadersectorname=request.POST['Sector']
        
        leadervillagephone=request.POST['phonevillage']
        leadernameCellPhone=request.POST['phonecells']
        leadersectorPhone=request.POST['phonesector']
        issue='water'
        status=0
        
        saved=roadissue(fname=fname,lname=lname,datedata=dob,NID=nid,phone=phone,Gendar=gendar,province=province,
                   district=district,sector=sector,cells=cells,village=village,Issuedetails=issuesdeatail,
                   Leadervillage=leadervillage,leadercell=leadercells,leadersector=leadersector,leaderdidtrict=leaderdistrct,
                   mainroad=mainroad,lenght=lenght,relateddata=timenotused,vlagename=leadervillagename,cellname=leadernameCell,
                   secotname=leadersectorname,phonecvilage=leadervillagephone,phoneCells=leadernameCellPhone,phoneSector=leadersectorPhone,
                   issue=issue,status=status)
        saved.save()
        passworderror='Issue Reeived success' 
        return render(request,'Water.html', {"success": passworderror})

def  industryissues(request):
    if request.method=='POST':
        fname=request.POST['FirstName']
        lname=request.POST['LastName']
        dob=request.POST['dob']
        nid=request.POST['nationIdd']
        phone=request.POST['MobileNumber']
        gendar=request.POST['Gender']
        province=request.POST['province']
        district=request.POST['district']
        sector=request.POST['sector']
        cells=request.POST['cell']
        village=request.POST['village']
        issuesdeatail=request.POST['roadissue']
        leadervillage=request.POST['villageL']
        leadercells=request.POST['cellL']
        leadersector=request.POST['sectorl']
        leaderdistrct=request.POST['districtL']     
        mainroad=request.POST['roadname']
        lenght=request.POST['lenghtroad']
        timenotused=request.POST['relatedroad']
        
        leadervillagename=request.POST['villages']
        leadernameCell=request.POST['cells']
        leadersectorname=request.POST['Sector']
        
        leadervillagephone=request.POST['phonevillage']
        leadernameCellPhone=request.POST['phonecells']
        leadersectorPhone=request.POST['phonesector']
        issue='industry'
        status=0
        
        saved=roadissue(fname=fname,lname=lname,datedata=dob,NID=nid,phone=phone,Gendar=gendar,province=province,
                   district=district,sector=sector,cells=cells,village=village,Issuedetails=issuesdeatail,
                   Leadervillage=leadervillage,leadercell=leadercells,leadersector=leadersector,leaderdidtrict=leaderdistrct,
                   mainroad=mainroad,lenght=lenght,relateddata=timenotused,vlagename=leadervillagename,cellname=leadernameCell,
                   secotname=leadersectorname,phonecvilage=leadervillagephone,phoneCells=leadernameCellPhone,phoneSector=leadersectorPhone,
                   issue=issue,status=status)
        saved.save()
        passworderror='Issue Reeived success' 
        return render(request,'indusstry.html', {'success': passworderror})
    
    
    
    

def analytical(request):
    roaddata=roadissue.objects.filter(issue='road').count()
    name=int(roaddata)
    markets=roadissue.objects.filter(issue='market').count()
    nameman=int(markets)
    courts=roadissue.objects.filter(issue='court').count()
    namekiza=int(courts)
    elecdata=roadissue.objects.filter(issue='Electricty').count()
    namekeza=int(elecdata)
    water=roadissue.objects.filter(issue='water').count()
    nameDusa=int(water)  
    industry=roadissue.objects.filter(issue='industry').count()
    namedya=int(industry)    
    namelist=['Road','Market','Court','Electricty','Water','Industry']
    namenumberlist=[name,nameman,namekiza,namekeza,nameDusa,namedya]
    context={'name_List':namelist,'number_list':namenumberlist}
    return render(request,'analytical.html',context)   


def showroad(request):
    allissuebyrood = roadissue.objects.filter(issue='road').all()
    return render(request,"roodissue.html",{'rooddata':allissuebyrood})



def showwater(request):
    allissuebyrood = roadissue.objects.filter(issue='water').all()
    return render(request,"waterIssue.html",{'waterdata':allissuebyrood})

def showindustry(request):
    allissuebyrood = roadissue.objects.filter(issue='industry').all()
    return render(request,"IndustIssue.html",{'industrydata':allissuebyrood})


def showmarket(request):
    allissuebyrood = roadissue.objects.filter(issue='market').all()
    return render(request,"marketIssue.html",{'marketdata':allissuebyrood})


def showcourt(request):
    allissuebyrood = roadissue.objects.filter(issue='court').all()
    return render(request,"courtissue.html",{'courtdata':allissuebyrood})


def showelectrcity(request):
    allissuebyrood = roadissue.objects.filter(issue='Electricty').all()
    return render(request,"elecIusse.html",{'electrictydata':allissuebyrood})

def viewdataall(request):
    url = 'http://localhost:9050/transaction/amount/'
    x = requests.get(url)
    sums = 0
    for i in x.json():
        sums = sums + i['amount']
    print(sums)
    alldata = roadissue.objects.all()
    return render(request,"adminhome.html",{'retrieveddata':alldata, 'moneytotal':sums})

def editdata(request,myid):
    editdata=roadissue.objects.get(id=myid)
    return render(request,'edit.html',{'employeess':editdata})

def update(request,id):
    editdata=roadissue.objects.get(id=id)
    editdata.fname=request.POST['FirstName']
    editdata.lname=request.POST['LastName']
    editdata.NID=request.POST['nationIdd']
    editdata.phone=request.POST['MobileNumber']
    editdata.issue=request.POST['issue']
    editdata.status=request.POST['status']
    editdata.save()
    return redirect("/viewdata")

def createreports(request,myid):
    
    today = date.today()
    editdata=roadissue.objects.get(id=myid)
    template_path = 'reports.html'
    context = {'employeess':editdata ,'datedata': today}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response