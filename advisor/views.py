from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import (MajorCourse, SecondMajorCourse, MinorCourse, CoreCourse,
                        ElectiveCourse, Advisee, Advisor, 
                        Instructor, MajorCourseGrade, SecondMajorCourseGrade,
                        MinorCourseGrade, CoreCourseGrade, ElectiveCourseGrade,
                        GradeChoice,CourseCredit, AdvisorRelationship, StudyMajor)

"""
def index(request):
    recent_student_list = Student.objects.order_by('last_name')[:5]
    template = loader.get_template('advisor/index.html')
    context = {'recent_student_list':recent_student_list,
    }
    return HttpResponse(template.render(context, request))
"""

"""
def index(request):
    recent_student_list = Student.objects.order_by('last_name')[:5]
    context = {'recent_student_list':recent_student_list}
    return render(request, 'advisor/index.html', context)
"""

def index(request):
    # recent_student_list = Student.objects.order_by('last_name')[:5]
    # context = {'recent_student_list':recent_student_list}
    advisees = Advisee.objects.order_by('last_name')
    advisors = Advisor.objects.order_by('last_name')
    study_majors = StudyMajor.objects.order_by('major_name')
    try:
        advisor_relationships = get_list_or_404(AdvisorRelationship)
    except:
        advisor_relationships = "0"
    
    context = {'advisees':advisees, 'advisors':advisors, 'study_majors':study_majors, 'advisor_relationships':advisor_relationships}
    return render(request, 'advisor/index.html', context)

