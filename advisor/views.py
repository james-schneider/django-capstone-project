from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.template import loader
from django.http import HttpResponse
from.forms import NoteForm

from .models import (MajorCourse, SecondMajorCourse, CoreCourse,
                        ElectiveCourse, Advisee, Advisor, 
                        Instructor, MajorCourseGrade, SecondMajorCourseGrade,
                        CoreCourseGrade, ElectiveCourseGrade,
                        GradeChoice,CourseCredit, AdvisorRelationship, StudyMajor,
                        Note, FutureCourse)

# original index view.  Not going to use it, but leaving it here for
# information only.
"""
def index(request):
    recent_student_list = Student.objects.order_by('last_name')[:5]
    template = loader.get_template('advisor/index.html')
    context = {'recent_student_list':recent_student_list,
    }
    return HttpResponse(template.render(context, request))
"""


################################################################################
# function: index
# input: 
# processing: create lists of each of the different types of courses.
#             The lists are going to be used to display the invidual
#             student records.
# output: render, which is an HTML page that displays the advisors
#################################################################################
def index(request):
    
    # list of advisors objects
    advisors = Advisor.objects.order_by('last_name')

    # context is a dictionary of values that is sent with the render request.
    # It includes all of the variables that you want to use on the html page
    # that is going to be rendered.
    context = {'advisors':advisors}
    return render(request, 'advisor/index.html', context)


