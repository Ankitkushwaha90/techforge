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
        
        # ===== COURSE 1: Web Development =====
        web_course = Course.objects.create(
            title="Complete Web Development Bootcamp",
            slug="web-development-bootcamp",
            description="Master modern web development with HTML5, CSS3, JavaScript, React, Node.js, and databases."
        )

        # Module 1: HTML & CSS Fundamentals
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
            code="<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>My First Web Page</title>\n</head>\n<body>\n    <header>\n        <h1>Welcome to My Website</h1>\n        <nav>\n            <ul>\n                <li><a href=\"#home\">Home</a></li>\n                <li><a href=\"#about\">About</a></li>\n                <li><a href=\"#contact\">Contact</a></li>\n            </ul>\n        </nav>\n    </header>\n    \n    <main>\n        <article>\n            <h2>About Me</h2>\n            <p>Hello! I'm a web developer passionate about creating amazing web experiences.</p>\n        </article>\n    </main>\n    \n    <footer>\n        <p>&copy; 2023 My Website. All rights reserved.</p>\n    </footer>\n</body>\n</html>",
            code_language="html",
            order=1
        )
        
        # CSS Content
        Content.objects.create(
            module=html_module,
            title="CSS3 Styling and Layout",
            description="Master CSS3 selectors, box model, and modern layout techniques",
            code="/* Modern CSS Reset */\n*, *::before, *::after {\n    box-sizing: border-box;\n    margin: 0;\n    padding: 0;\n}\n\n/* Variables and Custom Properties */\n:root {\n    --primary-color: #3498db;\n    --secondary-color: #2ecc71;\n    --text-color: #2c3e50;\n    --light-bg: #f5f6fa;\n}\n\n/* Modern Layout with Grid and Flexbox */\nbody {\n    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n    line-height: 1.6;\n    color: var(--text-color);\n    background-color: var(--light-bg);\n    padding: 2rem;\n}\n\n.container {\n    max-width: 1200px;\n    margin: 0 auto;\n    padding: 0 1rem;\n}\n\n/* Card Component */\n.card {\n    background: white;\n    border-radius: 8px;\n    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n    padding: 1.5rem;\n    margin-bottom: 1.5rem;\n    transition: transform 0.3s ease, box-shadow 0.3s ease;\n}\n\n.card:hover {\n    transform: translateY(-5px);\n    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);\n}\n\n/* Button Styles */\n.btn {\n    display: inline-block;\n    background: var(--primary-color);\n    color: white;\n    padding: 0.6rem 1.2rem;\n    border: none;\n    border-radius: 4px;\n    cursor: pointer;\n    font-size: 1rem;\n    text-decoration: none;\n    transition: background-color 0.3s ease;\n}\n\n.btn:hover {\n    background: #2980b9;\n}",
            code_language="css",
            order=2
        )

        # Module 2: JavaScript Fundamentals
        js_module = Module.objects.create(
            course=web_course,
            title="JavaScript Fundamentals",
            description="Master JavaScript programming from basics to advanced concepts",
            order=2
        )
        
        # JavaScript Content - Part 1
        Content.objects.create(
            module=js_module,
            title="Variables, Data Types, and Operators",
            description="Learn JavaScript variables, data types, and basic operators",
            code="// Variables and Constants\nlet name = 'John';          // String\nconst age = 30;             // Number\nlet isStudent = true;       // Boolean\nlet hobbies = ['reading', 'coding', 'music'];  // Array\nlet person = {              // Object\n    firstName: 'John',\n    lastName: 'Doe',\n    age: 30\n};\n\n// Template Literals\nconsole.log(`My name is ${name} and I'm ${age} years old.`);\n\n// Arrow Functions\nconst greet = (name) => {\n    return `Hello, ${name}!`;\n};\n\nconsole.log(greet('Alice')); // Hello, Alice!\n\n// Array Methods\nconst numbers = [1, 2, 3, 4, 5];\nconst doubled = numbers.map(num => num * 2);\nconsole.log(doubled); // [2, 4, 6, 8, 10]\n\n// Destructuring\nconst { firstName, lastName } = person;\nconsole.log(firstName, lastName); // John Doe",
            code_language="javascript",
            order=1
        )
        
        # JavaScript Content - Part 2
        Content.objects.create(
            module=js_module,
            title="Asynchronous JavaScript",
            description="Master async/await, promises, and fetch API",
            code="// Promises\nconst fetchData = () => {\n    return new Promise((resolve, reject) => {\n        // Simulate API call\n        setTimeout(() => {\n            const data = { id: 1, name: 'Sample Data' };\n            resolve(data);\n            // reject(new Error('Failed to fetch data'));\n        }, 1000);\n    });\n};\n\n// Using Promises with .then()\nfetchData()\n    .then(data => {\n        console.log('Data received:', data);\n        return data;\n    })\n    .catch(error => console.error('Error:', error));\n\n// Async/Await\nasync function getData() {\n    try {\n        const response = await fetch('https://api.example.com/data');\n        if (!response.ok) {\n            throw new Error('Network response was not ok');\n        }\n        const data = await response.json();\n        console.log('Data:', data);\n        return data;\n    } catch (error) {\n        console.error('Error fetching data:', error);\n    }\n}\n\n// Fetch API Example\nasync function fetchUsers() {\n    try {\n        const response = await fetch('https://jsonplaceholder.typicode.com/users');\n        const users = await response.json();\n        console.log('Users:', users);\n        // Process users data\n        displayUsers(users);\n    } catch (error) {\n        console.error('Error fetching users:', error);\n    }\n}\n\nfunction displayUsers(users) {\n    const container = document.getElementById('users-container');\n    container.innerHTML = users\n        .map(user => `\n            <div class=\"user-card\">\n                <h3>${user.name}</h3>\n                <p>Email: ${user.email}</p>\n                <p>Phone: ${user.phone}</p>\n            </div>\n        `)\n        .join('');\n}",
            code_language="javascript",
            order=2
        )

        # Module 3: React Fundamentals
        react_module = Module.objects.create(
            course=web_course,
            title="React.js Fundamentals",
            description="Learn to build interactive user interfaces with React",
            order=3
        )
        
        # React Content
        Content.objects.create(
            module=react_module,
            title="React Components and Props",
            description="Learn to create and use React components with props",
            code="import React from 'react';\nimport ReactDOM from 'react-dom/client';\n\n// Functional Component with Props\nfunction Welcome(props) {\n    return <h1>Hello, {props.name}!</h1>;\n}\n\n// Class Component\nclass Clock extends React.Component {\n    constructor(props) {\n        super(props);\n        this.state = { date: new Date() };\n    }\n\n    componentDidMount() {\n        this.timerID = setInterval(\n            () => this.tick(),\n            1000\n        );\n    }\n\n    componentWillUnmount() {\n        clearInterval(this.timerID);\n    }\n\n    tick() {\n        this.setState({\n            date: new Date()\n        });\n    }\n\n    render() {\n        return (\n            <div>\n                <h2>It is {this.state.date.toLocaleTimeString()}.</h2>\n            </div>\n        );\n    }\n}\n\n// App Component\nfunction App() {\n    return (\n        <div>\n            <Welcome name=\"Sara\" />\n            <Welcome name=\"Cahal\" />\n            <Welcome name=\"Edite\" />\n            <Clock />\n        </div>\n    );\n}\n\n// Render the App\nconst root = ReactDOM.createRoot(document.getElementById('root'));\nroot.render(<App />);",
            code_language="javascript",
            order=1
        )

        # Module 4: Node.js and Express
        node_module = Module.objects.create(
            course=web_course,
            title="Node.js and Express",
            description="Build server-side applications with Node.js and Express",
            order=4
        )
        
        # Node.js Content
        Content.objects.create(
            module=node_module,
            title="Building RESTful APIs with Express",
            description="Learn to create RESTful APIs using Express.js",
            code="const express = require('express');\nconst app = express();\nconst PORT = process.env.PORT || 3000;\n\n// Middleware\napp.use(express.json());\n\n// Sample data\nlet todos = [\n    { id: 1, title: 'Learn Node.js', completed: false },\n    { id: 2, title: 'Build a REST API', completed: false },\n    { id: 3, title: 'Deploy to production', completed: false }\n];\n\n// GET all todos\napp.get('/api/todos', (req, res) => {\n    res.json(todos);\n});\n\n// GET a single todo\napp.get('/api/todos/:id', (req, res) => {\n    const todo = todos.find(t => t.id === parseInt(req.params.id));\n    if (!todo) return res.status(404).json({ message: 'Todo not found' });\n    res.json(todo);\n});\n\n// POST a new todo\napp.post('/api/todos', (req, res) => {\n    const { title } = req.body;\n    if (!title) {\n        return res.status(400).json({ message: 'Title is required' });\n    }\n    \n    const newTodo = {\n        id: todos.length + 1,\n        title,\n        completed: false\n    };\n    \n    todos.push(newTodo);\n    res.status(201).json(newTodo);\n});\n\n// Start the server\napp.listen(PORT, () => {\n    console.log(`Server is running on http://localhost:${PORT}`);\n});",
            code_language="javascript",
            order=1
        )

        # Module 5: Database Integration
        db_module = Module.objects.create(
            course=web_course,
            title="Database Integration",
            description="Learn to work with SQL and NoSQL databases",
            order=5
        )
        
        # Database Content - MongoDB with Mongoose
        Content.objects.create(
            module=db_module,
            title="MongoDB with Mongoose",
            description="Learn to use MongoDB with Mongoose ODM",
            code="const mongoose = require('mongoose');\n\n// Connect to MongoDB\nmongoose.connect('mongodb://localhost:27017/techforge', {\n    useNewUrlParser: true,\n    useUnifiedTopology: true\n})\n.then(() => console.log('Connected to MongoDB'))\n.catch(err => console.error('Could not connect to MongoDB:', err));\n\n// Define a schema\nconst userSchema = new mongoose.Schema({\n    name: {\n        type: String,\n        required: true,\n        minlength: 3,\n        maxlength: 50\n    },\n    email: {\n        type: String,\n        required: true,\n        unique: true,\n        match: /^[^\s@]+@[^\s@]+\.[^\s@]+$/\n    },\n    password: {\n        type: String,\n        required: true,\n        minlength: 8\n    },\n    isAdmin: {\n        type: Boolean,\n        default: false\n    },\n    createdAt: {\n        type: Date,\n        default: Date.now\n    }\n});\n\n// Create a model\nconst User = mongoose.model('User', userSchema);\n\n// Create a new user\nasync function createUser(userData) {\n    const user = new User(userData);\n    try {\n        const result = await user.save();\n        console.log('User created:', result);\n        return result;\n    } catch (error) {\n        console.error('Error creating user:', error.message);\n        throw error;\n    }\n}\n\n// Find users\nasync function getUsers() {\n    try {\n        const users = await User.find().sort('name');\n        console.log('Users:', users);\n        return users;\n    } catch (error) {\n        console.error('Error fetching users:', error.message);\n        throw error;\n    }\n}\n\n// Update a user\nasync function updateUser(userId, updates) {\n    try {\n        const user = await User.findByIdAndUpdate(\n            userId,\n            { $set: updates },\n            { new: true }\n        );\n        if (!user) {\n            console.error('User not found');\n            return null;\n        }\n        console.log('User updated:', user);\n        return user;\n    } catch (error) {\n        console.error('Error updating user:', error.message);\n        throw error;\n    }\n}\n\n// Example usage\n// createUser({ name: 'John Doe', email: 'john@example.com', password: 'password123' });\n// getUsers();\n// updateUser('user-id-here', { name: 'John Smith' });",
            code_language="javascript",
            order=1
        )

        # Module 6: Authentication & Authorization
        auth_module = Module.objects.create(
            course=web_course,
            title="Authentication & Authorization",
            description="Implement secure user authentication and authorization",
            order=6
        )
        
        # Auth Content - JWT Authentication
        Content.objects.create(
            module=auth_module,
            title="JWT Authentication",
            description="Implement JWT authentication in a Node.js/Express app",
            code="const express = require('express');\nconst jwt = require('jsonwebtoken');\nconst bcrypt = require('bcryptjs');\nconst { User } = require('../models/user');\nconst auth = require('../middleware/auth');\n\nconst router = express.Router();\n\n// Register a new user\nrouter.post('/register', async (req, res) => {\n    try {\n        // Check if user already exists\n        let user = await User.findOne({ email: req.body.email });\n        if (user) {\n            return res.status(400).json({ message: 'User already exists' });\n        }\n\n        // Create new user\n        user = new User({\n            name: req.body.name,\n            email: req.body.email,\n            password: req.body.password\n        });\n\n        // Hash password\n        const salt = await bcrypt.genSalt(10);\n        user.password = await bcrypt.hash(user.password, salt);\n\n        // Save user to database\n        await user.save();\n\n        // Generate JWT token\n        const token = jwt.sign(\n            { userId: user._id, isAdmin: user.isAdmin },\n            process.env.JWT_SECRET || 'your-secret-key',\n            { expiresIn: '24h' }\n        );\n\n        res.status(201).json({ token });\n    } catch (error) {\n        console.error('Registration error:', error);\n        res.status(500).json({ message: 'Server error' });\n    }\n});\n\n// Login user\nrouter.post('/login', async (req, res) => {\n    try {\n        // Check if user exists\n        const user = await User.findOne({ email: req.body.email });\n        if (!user) {\n            return res.status(400).json({ message: 'Invalid credentials' });\n        }\n\n        // Validate password\n        const isMatch = await bcrypt.compare(req.body.password, user.password);\n        if (!isMatch) {\n            return res.status(400).json({ message: 'Invalid credentials' });\n        }\n\n        // Generate JWT token\n        const token = jwt.sign(\n            { userId: user._id, isAdmin: user.isAdmin },\n            process.env.JWT_SECRET || 'your-secret-key',\n            { expiresIn: '24h' }\n        );\n\n        res.json({ token });\n    } catch (error) {\n        console.error('Login error:', error);\n        res.status(500).json({ message: 'Server error' });\n    }\n});\n\n// Get current user (protected route)\nrouter.get('/me', auth, async (req, res) => {\n    try {\n        const user = await User.findById(req.user.userId).select('-password');\n        res.json(user);\n    } catch (error) {\n        console.error('Get user error:', error);\n        res.status(500).json({ message: 'Server error' });\n    }\n});\n\nmodule.exports = router;\n\n// auth.js (Middleware)\nconst jwt = require('jsonwebtoken');\n\nmodule.exports = function(req, res, next) {\n    // Get token from header\n    const token = req.header('x-auth-token');\n\n    // Check if no token\n    if (!token) {\n        return res.status(401).json({ message: 'No token, authorization denied' });\n    }\n\n    // Verify token\n    try {\n        const decoded = jwt.verify(token, process.env.JWT_SECRET || 'your-secret-key');\n        req.user = decoded;\n        next();\n    } catch (error) {\n        res.status(401).json({ message: 'Token is not valid' });\n    }\n};",
            code_language="javascript",
            order=1
        )

        # Module 7: Deployment and DevOps
        deploy_module = Module.objects.create(
            course=web_course,
            title="Deployment and DevOps",
            description="Learn to deploy web applications with CI/CD pipelines",
            order=7
        )
        
        # Deployment Content - Docker and Kubernetes
        Content.objects.create(
            module=deploy_module,
            title="Docker and Kubernetes",
            description="Containerize and orchestrate your applications",
            code="# Dockerfile for a Node.js application\nFROM node:16-alpine\n\n# Create app directory\nWORKDIR /usr/src/app\n\n# Install app dependencies\nCOPY package*.json ./\nRUN npm install\n\n# Bundle app source\nCOPY . .\n\n# Expose port\nEXPOSE 3000\n\n# Start the application\nCMD [ \"node\", \"server.js\" ]\n\n# docker-compose.yml\nversion: '3.8'\nservices:\n  web:\n    build: .\n    ports:\n      - '3000:3000'\n    environment:\n      - NODE_ENV=production\n      - MONGODB_URI=mongodb://mongo:27017/techforge\n    depends_on:\n      - mongo\n  \n  mongo:\n    image: mongo:5.0\n    volumes:\n      - mongodb_data:/data/db\n    ports:\n      - '27017:27017'\n\nvolumes:\n  mongodb_data:\n\n# Kubernetes Deployment (deployment.yaml)\napiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: web-app\nspec:\n  replicas: 3\n  selector:\n    matchLabels:\n      app: web-app\n  template:\n    metadata:\n      labels:\n        app: web-app\n    spec:\n      containers:\n      - name: web-app\n        image: your-username/web-app:latest\n        ports:\n        - containerPort: 3000\n        env:\n        - name: NODE_ENV\n          value: production\n        - name: MONGODB_URI\n          value: \"mongodb://mongo:27017/techforge\"\n---\napiVersion: v1\nkind: Service\nmetadata:\n  name: web-app\nspec:\n  selector:\n    app: web-app\n  ports:\n  - protocol: TCP\n    port: 80\n    targetPort: 3000\n  type: LoadBalancer",
            code_language="yaml",
            order=1
        )

        # ===== COURSE 2: Data Science with Python =====
        ds_course = Course.objects.create(
            title="Data Science with Python",
            slug="data-science-python",
            description="Master data analysis, visualization, and machine learning with Python",
            difficulty="Intermediate",
            estimated_duration=180,
            instructor=instructor,
            price=249.99
        )

        # Data Science Modules...
        # (Similar structure as web development course)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample courses and content!'))