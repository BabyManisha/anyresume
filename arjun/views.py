from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.base import View
from django.template.loader import get_template
import os
from resume.settings import db1, BASE_DIR, DB_HOST, DB_NAME
from django.views.decorators.csrf import csrf_exempt
import smtplib
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    user = db1.home.find_one({'name': 'Arjun. Maari'}, {'_id': 0})
    print user
    if user is None:
        return HttpResponse("InValid")
    else:
        return render(request, 'home.html', {'user': user, 'page': "Home"})

def educationPage(request):
    education = db1.education.find({}, {'_id': 0})
    print education
    ed = []
    for i in education:
        ed.append(i)
    return HttpResponse(json.dumps(ed))

def experiencePage(request):
    experience = db1.experience.find({}, {'_id': 0})
    print experience
    ex = []
    for i in experience:
        ex.append(i)
    return HttpResponse(json.dumps(ex))

def aboutPage(request):
    about = db1.about.find({}, {'_id': 0})
    print about
    ab = []
    for i in about:
        ab.append(i)
    return HttpResponse(json.dumps(ab))

def contactPage(request):
    user = db1.home.find_one({'name': 'Arjun. Maari'}, {'_id': 0})
    print user
    return render(request, 'home.html', {'user': user, 'page': "Contact", 'msg' : "Mail Sent Successfully!!"})


@csrf_exempt
def contactMessage(request):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    message = request.POST.get('message')

    cnmessage = {"firstName": firstName, 
                "lastName": lastName, 
                "email": email, 
                "mobile": mobile, 
                "message": message}
    dbr = db1.contact.insert(cnmessage)
    if dbr:
        to = email
        gmail_user = 'techcontest2015@gmail.com'
        gmail_pwd = 'Aviso@2017'
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Contact Successfull \n'
        msg = header + '\nHi ' + firstName +', Thank you for Your Message. I will contact you soon. \n'
        smtpserver.sendmail(gmail_user, to, msg)
        smtpserver.close()
        print "mailllllllll sucesssfully sent...."
        return HttpResponseRedirect('contactPage')
    else:
        '''return HttpResponse("ERROR: Sorry Please Register Again")'''
        return render(request, 'errorpage.html', {'emessage': "Sorry Something went wrong.. Please Contact Again"})
