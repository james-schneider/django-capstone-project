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

    #path('note/<int:advisee_id>/', views.note_detail, name='note_detail'),
    #path('note/new/', views.note_new, name='note_new'),
    #path('note/<int:advisee_id>/edit/', views.note_edit, name='note_edit'),



] 

#+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
