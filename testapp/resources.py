from import_export import resources
from .models import *

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('rollnumber','name','dept','year','dob','fathername','address','phone','email','bloodgrp')


class CseSyllabusResource(resources.ModelResource):
    class Meta:
        model = CseSyllabus
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('semester','subcode','subname')


class CseSemester1Resource(resources.ModelResource):
    class Meta:
        model = CseSemester1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8151','MA8151','PH8151','CY8151','GE8151','GE8152')

class CseSemester2Resource(resources.ModelResource):
    class Meta:
        model = CseSemester2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8251','MA8251','PH8252','BE8255','GE8291','CS8251')

class CseSemester3Resource(resources.ModelResource):
    class Meta:
        model = CseSemester3
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8351','CS8351','CS8391','CS8392','EC8395')

class CseSemester4Resource(resources.ModelResource):
    class Meta:
        model = CseSemester4
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8402','CS8491','CS8492','CS8451','CS8493','CS8494')

class CseSemester5Resource(resources.ModelResource):
    class Meta:
        model = CseSemester5
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8551','CS8591','EC8691','CS8501','CS8592')


class CseSemester6Resource(resources.ModelResource):
    class Meta:
        model = CseSemester6
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('CS8651','CS8691','CS8601','CS8602','CS8603','GE8075')


class CseSemester7Resource(resources.ModelResource):
    class Meta:
        model = CseSemester7
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071')


class CseSemester8Resource(resources.ModelResource):
    class Meta:
        model = CseSemester8
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('GE8076','CS8080')


# semester 1 internal marks 

class Semester1Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester1Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8151','MA8151','PH8151','CY8151','GE8151','GE8152')

class Semester1Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester1Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8151','MA8151','PH8151','CY8151','GE8151','GE8152')

class Semester1Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester1Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8151','MA8151','PH8151','CY8151','GE8151','GE8152')

# semester 2 internal marks 

class Semester2Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester2Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8251','MA8251','PH8252','BE8255','GE8291','CS8251')

class Semester2Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester2Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8251','MA8251','PH8252','BE8255','GE8291','CS8251')

class Semester2Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester2Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('HS8251','MA8251','PH8252','BE8255','GE8291','CS8251')

# semester 3 internal marks 

class Semester3Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester3Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8351','CS8351','CS8391','CS8392','EC8395')

class Semester3Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester3Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8351','CS8351','CS8391','CS8392','EC8395')

class Semester3Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester3Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8351','CS8351','CS8391','CS8392','EC8395')

# semester 4 internal marks 

class Semester4Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester4Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8402','CS8491','CS8492','CS8451','CS8493','CS8494')

class Semester4Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester4Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8402','CS8491','CS8492','CS8451','CS8493','CS8494')

class Semester4Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester4Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8402','CS8491','CS8492','CS8451','CS8493','CS8494')

# semester 5 internal marks 

class Semester5Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester5Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8551','CS8591','EC8691','CS8501','CS8592')

class Semester5Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester5Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8551','CS8591','EC8691','CS8501','CS8592')

class Semester5Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester5Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MA8551','CS8591','EC8691','CS8501','CS8592')

# semester 6 internal marks 

class Semester6Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester6Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('CS8651','CS8691','CS8601','CS8602','CS8603','GE8075')

class Semester6Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester6Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('CS8651','CS8691','CS8601','CS8602','CS8603','GE8075')

class Semester6Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester6Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('CS8651','CS8691','CS8601','CS8602','CS8603','GE8075')

# semester 7 internal marks 

class Semester7Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester7Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071')

class Semester7Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester7Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071')

class Semester7Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester7Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('MG8591','CS8792','CS8791','CS8092','CS8091','GE8077','GE8071')

# semester 8 internal marks 

class Semester8Internal1Resource(resources.ModelResource):
    class Meta:
        model = Semester8Internal1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('GE8076','CS8080')

class Semester8Internal2Resource(resources.ModelResource):
    class Meta:
        model = Semester8Internal2
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('GE8076','CS8080')

class Semester8Model1Resource(resources.ModelResource):
    class Meta:
        model = Semester8Model1
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('GE8076','CS8080')


# Cse Study material

class CseStudyMaterialResource(resources.ModelResource):
    class Meta:
        model = CseStudyMaterial
        exclude = ('id',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('semester','link')

