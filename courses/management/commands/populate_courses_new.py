from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from courses.models import Course, Module, Content

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with sample courses, modules, and content'

    def handle(self, *args, **options):
        # Clear existing data
        Content.objects.all().delete()
        Module.objects.all().delete()
        Course.objects.all().delete()
        
        # Create a test instructor
        instructor, created = User.objects.get_or_create(
            username='instructor',
            defaults={
                'email': 'instructor@techforge.com',
                'first_name': 'Tech',
                'last_name': 'Instructor',
                'is_staff': True
            }
        )
        if created:
            instructor.set_password('instructor123')
            instructor.save()

        # Course 1: Web Development
        web_course = Course.objects.create(
            title="Complete Web Development Bootcamp",
            slug="web-development-bootcamp",
            description="Learn modern web development with HTML, CSS, JavaScript, and React.",
            difficulty="Beginner",
            estimated_duration=60,
            instructor=instructor,
            price=99.99
        )

        # Module 1: HTML & CSS
        html_module = Module.objects.create(
            course=web_course,
            title="HTML & CSS Fundamentals",
            description="Learn the building blocks of web development",
            order=1
        )
        
        # Add content to HTML module
        Content.objects.create(
            module=html_module,
            title="Introduction to HTML",
            description="Learn the basics of HTML structure and elements",
            code="<!DOCTYPE html>\n<html>\n<head>\n    <title>My First Page</title>\n</head>\n<body>\n    <h1>Hello, World!</h1>\n</body>\n</html>",
            code_language="html",
            order=1
        )
        
        Content.objects.create(
            module=html_module,
            title="CSS Styling",
            description="Learn how to style your web pages with CSS",
            code=".header {\n    color: #333;\n    font-size: 2rem;\n    text-align: center;\n}",
            code_language="css",
            order=2
        )

        # Module 2: JavaScript
        js_module = Module.objects.create(
            course=web_course,
            title="JavaScript Basics",
            description="Learn JavaScript programming fundamentals",
            order=2
        )
        
        # Add content to JavaScript module
        Content.objects.create(
            module=js_module,
            title="Variables and Data Types",
            description="Learn about JavaScript variables and data types",
            code="// Variables\nlet message = 'Hello, World!';\nconst PI = 3.14159;\n\n// Data Types\nlet name = 'John';  // String\nlet age = 30;       // Number\nlet isStudent = true; // Boolean",
            code_language="javascript",
            order=1
        )

        # Course 2: Python Programming
        python_course = Course.objects.create(
            title="Python for Beginners",
            slug="python-for-beginners",
            description="Learn Python programming from scratch",
            difficulty="Beginner",
            estimated_duration=40,
            instructor=instructor,
            price=79.99
        )
        
        # Module for Python course
        python_basics = Module.objects.create(
            course=python_course,
            title="Python Basics",
            description="Get started with Python programming",
            order=1
        )
        
        # Add content to Python module
        Content.objects.create(
            module=python_basics,
            title="Variables and Data Types",
            description="Learn about Python variables and data types",
            code="# Variables and Data Types\nname = 'Alice'  # String\nage = 25        # Integer\nheight = 5.9    # Float\nis_student = True  # Boolean\n\n# Print values\nprint(f'Name: {name}, Age: {age} years')",
            code_language="python",
            order=1
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample courses and content!'))
