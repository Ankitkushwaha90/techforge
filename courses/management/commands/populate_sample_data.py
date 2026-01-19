from django.core.management.base import BaseCommand
from courses.models import Course, Module, Content

class Command(BaseCommand):
    help = 'Populate the database with sample courses, modules, and content'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write("Clearing existing data...")
        Content.objects.all().delete()
        Module.objects.all().delete()
        Course.objects.all().delete()
        
        # ===== COURSE 1: Web Development =====
        self.stdout.write("Creating Web Development course...")
        web_course = Course.objects.create(
            title="Complete Web Development Bootcamp",
            slug="web-development-bootcamp",
            description="Master modern web development with HTML5, CSS3, JavaScript, React, Node.js, and databases."
        )

        # Module 1: HTML & CSS Fundamentals
        self.stdout.write("Adding HTML & CSS module...")
        html_module = Module.objects.create(
            course=web_course,
            title="HTML5 & CSS3 Fundamentals",
            description="Learn the building blocks of web development with modern HTML5 and CSS3",
            order=1
        )
        
        # HTML Content
        Content.objects.create(
            module=html_module,
            title="HTML5 Structure and Semantics",
            description="Learn about HTML5 document structure and semantic elements",
            code="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>
    <main>
        <article>
            <h2>About Me</h2>
            <p>Hello! I'm learning web development.</p>
        </article>
    </main>
</body>
</html>""",
            code_language="html",
            order=1
        )
        
        # CSS Content
        Content.objects.create(
            module=html_module,
            title="CSS3 Styling",
            description="Learn basic CSS styling",
            code="""/* Basic CSS Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
}

h1 {
    color: #2c3e50;
    margin-bottom: 20px;
}

p {
    margin-bottom: 15px;
}""",
            code_language="css",
            order=2
        )

        # Module 2: JavaScript Fundamentals
        self.stdout.write("Adding JavaScript module...")
        js_module = Module.objects.create(
            course=web_course,
            title="JavaScript Fundamentals",
            description="Learn the basics of JavaScript programming",
            order=2
        )
        
        # JavaScript Content
        Content.objects.create(
            module=js_module,
            title="Variables and Functions",
            description="Learn about variables and functions in JavaScript",
            code="""// Variables
let name = 'John';
const age = 30;
var isStudent = true;

// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow function
const add = (a, b) => a + b;

// Using the functions
console.log(greet('Alice')); // Hello, Alice!
console.log(add(5, 3)); // 8""",
            code_language="javascript",
            order=1
        )

        # Module 3: React Basics
        self.stdout.write("Adding React module...")
        react_module = Module.objects.create(
            course=web_course,
            title="Introduction to React",
            description="Get started with React.js for building user interfaces",
            order=3
        )
        
        # React Content
        Content.objects.create(
            module=react_module,
            title="Your First React Component",
            description="Learn how to create a basic React component",
            code="""import React from 'react';

function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

export default App;""",
            code_language="javascript",
            order=1
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data!'))
