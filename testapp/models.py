from django.db import models

# For Student Details Table

class Student(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    dept = models.CharField(max_length=40)
    year = models.IntegerField()
    dob = models.CharField(max_length=20)
    fathername = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    bloodgrp = models.CharField(max_length=10)


# Cse syllabus information 

class CseSyllabus(models.Model):
    subcode = models.CharField(max_length=15,primary_key=True)
    subname = models.CharField(max_length=50)
    semester = models.IntegerField()


# Cse Semester Marks for All semesters

class CseSemester1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8151 = models.FloatField()
    MA8151 = models.FloatField()
    PH8151 = models.FloatField()
    CY8151 = models.FloatField()
    GE8151 = models.FloatField()
    GE8152 = models.FloatField()

class CseSemester2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8251 = models.FloatField()
    MA8251 = models.FloatField()
    PH8252 = models.FloatField()
    BE8255 = models.FloatField()
    GE8291 = models.FloatField()
    CS8251 = models.FloatField()

class CseSemester3(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8351 = models.FloatField()
    CS8351 = models.FloatField()
    CS8391  = models.FloatField()
    CS8392 = models.FloatField()
    EC8395 = models.FloatField()


class CseSemester4(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8402 = models.FloatField()
    CS8491 = models.FloatField()
    CS8492 = models.FloatField()
    CS8451 = models.FloatField()
    CS8493 = models.FloatField()
    CS8494 = models.FloatField()

class CseSemester5(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8551 = models.FloatField()
    CS8591 = models.FloatField()
    EC8691 = models.FloatField()
    CS8501 = models.FloatField()
    CS8592 = models.FloatField()
    

class CseSemester6(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    CS8651 = models.FloatField()
    CS8691= models.FloatField()
    CS8601 = models.FloatField()
    CS8602 = models.FloatField()
    CS8603 = models.FloatField()
    GE8075 = models.FloatField()


class CseSemester7(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MG8591 = models.FloatField()
    CS8792= models.FloatField()
    CS8791 = models.FloatField()
    CS8092 = models.FloatField()
    CS8091 = models.FloatField()
    GE8077 = models.FloatField()
    GE8071 = models.FloatField()


class CseSemester8(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    GE8076 = models.FloatField()
    CS8080 = models.FloatField()

# Semester 1 internal marks 

class Semester1Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8151 = models.FloatField()
    MA8151 = models.FloatField()
    PH8151 = models.FloatField()
    CY8151 = models.FloatField()
    GE8151 = models.FloatField()
    GE8152 = models.FloatField()

class Semester1Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8151 = models.FloatField()
    MA8151 = models.FloatField()
    PH8151 = models.FloatField()
    CY8151 = models.FloatField()
    GE8151 = models.FloatField()
    GE8152 = models.FloatField()

class Semester1Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8151 = models.FloatField()
    MA8151 = models.FloatField()
    PH8151 = models.FloatField()
    CY8151 = models.FloatField()
    GE8151 = models.FloatField()
    GE8152 = models.FloatField()


# Semester 2 internal marks 


class Semester2Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8251 = models.FloatField()
    MA8251 = models.FloatField()
    PH8252 = models.FloatField()
    BE8255 = models.FloatField()
    GE8291 = models.FloatField()
    CS8251 = models.FloatField()

class Semester2Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8251 = models.FloatField()
    MA8251 = models.FloatField()
    PH8252 = models.FloatField()
    BE8255 = models.FloatField()
    GE8291 = models.FloatField()
    CS8251 = models.FloatField()

class Semester2Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    HS8251 = models.FloatField()
    MA8251 = models.FloatField()
    PH8252 = models.FloatField()
    BE8255 = models.FloatField()
    GE8291 = models.FloatField()
    CS8251 = models.FloatField()


# Semester 3 internal marks 

class Semester3Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8351 = models.FloatField()
    CS8351 = models.FloatField()
    CS8391  = models.FloatField()
    CS8392 = models.FloatField()
    EC8395 = models.FloatField()


class Semester3Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8351 = models.FloatField()
    CS8351 = models.FloatField()
    CS8391  = models.FloatField()
    CS8392 = models.FloatField()
    EC8395 = models.FloatField()

class Semester3Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8351 = models.FloatField()
    CS8351 = models.FloatField()
    CS8391  = models.FloatField()
    CS8392 = models.FloatField()
    EC8395 = models.FloatField()


# Semester 4 internal marks 

class Semester4Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8402 = models.FloatField()
    CS8491 = models.FloatField()
    CS8492 = models.FloatField()
    CS8451 = models.FloatField()
    CS8493 = models.FloatField()
    CS8494 = models.FloatField()

class Semester4Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8402 = models.FloatField()
    CS8491 = models.FloatField()
    CS8492 = models.FloatField()
    CS8451 = models.FloatField()
    CS8493 = models.FloatField()
    CS8494 = models.FloatField()

class Semester4Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8402 = models.FloatField()
    CS8491 = models.FloatField()
    CS8492 = models.FloatField()
    CS8451 = models.FloatField()
    CS8493 = models.FloatField()
    CS8494 = models.FloatField()


# Semester 5 internal marks 

class Semester5Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8551 = models.FloatField()
    CS8591 = models.FloatField()
    EC8691 = models.FloatField()
    CS8501 = models.FloatField()
    CS8592 = models.FloatField()

class Semester5Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8551 = models.FloatField()
    CS8591 = models.FloatField()
    EC8691 = models.FloatField()
    CS8501 = models.FloatField()
    CS8592 = models.FloatField()

class Semester5Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MA8551 = models.FloatField()
    CS8591 = models.FloatField()
    EC8691 = models.FloatField()
    CS8501 = models.FloatField()
    CS8592 = models.FloatField()

# Semester 6 internal marks 

class Semester6Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    CS8651 = models.FloatField()
    CS8691= models.FloatField()
    CS8601 = models.FloatField()
    CS8602 = models.FloatField()
    CS8603 = models.FloatField()
    GE8075 = models.FloatField()


class Semester6Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    CS8651 = models.FloatField()
    CS8691= models.FloatField()
    CS8601 = models.FloatField()
    CS8602 = models.FloatField()
    CS8603 = models.FloatField()
    GE8075 = models.FloatField()

class Semester6Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    CS8651 = models.FloatField()
    CS8691= models.FloatField()
    CS8601 = models.FloatField()
    CS8602 = models.FloatField()
    CS8603 = models.FloatField()
    GE8075 = models.FloatField()


# Semester 7 internal marks 

class Semester7Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MG8591 = models.FloatField()
    CS8792= models.FloatField()
    CS8791 = models.FloatField()
    CS8092 = models.FloatField()
    CS8091 = models.FloatField()
    GE8077 = models.FloatField()
    GE8071 = models.FloatField()

class Semester7Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MG8591 = models.FloatField()
    CS8792= models.FloatField()
    CS8791 = models.FloatField()
    CS8092 = models.FloatField()
    CS8091 = models.FloatField()
    GE8077 = models.FloatField()
    GE8071 = models.FloatField()

class Semester7Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    MG8591 = models.FloatField()
    CS8792= models.FloatField()
    CS8791 = models.FloatField()
    CS8092 = models.FloatField()
    CS8091 = models.FloatField()
    GE8077 = models.FloatField()
    GE8071 = models.FloatField()


# Semester 8 internal marks 

class Semester8Internal1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    GE8076 = models.FloatField()
    CS8080 = models.FloatField()

class Semester8Internal2(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    GE8076 = models.FloatField()
    CS8080 = models.FloatField()

class Semester8Model1(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    GE8076 = models.FloatField()
    CS8080 = models.FloatField()

# For Cse Study materials

class CseStudyMaterial(models.Model):
    semester = models.IntegerField(primary_key=True)
    link = models.CharField(max_length=100)

