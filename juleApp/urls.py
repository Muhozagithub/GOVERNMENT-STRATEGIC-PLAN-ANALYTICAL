from django.urls import path
from . import views

app_name = "juleApp"

urlpatterns = [
        path('',views.homeApp),
        path('signup',views.signup),
        path('login',views.login),
        path('createAccountaction',views.createaccount),
        path('logintosystem',views.loginaction),
        path('admindata',views.adminhome),
        path('analysis',views.analytical), 
        path('dashboard',views.dashboalhome),
        path('road',views.roadhome),
        path('elec',views.elechome),
        path('markets',views.markethome),
        path('waterhome',views.woterhome),
        path('courthome',views.courthome),
        path('industrydata',views.insdustryhome),
        path('roadissue',views.roadissues),
        path('electricity',views.elecissues),
        path('market',views.marketissues),
        path('court',views.courtsissues),
        path('water',views.waterissues),
        path('industry',views.industryissues),
        path('roaddata',views.showroad),
        path('waterdata',views.showwater),
        path('industriesdata',views.showindustry),
        path('marketdata',views.showmarket),
        path('courtdata',views.showcourt),
        path('electrcitydata',views.showelectrcity),
        path('viewdata',views.viewdataall),
        #path('report/<int:id>',views.editdata,name='edit'),
        path('report/<int:myid>',views.createreports),
        path('edit/<int:myid>',views.editdata,name='edit'),
        path('edit/update/<int:id>',views.update,name='update')
        
      
]