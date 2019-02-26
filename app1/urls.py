from django.urls import path,re_path
from app1 import views

app_name='app1'

urlpatterns = [
    path('school_list',views.SchoolListView.as_view(),name='school_list'),
    path('student_list',views.StudentListView.as_view(),name='student_list'),
    re_path(r'^school_details/(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='school_details'),
    re_path(r'^student_details/(?P<pk>\d+)/$',views.StudentDetailView.as_view(),name='student_details'),
    path('school_create/',views.SchoolCreateView.as_view(),name='school_create'),
    path('student_create/',views.StudentCreateView.as_view(),name='student_create'),
    re_path(r'^school_update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='school_update'),
    re_path(r'^student_update/(?P<pk>\d+)/$',views.StudentUpdateView.as_view(),name='student_update'),
    re_path(r'^school_delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='school_delete'),
    re_path(r'^student_delete/(?P<pk>\d+)/$',views.StudentDeleteView.as_view(),name='student_delete'),
]