def advisee(request, advisee_id):
    advisee_info = get_object_or_404(Advisee, pk=advisee_id)
    #student_courses = get_list_or_404(CourseGrade.objects.order_by('student_id'))
    try: 
        major_courses = get_list_or_404(MajorCourseGrade, advisee_id=advisee_id)
    except:
        major_courses = "0"

    try: 
        second_major_courses = get_list_or_404(SecondMajorCourseGrade, advisee_id=advisee_id)
    except:
        second_major_courses = "0"

    try: 
        minor_courses = get_list_or_404(MinorCourseGrade, advisee_id=advisee_id)
    except:
        minor_courses = "0"

    try: 
        core_courses = get_list_or_404(CoreCourseGrade, advisee_id=advisee_id)
    except:
        core_courses = "0"

    try: 
        elective_courses = get_list_or_404(ElectiveCourseGrade, advisee_id=advisee_id)
    except:
        elective_courses = "0"
    

    #course_credits = get_list_or_404(CourseGrade, advisee_id=advisee_id)

    # variables uses to track credits in different course categories
    major_credits = 0.0
    second_major_credits = 0.0
    minor_credits = 0.0
    core_credits = 0.0
    elective_credits = 0.0


    gpa = 0.0
    grade_choices = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']

    if major_courses != "0":
        grade = ''
        quality_points = 0
        for course in major_courses:
            if course.grade in grade_choices:
            
                if course.grade == 'A+':
                    quality_points += course.course.credits * 4.3
                elif course.grade == 'A':
                    quality_points += course.course.credits * 4.0
                elif course.grade == 'A-':
                    quality_points += course.course.credits * 3.7
                elif course.grade == 'B+':
                    quality_points += course.course.credits * 3.3
                elif course.grade == 'B':
                    quality_points += course.course.credits * 3.0
                elif course.grade == 'B-':
                    quality_points += course.course.credits * 2.7
                elif course.grade == 'C+':
                    quality_points += course.course.credits * 2.3
                elif course.grade == 'C':
                    quality_points += course.course.credits * 2.0
                elif course.grade == 'C-':
                    quality_points += course.course.credits * 1.7
                elif course.grade == 'D+':
                    quality_points += course.course.credits * 1.3
                elif course.grade == 'D':
                    quality_points += course.course.credits * 1.0
                elif course.grade == 'D-':
                    quality_points += course.course.credits * 0.7
                elif course.grade == 'F':
                    quality_points += course.course.credits * 0.0

        major_credits = 0
        for course in major_courses:
            major_credits+=course.course.credits
            
        try:
            gpa = round((quality_points / credits), 3)
        except: gpa = "TBD"


    if second_major_courses != "0":
        grade = ''
        credits = 0
        quality_points = 0
        for course in second_major_courses:
            if course.grade in grade_choices:
                credits += course.course.credits
                if course.grade == 'A+':
                    quality_points += course.course.credits * 4.3
                elif course.grade == 'A':
                    quality_points += course.course.credits * 4.0
                elif course.grade == 'A-':
                    quality_points += course.course.credits * 3.7
                elif course.grade == 'B+':
                    quality_points += course.course.credits * 3.3
                elif course.grade == 'B':
                    quality_points += course.course.credits * 3.0
                elif course.grade == 'B-':
                    quality_points += course.course.credits * 2.7
                elif course.grade == 'C+':
                    quality_points += course.course.credits * 2.3
                elif course.grade == 'C':
                    quality_points += course.course.credits * 2.0
                elif course.grade == 'C-':
                    quality_points += course.course.credits * 1.7
                elif course.grade == 'D+':
                    quality_points += course.course.credits * 1.3
                elif course.grade == 'D':
                    quality_points += course.course.credits * 1.0
                elif course.grade == 'D-':
                    quality_points += course.course.credits * 0.7
                elif course.grade == 'F':
                    quality_points += course.course.credits * 0.0

    if second_major_courses != "0":
        for course in second_major_courses:
            second_major_credits+=course.course.credits
            
       

    if minor_courses != "0":
        grade = ''
        credits = 0
        quality_points = 0
        for course in minor_courses:
            if course.grade in grade_choices:
                credits += course.course.credits
                if course.grade == 'A+':
                    quality_points += course.course.credits * 4.3
                elif course.grade == 'A':
                    quality_points += course.course.credits * 4.0
                elif course.grade == 'A-':
                    quality_points += course.course.credits * 3.7
                elif course.grade == 'B+':
                    quality_points += course.course.credits * 3.3
                elif course.grade == 'B':
                    quality_points += course.course.credits * 3.0
                elif course.grade == 'B-':
                    quality_points += course.course.credits * 2.7
                elif course.grade == 'C+':
                    quality_points += course.course.credits * 2.3
                elif course.grade == 'C':
                    quality_points += course.course.credits * 2.0
                elif course.grade == 'C-':
                    quality_points += course.course.credits * 1.7
                elif course.grade == 'D+':
                    quality_points += course.course.credits * 1.3
                elif course.grade == 'D':
                    quality_points += course.course.credits * 1.0
                elif course.grade == 'D-':
                    quality_points += course.course.credits * 0.7
                elif course.grade == 'F':
                    quality_points += course.course.credits * 0.0


    if minor_courses != "0":
        for course in minor_courses:
            minor_credits+=course.course.credits
            
      

        if core_courses != "0":
            grade = ''
            credits = 0
            quality_points = 0
            for course in core_courses:
                if course.grade in grade_choices:
                    credits += course.course.credits
                    if course.grade == 'A+':
                        quality_points += course.course.credits * 4.3
                    elif course.grade == 'A':
                        quality_points += course.course.credits * 4.0
                    elif course.grade == 'A-':
                        quality_points += course.course.credits * 3.7
                    elif course.grade == 'B+':
                        quality_points += course.course.credits * 3.3
                    elif course.grade == 'B':
                        quality_points += course.course.credits * 3.0
                    elif course.grade == 'B-':
                        quality_points += course.course.credits * 2.7
                    elif course.grade == 'C+':
                        quality_points += course.course.credits * 2.3
                    elif course.grade == 'C':
                        quality_points += course.course.credits * 2.0
                    elif course.grade == 'C-':
                        quality_points += course.course.credits * 1.7
                    elif course.grade == 'D+':
                        quality_points += course.course.credits * 1.3
                    elif course.grade == 'D':
                        quality_points += course.course.credits * 1.0
                    elif course.grade == 'D-':
                        quality_points += course.course.credits * 0.7
                    elif course.grade == 'F':
                        quality_points += course.course.credits * 0.0

    if core_courses != "0":
        for course in core_courses:
            core_credits+=course.course.credits
        
            
      

    if elective_courses != "0":
        grade = ''
        credits = 0
        quality_points = 0
        for course in elective_courses:
            if course.grade in grade_choices:
                credits += course.course.credits
                if course.grade == 'A+':
                    quality_points += course.course.credits * 4.3
                elif course.grade == 'A':
                    quality_points += course.course.credits * 4.0
                elif course.grade == 'A-':
                    quality_points += course.course.credits * 3.7
                elif course.grade == 'B+':
                    quality_points += course.course.credits * 3.3
                elif course.grade == 'B':
                    quality_points += course.course.credits * 3.0
                elif course.grade == 'B-':
                    quality_points += course.course.credits * 2.7
                elif course.grade == 'C+':
                    quality_points += course.course.credits * 2.3
                elif course.grade == 'C':
                    quality_points += course.course.credits * 2.0
                elif course.grade == 'C-':
                    quality_points += course.course.credits * 1.7
                elif course.grade == 'D+':
                    quality_points += course.course.credits * 1.3
                elif course.grade == 'D':
                    quality_points += course.course.credits * 1.0
                elif course.grade == 'D-':
                    quality_points += course.course.credits * 0.7
                elif course.grade == 'F':
                    quality_points += course.course.credits * 0.0

    if elective_courses != "0":
        for course in elective_courses:
            elective_credits+=course.course.credits
            
    try:
        gpa = round((quality_points / credits), 3)
    except: gpa = "TBD"

    advisors = get_list_or_404(AdvisorRelationship, advisee_id=advisee_id)
    
    """if advisee_courses:
        context = {'advisee_info':advisee_info, 'advisee_courses':advisee_courses, 'advisors':advisors, 'gpa':gpa}
    else:
        context = {'advisee_info':advisee_info, 'advisors':advisors, 'gpa':gpa}"""
    context = {'advisee_info':advisee_info, 'major_courses':major_courses, \
                'second_major_courses':second_major_courses, 'minor_courses':minor_courses, \
                'core_courses':core_courses, 'elective_courses':elective_courses, \
                'advisors':advisors, 'gpa':gpa, 'major_credits':major_credits, \
                'second_major_credits':second_major_credits, 'minor_credits':minor_credits, \
                'core_credits':core_credits, 'elective_credits':elective_credits }

    # return the record.html template. advisor is the app name, record is the advisee name.
    return render(request, 'advisor/advisee.html', context)

    #return render(request, 'advisor/record.html', {'student_name': student_name}, {'student_courses': student_courses})

