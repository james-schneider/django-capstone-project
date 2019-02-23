from django.contrib import admin

from .models import (MajorCourse, SecondMajorCourse, MinorCourse, CoreCourse,
                        ElectiveCourse, Advisee, Advisor, 
                        Instructor, MajorCourseGrade, SecondMajorCourseGrade,
                        MinorCourseGrade, CoreCourseGrade, ElectiveCourseGrade,
                        GradeChoice,CourseCredit, AdvisorRelationship, StudyMajor)

admin.site.register(MajorCourse)
admin.site.register(SecondMajorCourse)
admin.site.register(MinorCourse)
admin.site.register(CoreCourse)
admin.site.register(ElectiveCourse)
admin.site.register(Advisee)
admin.site.register(Advisor)
#admin.site.register(Major)
admin.site.register(Instructor)
admin.site.register(MajorCourseGrade)
admin.site.register(GradeChoice)
admin.site.register(CourseCredit)
admin.site.register(AdvisorRelationship)
admin.site.register(StudyMajor)
admin.site.register(CoreCourseGrade)

