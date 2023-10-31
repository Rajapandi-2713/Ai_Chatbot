from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from testapp.models import *
from .resources import *

# For Student Details 
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    resource_class = StudentResource
    list_display=['rollnumber','name','dept','year'] 

# Cse syllabus information 
class CseSyllabusAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    resource_class = CseSyllabusResource
    list_display=['semester','subcode','subname'] 


# Cse Semester Marks for All semesters

class CseSemester1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester1Resource
    list_display=['rollnumber','HS8151','MA8151','PH8151','CY8151','GE8151','GE8152']

class CseSemester2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester2Resource
    list_display=['rollnumber','HS8251','MA8251','PH8252','BE8255','GE8291','CS8251']

class CseSemester3Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester3Resource
    list_display = ['rollnumber','MA8351','CS8351','CS8391','CS8392','EC8395']

class CseSemester4Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester4Resource
    list_display=['rollnumber','MA8402','CS8491','CS8492','CS8451','CS8493','CS8494']

class CseSemester5Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester5Resource
    list_display =['rollnumber','MA8551','CS8591','EC8691','CS8501','CS8592']

class CseSemester6Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester6Resource
    list_display=['rollnumber','CS8651','CS8691','CS8601','CS8602','CS8603','GE8075']

class CseSemester7Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester7Resource
    list_display=['rollnumber','MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071']

class CseSemester8Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseSemester8Resource
    list_display=['rollnumber','GE8076','CS8080']


# Semester 1 internal marks

class Semester1Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester1Internal1Resource
    list_display=['rollnumber','HS8151','MA8151','PH8151','CY8151','GE8151','GE8152']

class Semester1Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester1Internal2Resource
    list_display=['rollnumber','HS8151','MA8151','PH8151','CY8151','GE8151','GE8152']

class Semester1Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester1Model1Resource
    list_display=['rollnumber','HS8151','MA8151','PH8151','CY8151','GE8151','GE8152']

# Semester 2 internal marks

class Semester2Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester2Internal1Resource
    list_display=['rollnumber','HS8251','MA8251','PH8252','BE8255','GE8291','CS8251']

class Semester2Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester2Internal2Resource
    list_display=['rollnumber','HS8251','MA8251','PH8252','BE8255','GE8291','CS8251']

class Semester2Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester2Model1Resource
    list_display=['rollnumber','HS8251','MA8251','PH8252','BE8255','GE8291','CS8251']

# Semester 3 internal marks

class Semester3Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester3Internal1Resource
    list_display = ['rollnumber','MA8351','CS8351','CS8391','CS8392','EC8395']

class Semester3Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester3Internal2Resource
    list_display = ['rollnumber','MA8351','CS8351','CS8391','CS8392','EC8395']

class Semester3Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester3Model1Resource
    list_display = ['rollnumber','MA8351','CS8351','CS8391','CS8392','EC8395']

# Semester 4 internal marks

class Semester4Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester4Internal1Resource
    list_display=['rollnumber','MA8402','CS8491','CS8492','CS8451','CS8493','CS8494']

class Semester4Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester4Internal2Resource
    list_display=['rollnumber','MA8402','CS8491','CS8492','CS8451','CS8493','CS8494']

class Semester4Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester4Model1Resource
    list_display=['rollnumber','MA8402','CS8491','CS8492','CS8451','CS8493','CS8494']

# Semester 5 internal marks

class Semester5Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester5Internal1Resource
    list_display =['rollnumber','MA8551','CS8591','EC8691','CS8501','CS8592']

class Semester5Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester5Internal2Resource
    list_display =['rollnumber','MA8551','CS8591','EC8691','CS8501','CS8592']

class Semester5Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester5Model1Resource
    list_display =['rollnumber','MA8551','CS8591','EC8691','CS8501','CS8592']

# Semester 6 internal marks

class Semester6Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester6Internal1Resource
    list_display=['rollnumber','CS8651','CS8691','CS8601','CS8602','CS8603','GE8075']

class Semester6Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester6Internal2Resource
    list_display=['rollnumber','CS8651','CS8691','CS8601','CS8602','CS8603','GE8075']

class Semester6Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester6Model1Resource
    list_display=['rollnumber','CS8651','CS8691','CS8601','CS8602','CS8603','GE8075']


# Semester 7 internal marks

class Semester7Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester7Internal1Resource
    list_display=['rollnumber','MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071']

class Semester7Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester7Internal2Resource
    list_display=['rollnumber','MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071']

class Semester7Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester7Model1Resource
    list_display=['rollnumber','MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071']


# Semester 8 internal marks

class Semester8Internal1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester8Internal1Resource
    list_display=['rollnumber','GE8076','CS8080']

class Semester8Internal2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester8Internal2Resource
    list_display=['rollnumber','GE8076','CS8080']

class Semester8Model1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Semester8Model1Resource
    list_display=['rollnumber','GE8076','CS8080']


# Cse Study material

class CseStudyMaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CseStudyMaterialResource
    list_display=['semester','link']


# Register to admin panel 

admin.site.register(Student,StudentAdmin)
admin.site.register(CseSyllabus,CseSyllabusAdmin)

admin.site.register(CseSemester1,CseSemester1Admin)
admin.site.register(CseSemester2,CseSemester2Admin)
admin.site.register(CseSemester3,CseSemester3Admin)
admin.site.register(CseSemester4,CseSemester4Admin)
admin.site.register(CseSemester5,CseSemester5Admin)
admin.site.register(CseSemester6,CseSemester6Admin)
admin.site.register(CseSemester7,CseSemester7Admin)
admin.site.register(CseSemester8,CseSemester8Admin)

admin.site.register(Semester1Internal1,Semester1Internal1Admin)
admin.site.register(Semester1Internal2,Semester1Internal2Admin)
admin.site.register(Semester1Model1,Semester1Model1Admin)

admin.site.register(Semester2Internal1,Semester2Internal1Admin)
admin.site.register(Semester2Internal2,Semester2Internal2Admin)
admin.site.register(Semester2Model1,Semester2Model1Admin)

admin.site.register(Semester3Internal1,Semester3Internal1Admin)
admin.site.register(Semester3Internal2,Semester3Internal2Admin)
admin.site.register(Semester3Model1,Semester3Model1Admin)

admin.site.register(Semester4Internal1,Semester4Internal1Admin)
admin.site.register(Semester4Internal2,Semester4Internal2Admin)
admin.site.register(Semester4Model1,Semester4Model1Admin)

admin.site.register(Semester5Internal1,Semester5Internal1Admin)
admin.site.register(Semester5Internal2,Semester5Internal2Admin)
admin.site.register(Semester5Model1,Semester5Model1Admin)


admin.site.register(Semester6Internal1,Semester6Internal1Admin)
admin.site.register(Semester6Internal2,Semester6Internal2Admin)
admin.site.register(Semester6Model1,Semester6Model1Admin)

admin.site.register(Semester7Internal1,Semester7Internal1Admin)
admin.site.register(Semester7Internal2,Semester7Internal2Admin)
admin.site.register(Semester7Model1,Semester7Model1Admin)


admin.site.register(Semester8Internal1,Semester8Internal1Admin)
admin.site.register(Semester8Internal2,Semester8Internal2Admin)
admin.site.register(Semester8Model1,Semester8Model1Admin)

admin.site.register(CseStudyMaterial, CseStudyMaterialAdmin)



