from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from . import views

app_name = 'advisor'
urlpatterns = [
    
    # ex: /advisor/
    path('', views.index, name='index'),
    
    # ex: /advisor/advisee/1
    path('advisee/<int:advisee_id>/', views.advisee, name='advisee'),

    # ex: /advisor/advisor/1
    path('advisor/<int:advisor_id>/', views.advisor_record, name='advisor_record'),

    # ex: /advisor/majors
    path('majors/', views.studies, name='studies'),

    # ex: /advisor/advisors
    path('advisors/', views.advisors, name='advisors'),

    # ex: /advisor/advisees
    path('advisees/', views.advisee_list, name='advisee_list'),

    # ex: /advisor/courses
    path('courses/', views.courses, name='courses'),

    # ex: /advisor/about
    path('about/', views.about, name='about'),

    path('note/<int:advisee_id>/', views.note, name='note'),

    path('majorgrades/<int:advisee_id>/', views.major_grades, name='major_grades'),

    path('secondmajorgrades/<int:advisee_id>/', views.second_major_grades, name='second_major_grades'),

    path('coregrades/<int:advisee_id>/', views.core_grades, name='core_grades'),

    path('electivegrades/<int:advisee_id>/', views.elective_grades, name='elective_grades'),

    path('futurecourses/<int:advisee_id>/', views.future_courses, name='future_courses'),

    #path('note/<int:advisee_id>/', views.note_detail, name='note_detail'),
    #path('note/new/', views.note_new, name='note_new'),
    #path('note/<int:advisee_id>/edit/', views.note_edit, name='note_edit'),



] 

#+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
