from django.shortcuts import render,redirect
from  django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
import requests

#Making JSON encoder
from json import JSONEncoder
import json
class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

def contact_view(request):
    return render(request, 'firstapp/contact.html', {})

def faq_view(request):
    return render(request, 'firstapp/faq.html', {})

def home_view(request,*args,**kwargs):
    return render(request,'firstapp/home.html',{})

def about_view(request,*args,**kwargs):
    return render(request, 'firstapp/about.html', {})

def register_user(request):
    print("inside register_user")
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    new_user = User_Base(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
    new_user.save()
    return render(request,'firstapp/tmp.html',{})

def login_user(request):
    print('Inside login user')
    username = request.POST.get('username')
    password = request.POST.get('password')
    if(username!=None and password!=None):
        request.session['username']=username
        request.session['password']=password
        request.session['data']  = None
    else:
        username = request.session['username']
        password = request.session['password']
    test = User_Base.objects.filter(username=username).filter(password=password)
    print("type= ",type(test))
    print(len(test))
    if(test):
        context = {
            'user' : test[0],
            'data' : request.session['data'],
        }
        print('Valid User')
        test2 = test[0]
        print(type(test2))
        #if(request.session['data'] != None):
         #   context['data'] = request.session['data']
        return render(request, 'firstapp/tmp.html',context)
    else:
        print('Invalid User')
        return HttpResponseRedirect(reverse('firstapp:home'))


def login_hospital(request):
    print('Inside Hospital Login')
    username = request.POST.get('username')
    password = request.POST.get('password')
    if(username!=None and password!=None):
        request.session['username']=username
        request.session['password']=password
    else:
        username = request.session['username']
        password = request.session['password']
    test = Hospital_Base.objects.filter(username=username).filter(password=password)
    ward = Hospital_Wards.objects.filter(username=username)
    opd = Hospital_OPD.objects.filter(username=username)
    print("type ",type(test))
    print(len(test))
    if(test):
        print('Valid Hospital')
        test2=test[0]
        print(type(test2))
        context = {
            'hospital' : test2,
            'ward' : ward[0],
            'opd' : opd[0],
        }
        return render(request, 'firstapp/login_hospital.html',context)
    else:
        print('Invalid User')
       # return home_view(request)
        return HttpResponseRedirect(reverse('firstapp:home'))

def register_hospital(request):
    print("Inside Hospital Register")
    username = request.POST.get('username')
    password = request.POST.get('password')
    hospital_name = request.POST.get('name_of_hospital')
    phone = request.POST.get('phone')
    website = request.POST.get('website')
    new_hospital = Hospital_Base(username=username,password=password,phone=phone,website=website,hospital_name=hospital_name)
    new_ward = Hospital_Wards(username=username,emer_w=0,cardio_w=0,neuro_w=0,ortho_w=0,gen_w=0)
    time = '00:00'
    new_opd = Hospital_OPD(username=username,cardio_t1=time,cardio_t2=time,neuro_t1=time,neuro_t2=time,ortho_t1=time,ortho_t2=time,dent_t1=time,dent_t2=time,gen_t1=time,gen_t2=time)
    new_ward.save()
    new_opd.save()
    new_hospital.save()
    return HttpResponseRedirect(reverse('firstapp:home'))

def update_hospital(request):
    emer_w = request.POST.get('emer')
    cardio_w = request.POST.get('cardio')
    neuro_w = request.POST.get('neuro')
    ortho_w = request.POST.get('ortho')
    gen_w = request.POST.get('gen')
    username = request.session['username']
    password = request.session['password']
    test = Hospital_Wards.objects.filter(username=username)
    if(len(test)==0):
        up_hospital_ward = Hospital_Wards(username=username,emer_w=emer_w,cardio_w=cardio_w,neuro_w=neuro_w,ortho_w=ortho_w,gen_w=gen_w)
        up_hospital_ward.save()
    else:
        test2 = test[0]
        test2.emer_w = emer_w
        test2.cardio_w = cardio_w
        test2.neuro_w = neuro_w
        test2.ortho_w = ortho_w
        test2.gen_w = gen_w
        test2.save()
    return HttpResponseRedirect(reverse('firstapp:hospital'))

def ward_hospital(request):
    print('ward_hospital')
    username = request.session['username']
    password = request.session['password']
    print('username=',username)
    print('password=',password)
    emer_w = request.POST.get('emergency')
    cardio_w = request.POST.get('cardio')
    neuro_w = request.POST.get('neuro')
    ortho_w = request.POST.get('ortho')
    gen_w = request.POST.get('general')
    test = Hospital_Wards.objects.filter(username=username)
    if(len(test)==0):
        up_hospital_ward = Hospital_Wards(emer_w=emer_w,cardio_w=cardio_w,neuro_w=neuro_w,ortho_w=ortho_w,gen_w=gen_w,username=username)
        up_hospital_ward.save()
    else:
        test2 = test[0]
        test2.emer_w = emer_w
        test2.cardio_w = cardio_w
        test2.neuro_w = neuro_w
        test2.ortho_w = ortho_w
        test2.gen_w = gen_w
        test2.save()
    return HttpResponseRedirect(reverse('firstapp:hospital'))

def opd_hospital(request):
    print('OPD Hospital')
    username = request.session['username']
    password = request.session['password']
    cardio_t1 = request.POST.get('cardio1')
    cardio_t2 = request.POST.get('cardio2')
    neuro_t1 = request.POST.get('neuro1')
    neuro_t2 = request.POST.get('neuro2')
    ortho_t1 = request.POST.get('ortho1')
    ortho_t2 = request.POST.get('ortho2')
    dent_t1 = request.POST.get('dent1')
    dent_t2 = request.POST.get('dent2')
    gen_t1 = request.POST.get('gen1')
    gen_t2 = request.POST.get('gen2')
    test = Hospital_OPD.objects.filter(username=username)
    if(len(test)==0):
        up_hospital_opd = Hospital_OPD(username=username,cardio_t1=cardio_t1,cardio_t2=cardio_t2,neuro_t1=neuro_t1,neuro_t2=neuro_t2,ortho_t1=ortho_t1,ortho_t2=ortho_t2,dent_t1=dent_t1,dent_t2=dent_t2,gen_t1=gen_t1,gen_t2=gen_t2)
        up_hospital_opd.save()
    else:
        test2 = test[0]
        test2.cardio_t1 = cardio_t1
        test2.cardio_t2 = cardio_t2
        test2.neuro_t1 = neuro_t1
        test2.neuro_t2 = neuro_t2
        test2.ortho_t1 = ortho_t1
        test2.ortho_t2 = ortho_t2
        test2.dent_t1 = dent_t1
        test2.dent_t2 = dent_t2
        test2.gen_t1 = gen_t1
        test2.gen_t2 = gen_t2
        test2.save()
    return HttpResponseRedirect(reverse('firstapp:hospital'))

def logout(request):
    request.session['username'] = None
    request.session['password'] = None
    request.session['data']  = None
    request.session.flush()
    return HttpResponseRedirect(reverse('firstapp:home'))

def hospital_location(request):
    username = request.session['username']
    coord = request.POST.get('loc')
    print('coord=',coord)
    test = str(coord).split(',')
    print('test_loc=',test)
    hospital = Hospital_Location.objects.filter(username=username)
    if(len(hospital)==0):
        obj = Hospital_Location(username=username,hospital_lat=test[0],hospital_lon=test[1])
        obj.save()
    else:
        obj = hospital[0]
        obj.hospital_lat = test[0]
        obj.hospital_lon = test[1]
        obj.save()
    return HttpResponseRedirect(reverse('firstapp:hospital'))


def main_view(request):
    type_w = request.POST.get('type_w')
    location = request.POST.get('location')
    print(type_w)
    print(location)
    url2 = '&mode=fastest;car;traffic:disabled'
    url = 'https://route.api.here.com/routing/7.2/calculateroute.json?app_id=9Ab1yIULBo3Lj9plEA8t&app_code=JhmMlH2uPy4UEH5ShcXnMQ&waypoint0=geo!'+location+'&waypoint1=geo!'
    hospitals = []
    if(type_w == 'Emergency'):
        hospitals = Hospital_Wards.objects.exclude(emer_w=0)
    elif(type_w == 'Cardiology'):
        hospitals = Hospital_Wards.objects.exclude(cardio_w=0)
    elif(type_w == 'Neurology'):
        hospitals = Hospital_Wards.objects.exclude(neuro_w=0)
    elif(type_w == 'Orthopaedic'):
        hospitals = Hospital_Wards.objects.exclude(ortho_w=0)
    else:
        hospitals = Hospital_Wards.objects.exclude(gen_w=0)

    final_list = list()
    new_ob = None
    for obj in hospitals:
        if(type_w == 'Emergency'):
            new_ob = Results(username_user=request.session['username'],username_hospital=obj.username,beds=obj.emer_w,)
         #   final_list.append(new_ob)
         #   print('new_ob=',new_ob.__dict__)
         #   print('new_list=',final_list)
        elif(type_w == 'Cardiology'):
            new_ob = Results(username_user=request.session['username'],username_hospital=obj.username,beds=obj.cardio_w,)
           # final_list.append(new_ob)
        elif(type_w == 'Neurology'):
            new_ob = Results(username_user=request.session['username'],username_hospital=obj.username,beds=obj.neuro_w,)
            #final_list.append(new_ob)
        elif(type_w == 'Orthopaedic'):
            new_ob = Results(username_user=request.session['username'],username_hospital=obj.username,beds=obj.ortho_w,)
            #final_list.append(new_ob)
        else:
            new_ob = Results(username_user=request.session['username'],username_hospital=obj.username,beds=obj.gen_w,)
            #final_list.append(new_ob)
        final_list.append(new_ob)
        #print('new_ob=',new_ob.__dict__)
        print('list=', final_list)
        print('len=',len(final_list))

        loc = Hospital_Location.objects.filter(username=final_list[-1].username_hospital)
        final_list[-1].location = loc[0].hospital_lat+','+loc[0].hospital_lon
        hname = Hospital_Base.objects.filter(username=final_list[-1].username_hospital)
        final_list[-1].name = hname[0].hospital_name
        final_list[-1].website = hname[0].website

        timing = Hospital_OPD.objects.filter(username=final_list[-1].username_hospital)
        if(type_w == 'Emergency'):
            final_list[-1].opd1 = timing[0].dent_t1
            final_list[-1].opd2 = timing[0].dent_t2
        elif(type_w == 'Cardiology'):
            final_list[-1].opd1 = timing[0].cardio_t1
            final_list[-1].opd2 = timing[0].cardio_t2
        elif(type_w == 'Orthopaedic'):
            final_list[-1].opd1 = timing[0].ortho_t1
            final_list[-1].opd2 = timing[0].ortho_t2
        elif(type_w == 'Neurology'):
            final_list[-1].opd1 = timing[0].neuro_t1
            final_list[-1].opd2 = timing[0].neuro_t2
        else:
            final_list[-1].opd1 = timing[0].gen_t1
            final_list[-1].opd2 = timing[0].gen_t2
        #Calculation of Distance and Time
        h_loc = final_list[-1].location
        new_url = url+h_loc+url2
        response = requests.get(new_url)
        data = response.json()
        dis = data['response']['route'][0]['summary']['distance']
        dur = data['response']['route'][0]['summary']['baseTime']
        print('dis = ',dis)
        print('dur = ',dur)
        final_list[-1].distance = (float) (dis/1000.0)
        final_list[-1].time = (float) (dur/3600.0)
    final_list.sort(key=lambda x: x.distance, reverse=False)
    for i in range(len(final_list)):
        final_list[i] = json.dumps(final_list[i],cls=MyEncoder)
    for i in range(len(final_list)):
        final_list[i] = json.loads(final_list[i])
    request.session['data']= final_list
    #for i in final_list:
     #   print(i.__dict__)
   # print('final_list=',final_list)
    return HttpResponseRedirect(reverse('firstapp:user'))



