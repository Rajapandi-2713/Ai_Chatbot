from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from re import * 


def home(request):
    return render(request,'index.html')

@csrf_exempt
def getResponse(request):


    # To get the input from user 

    result = (request.POST['data']).lower()
    data = request.POST['text']


    # To Match the input and return response 


    # match with semester 

    if fullmatch('[0-9]', result):

        return HttpResponse(semester_marks(int(data),int(result)))

    
    # match with register number 

    elif fullmatch('9210[0-9]*', result):

        if fullmatch('[a-z\s]*stu[a-z\s]*info[a-z\s]*', data.lower()):

            return HttpResponse(getInfo(int(result)))

        elif fullmatch('[a-z\s]*sem[a-z\s]*mark[a-z\s]*', data.lower()):

            text = 'Enter the semester :'
            return HttpResponse(text)

        elif (fullmatch('[a-z\s]*internal[a-z\s]*mark[a-z\s]*', data.lower()) or fullmatch('[a-z\s]*model[a-z\s]*mark[a-z\s]*', data.lower())):

            return HttpResponse(internalMarks(int(result)))


    # match with input query 

    elif fullmatch('[a-z\s]*stu[a-z\s]*info[a-z\s]*', result) or fullmatch('[a-z\s]*sem[a-z\s]*mark[a-z\s]*', result) or (fullmatch('[a-z\s]*internal[a-z\s]*mark[a-z\s]*', result) or fullmatch('[a-z\s]*model[a-z\s]*mark[a-z\s]*', result)):

        text = 'Enter Your Register Number'
        return HttpResponse(text)

    elif fullmatch('[a-z\s]*cse\s*study\s*material[a-z]*',result) or fullmatch('[a-z\s]*study\s*material[a-z\s]*cse[a-z/s]*',result) or fullmatch('[a-z\s]*study\s*material[a-z\s]*',result) :
        
        return HttpResponse(getMaterial())

    # For undefined behaviour

    else:
        return HttpResponse("No Record Found")
        

# To get student information

def getInfo(regno):

    try:
        obj = Student.objects.get(rollnumber=regno)

    except ObjectDoesNotExist:

        return "No record found or invalid register number ! "

    else:
        if obj:
            string = ""
            string += "Roll Number : "+str(obj.rollnumber)+"<br>"
            string += "Name : "+str(obj.name )+"<br>"
            string += "Department : "+str(obj.dept )+"<br>"
            string += "Year : "+str(obj.year)+"<br>"
            string += "DOB : "+str(obj.dob )+"<br>"
            string += "Fathername : "+str(obj.fathername)+"<br>"
            string += "Address : "+str(obj.address)+"<br>"
            string += "Phone : "+str(obj.phone)+"<br>"
            string += "Email : "+str(obj.email )+"<br>"
            string += "Blood Group : "+str(obj.bloodgrp)
            return string


# To get study materials 
      
def getMaterial():
    string = "CSE MATERIALS :<br>"

    for x in range(1,9):
        obj = CseStudyMaterial.objects.get(semester=x)
        temp = "<a href = {} target={} > Semester {} </a>".format(obj.link,"_blank",x)
        string+= temp + "<br>"

    return string


# To get semester marks 