def advisor_record(request, advisor_id):
    
    advisee_list = get_list_or_404(AdvisorRelationship, advisor_id=advisor_id)
    advisor = get_list_or_404(AdvisorRelationship, advisor_id=advisor_id)[0]
    #advisor = get_object_or_404(AdvisorRelationship, advisee_id=advisee_id)
    #advisor_advisee_info = get_list_or_404(AdvisorRelationship, advisor_id=advisor_id)
    #advisee_list = AdvisorRelationship.objects.order_by('advisor')
    #advisee_list = get_list_or_404(AdvisorRelationship, advisor_id=advisor_id)
    context = {'advisee_list':advisee_list, 'advisor':advisor}
    ##advisor is the app, advisor_record.html is the view
    return render(request, 'advisor/advisor_record.html', context)

def studies(request):
    #advisee_info = get_object_or_404(Advisee, pk=advisee_id)
    study_majors = get_list_or_404(StudyMajor)
    #context = {'advisee_info':advisee_info, 'major':major}
    context = {'study_majors':study_majors}
    ##advisor is the app, major.html is the template
    return render(request, 'advisor/studies.html', context)

def advisees_by_major(request, advisee_id):
    advisee_info = get_object_or_404(Advisee, pk=advisee_id)
    study_majors = get_list_or_404(StudyMajor)
    #context = {'advisee_info':advisee_info, 'major':major}
    context = {'study_majors':study_majors}
    ##advisor is the app, studies.html is the template
    return render(request, 'advisor/studies.html', context)

def advisors(request):
    # recent_student_list = Student.objects.order_by('last_name')[:5]
    # context = {'recent_student_list':recent_student_list}
    
    advisees = Advisee.objects.order_by('last_name')
    advisors = Advisor.objects.order_by('last_name')
    study_majors = StudyMajor.objects.order_by('major_name')
    try:
        advisor_relationships = get_list_or_404(AdvisorRelationship)
    except:
        advisor_relationships = '0'


    #advisor_list = [AdvisorRelationship() for i in range(5) ]
    advisor_list = [get_list_or_404(AdvisorRelationship)]


    
    
    
    #for advisor in advisor_relationships:
    #    advisor_list += advisor
    
    context = {'advisees':advisees, 'advisors':advisors, 'study_majors':study_majors, 'advisor_relationships':advisor_relationships, 'advisor_list':advisor_list}
    return render(request, 'advisor/advisors.html', context)


def advisee_list(request):
    advisees = Advisee.objects.order_by('last_name')
    context = {'advisees':advisees}

    return render(request, 'advisor/advisee_list.html', context)


def courses (request):

    courses = Course.objects.order_by('course_no')
    context = {'courses':courses}

    return render(request, 'advisor/courses.html', context)
