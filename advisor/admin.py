from django.contrib import admin

from .models import (Course, Advisee, Advisor, 
                        Instructor, CourseGrade, GradeChoice, 
                        CourseCredit, AdvisorRelationship, StudyMajor)

admin.site.register(Course)
admin.site.register(Advisee)
admin.site.register(Advisor)
#admin.site.register(Major)
admin.site.register(Instructor)
admin.site.register(CourseGrade)
admin.site.register(GradeChoice)
admin.site.register(CourseCredit)
admin.site.register(AdvisorRelationship)
admin.site.register(StudyMajor)

