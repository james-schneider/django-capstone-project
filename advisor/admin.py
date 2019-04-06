from django.contrib import admin

from .models import (MajorCourse, SecondMajorCourse, CoreCourse,
                        ElectiveCourse, Advisee, Advisor, 
                        Instructor, MajorCourseGrade, SecondMajorCourseGrade,
                        CoreCourseGrade, ElectiveCourseGrade,
                        GradeChoice, CourseCredit, AdvisorRelationship, StudyMajor,
                        Note, FutureCourse)

admin.site.register(MajorCourse)
admin.site.register(SecondMajorCourse)
#admin.site.register(MinorCourse)
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
admin.site.register(SecondMajorCourseGrade)
#admin.site.register(MinorCourseGrade)
admin.site.register(ElectiveCourseGrade)
admin.site.register(Note)
admin.site.register(FutureCourse)

