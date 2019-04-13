from django.db import models


class StudyMajor(models.Model):
    major_name = models.CharField(max_length=100)
    concentration = models.CharField(max_length=100, blank=True)

    def __str__(self):
        if self.concentration != "":
            return self.major_name + ": " + self.concentration
        return self.major_name


# model for advisees (students)
class Advisee(models.Model):

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    semester_started = models.CharField(max_length=30, blank=True)
    grade_level = models.CharField(max_length=30, blank=True)
    cell_number = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    first_major = models.ForeignKey(StudyMajor, related_name='advisee_first_major', \
                  on_delete=models.CASCADE, null=True, blank=True)
    second_major = models.ForeignKey(StudyMajor, related_name='advisee_second_major', \
                  on_delete=models.CASCADE, null=True, blank=True)
    
    # Advisor notes. Will be saved to the database.
    notes = models.CharField(max_length=10000, null=True, blank=True)
    
    #concentration = models.CharField(max_length=30, blank=True)
    #minor = models.CharField(max_length=30, blank=True)
    #is_double_major = models.BooleanField(default=False, blank=True)

    def __str__(self):
        
        if self.middle_name != "":
            return self.last_name + ", " + self.first_name + " " + self.middle_name

        return self.last_name + ", " + self.first_name


class Advisor(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        
        if self.middle_name != "":
            return self.last_name + ", " + self.first_name + " " + self.middle_name

        return self.last_name + ", " + self.first_name


class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        
        if self.middle_name != "":
            return self.first_name + " " + self.middle_name + " " + self.last_name

        return self.last_name + ", " + self.first_name + " " + self.middle_name


class GradeChoice(models.Model):
    grade = models.CharField(max_length=10)

    def __str__(self):
        
        return self.grade

class MajorCourse(models.Model):
    course_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.FloatField(max_length=10, default=3.0)
    instructor_name = models.CharField(max_length=100, blank=True)
    is_developmental = models.BooleanField(default=False, blank=True)
    #instructor_name = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.course_no + " - " + self.course_name

class SecondMajorCourse(models.Model):
    course_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.FloatField(max_length=10, blank=True, null=True)
    instructor_name = models.CharField(max_length=100, blank=True)
    is_developmental = models.BooleanField(default=False, blank=True)
    #instructor_name = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.course_no + " - " + self.course_name

"""class MinorCourse(models.Model):
    course_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.FloatField(max_length=10, blank=True, null=True)
    instructor_name = models.CharField(max_length=100, blank=True)
    #instructor_name = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.course_no + " - " + self.course_name"""

class CoreCourse(models.Model):
    course_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.FloatField(max_length=10, blank=True, null=True)
    instructor_name = models.CharField(max_length=100, blank=True)
    is_developmental = models.BooleanField(default=False, blank=True)
    #instructor_name = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.course_no + " - " + self.course_name

class ElectiveCourse(models.Model):
    course_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.FloatField(max_length=10, blank=True, null=True)
    instructor_name = models.CharField(max_length=100, blank=True)
    is_developmental = models.BooleanField(default=False, blank=True)
    #instructor_name = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.course_no + " - " + self.course_name


class MajorCourseGrade(models.Model):
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)
    course = models.ForeignKey(MajorCourse, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True)
    #credits = models.ForeignKey(Course, on_delete=models.CASCADE)
    #grade = models.ForeignKey(GradeChoice, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        
        #return str(self.grade)
        return str(self.advisee) + " - " + str(self.course) + " = " + str(self.grade)

class SecondMajorCourseGrade(models.Model):
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)
    course = models.ForeignKey(SecondMajorCourse, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True)
    #credits = models.ForeignKey(Course, on_delete=models.CASCADE)
    #grade = models.ForeignKey(GradeChoice, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        
        #return str(self.grade)
        return str(self.advisee) + " - " + str(self.course) + " = " + str(self.grade)

"""class MinorCourseGrade(models.Model):
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)
    course = models.ForeignKey(MinorCourse, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True)
    #credits = models.ForeignKey(Course, on_delete=models.CASCADE)
    #grade = models.ForeignKey(GradeChoice, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        
        #return str(self.grade)
        return str(self.advisee) + " - " + str(self.course) + " = " + str(self.grade)"""

class CoreCourseGrade(models.Model):
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)
    course = models.ForeignKey(CoreCourse, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True)
    #credits = models.ForeignKey(Course, on_delete=models.CASCADE)
    #grade = models.ForeignKey(GradeChoice, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        
        #return str(self.grade)
        return str(self.advisee) + " - " + str(self.course) + " = " + str(self.grade)

class ElectiveCourseGrade(models.Model):
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)
    course = models.ForeignKey(ElectiveCourse, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True)
    #credits = models.ForeignKey(Course, on_delete=models.CASCADE)
    #grade = models.ForeignKey(GradeChoice, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        
        #return str(self.grade)
        return str(self.advisee) + " - " + str(self.course) + " = " + str(self.grade)

class CourseCredit(models.Model):
    course = models.ForeignKey(MajorCourse, on_delete=models.CASCADE)
    hours = models.CharField(max_length=10)

    def __str__(self):

        return str(self.course) + " = " + self.hours + " credit hours."

class AdvisorRelationship(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.advisor) + " ---> " + str(self.advisee)


class Note(models.Model):
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)
    text = models.CharField(max_length=120, null=True, blank=True)
    #created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):

        return str(self.advisee) + ": " + str(self.text)

class FutureCourse(models.Model):
    advisee = models.ForeignKey(Advisee, on_delete=models.CASCADE)
    course_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    course_term = models.CharField(max_length=10, blank=True, null=True)
    course_year = models.CharField(max_length=10, blank=True, null=True)
    credits = models.FloatField(max_length=10, blank=True, null=True)
    instructor_name = models.CharField(max_length=100, blank=True, null=True)
    is_developmental = models.BooleanField(default=False, blank=True)

    
    def __str__(self):
        return self.course_no + " - " + self.course_name + " - " + self.advisee.last_name + ", " + self.advisee.first_name





