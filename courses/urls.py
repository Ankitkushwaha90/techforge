from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # HTML views
    path('', views.courses_list, name='courses_list'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
    path('<slug:course_slug>/modules/<int:module_id>/', views.module_detail, name='module_detail'),
    
    # API endpoints
    path('api/courses/', views.CourseListCreateView.as_view(), name='api-courses-list'),
    path('api/courses/<slug:slug>/', views.CourseDetailView.as_view(), name='api-course-detail'),
    path('api/courses/<int:course_id>/modules/', views.ModuleListCreateView.as_view(), name='api-module-list'),
    path('api/courses/<int:course_id>/modules/<int:pk>/', views.ModuleDetailView.as_view(), name='api-module-detail'),
    path('api/modules/<int:module_id>/contents/', views.ContentListCreateView.as_view(), name='api-content-list'),
    path('api/modules/<int:module_id>/contents/<int:pk>/', views.ContentDetailView.as_view(), name='api-content-detail'),
]
