from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, Module, Content
from .serializers import CourseSerializer, ModuleSerializer, ContentSerializer

def courses_list(request):
    """View function to display all courses in a card-based layout."""
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/courses_list.html', {'courses': courses})

def course_detail(request, slug):
    """View function to display a single course with its modules and content."""
    course = get_object_or_404(Course, slug=slug)
    modules = course.modules.all().order_by('order')
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'modules': modules
    })

def module_detail(request, course_slug, module_id):
    """View function to display a single module with its contents."""
    module = get_object_or_404(Module, id=module_id, course__slug=course_slug)
    contents = module.contents.all().order_by('order')
    
    # Debug information
    print(f"Module ID: {module_id}, Title: {module.title}")
    print(f"Number of contents: {contents.count()}")
    for i, content in enumerate(contents, 1):
        print(f"Content {i}: ID={content.id}, Title='{content.title}', Type={content.code_language if hasattr(content, 'code_language') else 'N/A'}")
    
    return render(request, 'courses/module_detail.html', {
        'course': module.course,
        'module': module,
        'contents': contents
    })

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'

class ModuleListCreateView(generics.ListCreateAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.filter(course_id=self.kwargs['course_id'])

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.kwargs['course_id'])
        serializer.save(course=course)

class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.filter(
            course_id=self.kwargs['course_id'],
            id=self.kwargs['pk']
        )

class ContentListCreateView(generics.ListCreateAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.filter(module_id=self.kwargs['module_id'])

    def perform_create(self, serializer):
        module = Module.objects.get(id=self.kwargs['module_id'])
        serializer.save(module=module)

class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.filter(
            module_id=self.kwargs['module_id'],
            id=self.kwargs['pk']
        )
