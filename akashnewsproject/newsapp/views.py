from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')

def moviesinfo(request):
    head_msg='Latest Movies Information'
    msg1='Sara is slowly getting cute'
    msg2='Love Aaj Kal coming on this 14th'
    msg3='Kartik Aryan Fire the Bollywood Cinema Now Days'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest Sports Information'
    msg1='Virat Kohli going to bread all the records in nexr upcoming year'
    msg2='IPL start date declared'
    msg3='India doing good in Athelatics'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg='Latest Politics Information'
    msg1='Phopnar Sarpanch election seat delclared'
    msg2='Janpat panchyat election most suitable candidate is Asha Bai Mahajan'
    msg3='people of my villege going made these days'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