################################################################################
# function: advisee
# input: advisee_id--id number that is automatically created when
#        a new advisee (student) is added to the database.
# processing: create lists of each of the different types of courses.
#             The lists are going to be used to display the invidual
#             student records.
# output: render, which is an HTML page that displays individual student records
#################################################################################
def advisee(request, advisee_id):
    
    # list of advisees from the Advisee model in models.py
    advisee_info = get_object_or_404(Advisee, pk=advisee_id)

    # list of course grades from the MajorCourseGrade model in models.py
    try: 
        major_courses = get_list_or_404(MajorCourseGrade, advisee_id=advisee_id)
    except:
        major_courses = "0"

    major_requirements_met = False

    # list of courses required for CIS major
    required_for_CIS_major = ['CIS 175', 'CIS 201', 'CIS 211', 'CIS 297', 'CIS 301',
                                'CIS 305', 'CIS 310', 'CIS 318', 'CIS 341', 'CIS 420',
                                'CIS 450']
    
    # list of math courses for CIS major.  Only one is required.
    math_for_CIS_major = ['MATH 211', 'MATH 213', 'MATH 302']

    # list of electives for CIS major.  Only two are required.
    electives_for_CIS_major = ['ACCT 211', 'ACCT 430', 'CIS 285', 'CIS 401', 'CIS 495',
                                'CS 287', 'CS 313', 'CS 315', 'CS 418', 'CS 430']

    required_for_CIS_major_counter = 0
    math_for_CIS_major_counter = 0
    electives_for_CIS_major_counter = 0


    if major_courses != "0":
        if advisee_info.first_major == 'CIS':
            for course in major_courses:
                if course.course.course_no in required_for_CIS_major:
                    required_for_CIS_major_counter += 1
                if course.course.course_no in math_for_CIS_major:
                    math_for_CIS_major_counter += 1
                if course.course.course_no in electives_for_CIS_major:
                    electives_for_CIS_major_counter += 1
        
            if required_for_CIS_major_counter >= 11 and math_for_CIS_major_counter >=1 and \
                electives_for_CIS_major_counter >= 2:
                major_requirements_met = True


    # list of course grades from the SecondMajorCourseGrade model in models.py
    try: 
        second_major_courses = get_list_or_404(SecondMajorCourseGrade, advisee_id=advisee_id)
    except:
        second_major_courses = "0"

    # not using the MinorCourses model.  Including minor courses
    # and other information in the SecondMajor model
    """try: 
        minor_courses = get_list_or_404(MinorCourseGrade, advisee_id=advisee_id)
    except:
        minor_courses = "0"""

    # list of course grades from the CoreCourseGrade model in models.py
    try: 
        core_courses = get_list_or_404(CoreCourseGrade, advisee_id=advisee_id)
    except:
        core_courses = "0"

    # list of course grades from the ElectiveCourseGrade model in models.py
    try: 
        elective_courses = get_list_or_404(ElectiveCourseGrade, advisee_id=advisee_id)
    except:
        elective_courses = "0"

    try:
        future_courses = get_list_or_404(FutureCourse, advisee_id=advisee_id)
    except:
        future_courses = "0"
    

    # initialize variables used to track credits
    # in different course categories
    major_credits = 0.0
    second_major_credits = 0.0
    minor_credits = 0.0
    core_credits = 0.0
    elective_credits = 0.0
    total_credits = 0.0

    # initialize variables used to track credits for GPA 
    # in different course categories
    gpa_major_credits = 0.0
    gpa_second_major_credits = 0.0
    gpa_minor_credits = 0.0
    gpa_core_credits = 0.0
    gpa_elective_credits = 0.0
    gpa_total_credits = 0.0

    
    # initialize variables used to track quality points for GPA
    # in different course categories
    gpa_major_quality_points = 0.0
    gpa_second_major_quality_points = 0.0
    gpa_minor_quality_points = 0.0
    gpa_core_quality_points = 0.0
    gpa_elective_quality_points = 0.0
    gpa_total_quality_points = 0.0

    # initialize variable used to track developmental credits
    # this variable will be subtracted from credits needed for graduation
    developmental_credits = 0.0
    
    
    # initialize gpa variable. Used to calculate an advisee's GPA
    gpa = 0.0
    # list of choices that will be used to calculate quality points for GPA purposes
    grade_choices = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']

    
    if major_courses != "0":
        quality_points = 0.0
        # loop through all of the major courses to find out how many
        # credits have been earned and calculate GPA
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

                
                # variable used to calculate GPA
                gpa_major_credits+=course.course.credits
                # variable used to calculate GPA
                gpa_major_quality_points+=quality_points
                
                # reset quality points for calculation in next course
                quality_points = 0.0

            if course.course.is_developmental == True:
                developmental_credits += course.course.credits

            major_credits+=course.course.credits

            


    if second_major_courses != "0":
        quality_points = 0.0
        # loop through all of the second major courses to find out how many
        # credits have been earned and calculate GPA
        for course in second_major_courses:
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

                gpa_second_major_credits+=course.course.credits

                gpa_second_major_quality_points+=quality_points

                # reset quality points for calculation in next course
                quality_points = 0.0

            if course.course.is_developmental == True:
                developmental_credits += course.course.credits
            
            second_major_credits+=course.course.credits


                        
       
    # not using the MinorCourses model.  Including minor courses
    # and other information in the SecondMajor model.
    """if minor_courses != "0":
        grade = ''
        quality_points = 0.0
        for course in minor_courses:
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

                gpa_minor_credits+=course.course.credits

                gpa_minor_quality_points+=quality_points
            
            minor_credits+=course.course.credits

            minor_quality_points+=quality_points"""
            
      
    
    if core_courses != "0":
        quality_points = 0.0
        # loop through all of the core courses to find out how many
        # credits have been earned and calculate GPA
        for course in core_courses:
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

                # variables to be used to calculate GPA
                gpa_core_credits+=course.course.credits
                # variables to be used to calculate GPA
                gpa_core_quality_points+=quality_points

                # reset quality points for calculation in next course
                quality_points = 0.0

            if course.course.is_developmental == True:
                developmental_credits += course.course.credits

            # variables to be used to calculate credits--not included in GPA
            core_credits+=course.course.credits
        

    if elective_courses != "0":
        quality_points = 0.0
        # loop through all of the elective courses to find out how many
        # credits have been earned and calculate GPA
        for course in elective_courses:
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

                # variable used to calculate GPA
                gpa_elective_credits+=course.course.credits
                # variable used to calculate GPA
                gpa_elective_quality_points+=quality_points

                # reset quality points for calculation in next course
                quality_points = 0.0

            if course.course.is_developmental == True:
                developmental_credits += course.course.credits

            # variable used to calculate credits--not included in GPA
            elective_credits+=course.course.credits


    # logic for 'double dipping'. A student can count up to three courses
    # in both a major, double major and/or minor.
    # However, they only get the grade and credit hours for one instance.
    major_course_list = []
    second_major_course_list = []
    elective_course_list = []
    in_major_and_second_major_list = []
    
    if major_courses != '0':
        for course in major_courses:
            major_course_list.append(course.course.course_no)

    if second_major_courses != '0':
        for course in second_major_courses:
            second_major_course_list.append(course.course.course_no)

    if elective_courses != '0':
        for course in elective_courses:
            elective_course_list.append(course.course.course_no)
    
    for course in major_course_list:
        if course in second_major_course_list:
            in_major_and_second_major_list.append(course)

    double_dip_count = 0
    for item in in_major_and_second_major_list:
        double_dip_count +=1

    



    
        


    # variable used for displaying total credits of all courses
    # developmental course credits will be subtraced
    total_credits = (major_credits + second_major_credits + minor_credits \
                    + core_credits + elective_credits - developmental_credits)

    # variable used for calculating credits--used in GPA calculation
    gpa_total_credits = (gpa_major_credits + gpa_second_major_credits + gpa_minor_credits \
                    + gpa_core_credits + gpa_elective_credits)
    # variable used for calculating quality points--used in GPA calculation
    gpa_total_quality_points = (gpa_major_quality_points + gpa_second_major_quality_points + \
                        gpa_minor_quality_points + gpa_core_quality_points + gpa_elective_quality_points)
            
    # calculate GPA, else gpa = "TBD"
    # GPA includes developmental courses
    try:
        gpa = round((gpa_total_quality_points / gpa_total_credits), 3)
    except: gpa = "TBD"
    
    #variable used to display the advisor of the individual advisee
    advisors = get_list_or_404(AdvisorRelationship, advisee_id=advisee_id)
    



    # notes that will be used for advisor notes
    try: 
        notes = get_list_or_404(Note, advisee_id=advisee_id)
        #notes = get_list_or_404(Note)
    except:
        notes = ""
    
    # Not being used yet---------------------------------------
    # ---------------------------------------------------------
    # this is the form that is going to be used for
    # adding notes.
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    #-----------------------------------------------------------


    
    # title that is going to show up in the browser tab
    title=advisee_info.first_name + " " + advisee_info.last_name
    
    # context is a dictionary of values that is sent with the render request.
    # It includes all of the variables that you want to use on the html page
    # that is going to be rendered.
    context = {'advisee_info':advisee_info, 'major_courses':major_courses, \
                'second_major_courses':second_major_courses, \
                'core_courses':core_courses, 'elective_courses':elective_courses, \
                'advisors':advisors, 'gpa':gpa, 'major_credits':major_credits, \
                'second_major_credits':second_major_credits, 'minor_credits':minor_credits, \
                'core_credits':core_credits, 'elective_credits':elective_credits, 'total_credits':total_credits, \
                'title':title, 'notes':notes, 'form':form, 'major_course_list':major_course_list, \
                'in_major_and_second_major_list':in_major_and_second_major_list, 'double_dip_count':double_dip_count,
                'future_courses':future_courses, 'major_requirements_met':major_requirements_met}

    #advisor is the name of the app, advisee.html is the template
    return render(request, 'advisor/advisee.html', context)

    
    
    