def semester_marks(rollno,sem):

    string = ""

    if sem == 1 :

        try:
            obj = CseSemester1.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found ! "

        else:
            string += "SEMESTER 1 :<br>"
            string += "HS8151 :"+ str(obj.HS8151) + "<br>"
            string += "MA8151 :"+ str(obj.MA8151) + "<br>"
            string += "PH8151 :"+ str(obj.PH8151) + "<br>"
            string += "CY8151:"+ str(obj.CY8151) + "<br>"
            string += "GE8151 :"+ str(obj.GE8151) + "<br>"
            string += "GE8152 :"+ str(obj.GE8152)

            return string

    elif sem == 2 :

        try:
            obj = CseSemester2.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found for the given semester! "

        else:
            string += "SEMESTER 2 :<br>"
            string += "HS8251 :"+ str(obj.HS8251) + "<br>"
            string += "MA8251 :"+ str(obj.MA8251) + "<br>"
            string += "PH8252 :"+ str(obj.PH8252) + "<br>"
            string += "BE8255:"+ str(obj.BE8255) + "<br>"
            string += "GE8291 :"+ str(obj.GE8291) + "<br>"
            string += "CS8251 :"+ str(obj.CS8251)

            return string

    elif sem == 3 :

        try:
            obj = CseSemester3.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found for the given semester! "

        else:
            string += "SEMESTER 3 :<br>"
            string += "MA8351 :"+ str(obj.MA8351) + "<br>"
            string += "CS8351 :"+ str(obj.CS8351) + "<br>"
            string += "CS8391 :"+ str(obj.CS8391) + "<br>"
            string += "CS8392:"+ str(obj.CS8392) + "<br>"
            string += "EC8395 :"+ str(obj.EC8395)

            return string

    elif sem == 4 :

        try:
            obj = CseSemester4.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found for the given semester! "

        else:
            string += "SEMESTER 4 :<br>"
            string += "MA8402 :"+ str(obj.MA8402) + "<br>"
            string += "CS8491  :"+ str(obj.CS8491 ) + "<br>"
            string += "CS8492 :"+ str(obj.CS8492) + "<br>"
            string += "CS8451:"+ str(obj.CS8451) + "<br>"
            string += "CS8493 :"+ str(obj.CS8493) + "<br>"
            string += "CS8494 :"+ str(obj.CS8494)

            return string

    elif sem == 5 :

        try:
            obj = CseSemester5.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found for the given semester! "

        else:
            string += "SEMESTER 5 :<br>"
            string += "MA8551 :"+ str(obj.MA8551) + "<br>"
            string += "CS8591 :"+ str(obj.CS8591) + "<br>"
            string += "EC8691 :"+ str(obj.EC8691) + "<br>"
            string += "CS8501:"+ str(obj.CS8501) + "<br>"
            string += "CS8592 :"+ str(obj.CS8592)

            return string

    elif sem == 6 :

        try:
            obj = CseSemester6.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found for the given semester! "

        else:
            string += "SEMESTER 6 :<br>"
            string += "CS8651 :"+ str(obj.CS8651) + "<br>"
            string += "CS8691 :"+ str(obj.CS8691) + "<br>"
            string += "CS8601 :"+ str(obj.CS8601) + "<br>"
            string += "CS8602 :"+ str(obj.CS8602) + "<br>"
            string += "CS8603 :"+ str(obj.CS8603) + "<br>"
            string += "GE8075 :"+ str(obj.GE8075)

            return string

    elif sem == 7 :

        try:
            obj = CseSemester7.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found for the given semester! "

        else:
            string += "SEMESTER 7 :<br>"
            string += "MG8591 :"+ str(obj.MG8591) + "<br>"
            string += "CS8792 :"+ str(obj.CS8792) + "<br>"
            string += "CS8791 :"+ str(obj.CS8791) + "<br>"
            string += "CS8092:"+ str(obj.CS8092) + "<br>"
            string += "CS8091 :"+ str(obj.CS8091) + "<br>"
            string += "GE8077 :"+ str(obj.GE8077) + "<br>"
            string += "GE8071 :"+ str(obj.GE8071)

            return string

    elif sem == 8 :

        try:
            obj = CseSemester8.objects.get(rollnumber = rollno)

        except ObjectDoesNotExist:

            return "No record found for the given semester! "

        else:
            string += "SEMESTER 1 :<br>"
            string += "GE8076 :"+ str(obj.GE8076) + "<br>"
            string += "CS8080 :"+ str(obj.CS8080)

            return string

    else:
        return "No record found for the given semester! "


# To get internal marks 

def internalMarks(rollno):

    string = ""

    try:
        obj = Semester6Internal1.objects.get(rollnumber = rollno)

    except ObjectDoesNotExist:

        return "No record found or invalid register number ! "

    else:
        string += "Internal 1 :<br><br>"
        string += "CS8651 :"+ str(obj.CS8651) + "<br>"
        string += "CS8691 :"+ str(obj.CS8691) + "<br>"
        string += "CS8601 :"+ str(obj.CS8601) + "<br>"
        string += "CS8602 :"+ str(obj.CS8602) + "<br>"
        string += "CS8603 :"+ str(obj.CS8603) + "<br>"
        string += "GE8075 :"+ str(obj.GE8075)+ "<br><br>"


    try:
        obj = Semester6Internal2.objects.get(rollnumber = rollno)

    except ObjectDoesNotExist:

        string += "Internal 2 :<br> Record not found"

        return string

    else:
        string += "Internal 2 :<br><br>"
        string += "CS8651 :"+ str(obj.CS8651) + "<br>"
        string += "CS8691 :"+ str(obj.CS8691) + "<br>"
        string += "CS8601 :"+ str(obj.CS8601) + "<br>"
        string += "CS8602 :"+ str(obj.CS8602) + "<br>"
        string += "CS8603 :"+ str(obj.CS8603) + "<br>"
        string += "GE8075 :"+ str(obj.GE8075)+ "<br><br>"


    try:
        obj = Semester6Model1.objects.get(rollnumber = rollno)

    except ObjectDoesNotExist:
        
        string += "Model 1 :<br><br> Record not found"

        return string

    else:
        string += "Model 1 :<br>"
        string += "CS8651 :"+ str(obj.CS8651) + "<br>"
        string += "CS8691 :"+ str(obj.CS8691) + "<br>"
        string += "CS8601 :"+ str(obj.CS8601) + "<br>"
        string += "CS8602 :"+ str(obj.CS8602) + "<br>"
        string += "CS8603 :"+ str(obj.CS8603) + "<br>"
        string += "GE8075 :"+ str(obj.GE8075)

    return string