################################################################################
# function: advisor_record
# input: advisor_id--id number that is automatically created when a new advisor
#        is added to the database
# processing: create list of advisor relationships to display all of the
#             advisees (students) assigned to that particular advisor
# output: render, which is an HTML page that displays the advisors and
#         all of their advisees
#################################################################################
def advisor_record(request, advisor_id):
    
    advisee_list = get_list_or_404(AdvisorRelationship, advisor_id=advisor_id)
    advisor = get_list_or_404(AdvisorRelationship, advisor_id=advisor_id)[0]

    # title that is going to show up in the browser tab
    title = advisor.advisor.first_name + " " + advisor.advisor.last_name
    
    context = {'advisee_list':advisee_list, 'advisor':advisor, 'title':title}
    
    #advisor is the name of the app, advisor_record.html is the template
    return render(request, 'advisor/advisor_record.html', context)



################################################################################
# function: advisors
# input: 
# processing: create list of advisor objects
# output: render, which is an HTML page that displays the advisors
#################################################################################
def advisors(request):

    advisors = Advisor.objects.order_by('last_name')
    
    #title for web page metadata
    title = 'Advisors'
    
    context = {'advisors':advisors, 'title':title}

    #advisor is the name of the app, advisors.html is the template
    return render(request, 'advisor/advisors.html', context)


################################################################################
# function: advisee_list
# input: page request
# processing: create list of advisee (student) objects
# output: render, which is an HTML page that displays the advisees (students)
#################################################################################
def advisee_list(request):
    
    advisees = Advisee.objects.order_by('last_name')
    
    #title for web page metadata
    title = 'Advisees'
    
    context = {'advisees':advisees, 'title':title}

    #advisor is the name of the app, advisee_list.html is the template
    return render(request, 'advisor/advisee_list.html', context)


################################################################################
# function: about
# input: page request
# processing: none
# output: render, which is an HTML page that displays the About page info
#################################################################################
def about(request):

    #title for web page metadata
    title = 'About'

    context = {'title':title}

    #advisor is the name of the app, about.html is the template
    return render(request, 'advisor/about.html', context)




def advisees_by_major(request, advisee_id):

    advisee_info = get_object_or_404(Advisee, pk=advisee_id)
    study_majors = get_list_or_404(StudyMajor)
    #context = {'advisee_info':advisee_info, 'major':major}
    context = {'study_majors':study_majors}
    ##advisor is the app, studies.html is the template
    return render(request, 'advisor/studies.html', context)


def courses (request):

    courses = Course.objects.order_by('course_no')
    context = {'courses':courses}

    return render(request, 'advisor/courses.html', context)


def studies(request):
    
    study_majors = get_list_or_404(StudyMajor)
    
    context = {'study_majors':study_majors}

    return render(request, 'advisor/studies.html', context)
