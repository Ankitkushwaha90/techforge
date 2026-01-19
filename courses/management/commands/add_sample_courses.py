from django.core.management.base import BaseCommand
from courses.models import Course, Module, Content

def create_course_with_modules():
    # 1. Cybersecurity Course - Expanded
    cyber_course, _ = Course.objects.get_or_create(
        title="Cybersecurity Professional",
        defaults={
            'description': 'Comprehensive training in cybersecurity including ethical hacking, network defense, and security analysis.'
        }
    )

    # Cybersecurity Modules - Expanded
    cyber_modules = [
        {
            'title': 'Cybersecurity Fundamentals',
            'description': 'Core concepts and principles of cybersecurity',
            'order': 1,
            'contents': [
                {
                    'title': 'Security Principles',
                    'content': 'CIA Triad: Confidentiality, Integrity, and Availability. Defense in depth, least privilege, and zero trust models.',
                    'content_type': 'text',
                    'order': 1
                },
                {
                    'title': 'Threat Landscape',
                    'content': 'Malware, phishing, DDoS, APTs, insider threats, and emerging attack vectors.',
                    'content_type': 'text',
                    'order': 2
                },
                {
                    'title': 'Security Policies',
                    'content': 'Developing and implementing effective security policies and procedures.',
                    'content_type': 'text',
                    'order': 3
                }
            ]
        },
        {
            'title': 'Network Security',
            'description': 'Securing network infrastructure and communications',
            'order': 2,
            'contents': [
                {
                    'title': 'Firewall Configuration',
                    'content': 'Configuring and managing firewalls (iptables, pfSense, Cisco ASA)',
                    'content_type': 'text',
                    'code': '# Example iptables rule\nsudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # Allow SSH\nsudo iptables -A INPUT -j DROP  # Default deny',
                    'language': 'bash',
                    'order': 1
                },
                {
                    'title': 'VPN Implementation',
                    'content': 'Setting up secure VPN connections (OpenVPN, WireGuard)',
                    'content_type': 'text',
                    'code': '# Basic WireGuard server config\n[Interface]\nPrivateKey = [PRIVATE_KEY]\nAddress = 10.0.0.1/24\nListenPort = 51820',
                    'language': 'ini',
                    'order': 2
                }
            ]
        },
        {
            'title': 'Ethical Hacking',
            'description': 'Penetration testing and vulnerability assessment',
            'order': 3,
            'contents': [
                {
                    'title': 'Kali Linux Tools',
                    'content': 'Using Metasploit, Nmap, Burp Suite, and other security tools.',
                    'content_type': 'text',
                    'code': '# Basic Nmap scan\nnmap -sV -sC -p- 192.168.1.1',
                    'language': 'bash',
                    'order': 1
                }
            ]
        }
    ]

    # 2. IoT Course - Expanded
    iot_course, _ = Course.objects.get_or_create(
        title="IoT Development & Security",
        defaults={
            'description': 'End-to-end IoT development with a focus on security and real-world applications.'
        }
    )

    # IoT Modules - Expanded
    iot_modules = [
        {
            'title': 'IoT Architecture',
            'description': 'Understanding IoT system components and architecture',
            'order': 1,
            'contents': [
                {
                    'title': 'IoT Stack',
                    'content': 'Device layer, communication protocols, cloud platforms, and applications.',
                    'content_type': 'text',
                    'order': 1
                },
                {
                    'title': 'Sensors and Actuators',
                    'content': 'Working with common IoT sensors (DHT22, PIR, ultrasonic) and actuators.',
                    'content_type': 'text',
                    'code': '// Reading from DHT22 sensor\n#include <DHT.h>\n#define DHTPIN 2\n#define DHTTYPE DHT22\nDHT dht(DHTPIN, DHTTYPE);\n\nvoid setup() {\n  Serial.begin(9600);\n  dht.begin();\n}\n\nvoid loop() {\n  float h = dht.readHumidity();\n  float t = dht.readTemperature();\n  Serial.print("Humidity: ");\n  Serial.print(h);\n  Serial.print(" %\tTemperature: ");\n  Serial.print(t);\n  Serial.println(" °C");\n  delay(2000);\n}',
                    'language': 'cpp',
                    'order': 2
                }
            ]
        },
        {
            'title': 'IoT Security',
            'description': 'Securing IoT devices and communications',
            'order': 2,
            'contents': [
                {
                    'title': 'Secure Device Provisioning',
                    'content': 'Secure boot, device identity, and authentication mechanisms.',
                    'content_type': 'text',
                    'order': 1
                },
                {
                    'title': 'Encryption in IoT',
                    'content': 'Implementing TLS/DTLS for secure communication.',
                    'content_type': 'text',
                    'code': '// Example MQTT with TLS in Python\nimport paho.mqtt.client as mqtt\nimport ssl\n\nclient = mqtt.Client()\nclient.tls_set(ca_certs="ca.crt",\n               certfile="client.crt",\n               keyfile="client.key",\n               cert_reqs=ssl.CERT_REQUIRED,\n               tls_version=ssl.PROTOCOL_TLSv1_2)\nclient.connect("mqtt.example.com", 8883, 60)\nclient.publish("sensors/temperature", "25.5")',
                    'language': 'python',
                    'order': 2
                }
            ]
        },
        {
            'title': 'Edge Computing',
            'description': 'Processing data at the edge with IoT devices',
            'order': 3,
            'contents': [
                {
                    'title': 'TinyML',
                    'content': 'Running machine learning models on microcontrollers.',
                    'content_type': 'text',
                    'order': 1
                }
            ]
        }
    ]

    # 3. Data Science Course - Expanded
    ds_course, _ = Course.objects.get_or_create(
        title="Data Science & Machine Learning Professional",
        defaults={
            'description': 'Master data analysis, visualization, and machine learning with Python and modern tools.'
        }
    )

    # Data Science Modules - Expanded
    ds_modules = [
        {
            'title': 'Data Analysis with Python',
            'description': 'Data manipulation and analysis using Python',
            'order': 1,
            'contents': [
                {
                    'title': 'Pandas Mastery',
                    'content': 'Data manipulation with Pandas DataFrames',
                    'content_type': 'text',
                    'code': 'import pandas as pd\nimport numpy as np\n\n# Create sample data\ndata = {\'Name\': [\'Alice\', \'Bob\', \'Charlie\'],\n        \'Age\': [25, 30, 35],\n        \'City\': [\'New York\', \'London\', \'Paris\']}\n\ndf = pd.DataFrame(data)\n\n# Basic operations\nprint(df[df[\'Age\'] > 30])  # Filtering\nprint(df.groupby(\'City\').mean())  # Grouping',
                    'language': 'python',
                    'order': 1
                },
                {
                    'title': 'Data Visualization',
                    'content': 'Creating visualizations with Matplotlib and Seaborn',
                    'content_type': 'text',
                    'code': 'import matplotlib.pyplot as plt\nimport seaborn as sns\nimport numpy as np\n\n# Sample data\nx = np.linspace(0, 10, 100)\ny = np.sin(x)\n\n# Create plot\nplt.figure(figsize=(10, 6))\nplt.plot(x, y, label=\'Sine Wave\')\nplt.title(\'Sample Plot\')\nplt.xlabel(\'X-axis\')\nplt.ylabel(\'Y-axis\')\nplt.legend()\nplt.grid(True)\nplt.show()',
                    'language': 'python',
                    'order': 2
                }
            ]
        },
        {
            'title': 'Machine Learning',
            'description': 'Supervised and unsupervised learning techniques',
            'order': 2,
            'contents': [
                {
                    'title': 'Model Training with Scikit-learn',
                    'content': 'Building and evaluating machine learning models',
                    'content_type': 'text',
                    'code': 'from sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score\nimport pandas as pd\n\n# Sample data\ndata = pd.read_csv(\'data.csv\')\nX = data.drop(\'target\', axis=1)\ny = data[\'target\']\n\n# Split data\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n\n# Train model\nmodel = RandomForestClassifier()\nmodel.fit(X_train, y_train)\n\n# Evaluate\npredictions = model.predict(X_test)\nprint(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")',
                    'language': 'python',
                    'order': 1
                },
                {
                    'title': 'Neural Networks with TensorFlow',
                    'content': 'Building deep learning models',
                    'content_type': 'text',
                    'code': 'import tensorflow as tf\nfrom tensorflow.keras import layers, models\nimport numpy as np\n\n# Sample data\n(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()\ntrain_images = train_images.reshape((60000, 28, 28, 1)).astype(\'float32\') / 255\ntest_images = test_images.reshape((10000, 28, 28, 1)).astype(\'float32\') / 255\n\n# Create a simple CNN\nmodel = models.Sequential([\n    layers.Conv2D(32, (3, 3), activation=\'relu\', input_shape=(28, 28, 1)),\n    layers.MaxPooling2D((2, 2)),\n    layers.Flatten(),\n    layers.Dense(64, activation=\'relu\'),\n    layers.Dense(10, activation=\'softmax\')\n])\n\n# Compile model\nmodel.compile(optimizer=\'adam\',\n              loss=\'sparse_categorical_crossentropy\',\n              metrics=[\'accuracy\'])\n\n# Train model\nmodel.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))',
                    'language': 'python',
                    'order': 2
                }
            ]
        }
    ]

    # 4. AI Courses - Expanded
    ai_courses = [
        {
            'title': 'Generative AI Engineering',
            'description': 'Master advanced generative models and their applications',
            'modules': [
                {
                    'title': 'GANs in Depth',
                    'description': 'Advanced topics in Generative Adversarial Networks',
                    'order': 1,
                    'contents': [
                        {
                            'title': 'DCGAN Implementation',
                            'content': 'Building a Deep Convolutional GAN with PyTorch',
                            'content_type': 'text',
                            'code': 'import torch\nimport torch.nn as nn\nimport torch.optim as optim\n\n# Generator\nclass Generator(nn.Module):\n    def __init__(self):\n        super(Generator, self).__init__()\n        self.main = nn.Sequential(\n            nn.ConvTranspose2d(100, 512, 4, 1, 0, bias=False),\n            nn.BatchNorm2d(512),\n            nn.ReLU(True),\n            # ... more layers ...\n            nn.Tanh()\n        )\n\n# Training loop\ndef train_gan(generator, discriminator, dataloader, num_epochs=50):\n    criterion = nn.BCELoss()\n    optimizer_g = optim.Adam(generator.parameters(), lr=0.0002)\n    # ... training code ...',
                            'language': 'python',
                            'order': 1
                        }
                    ]
                },
                {
                    'title': 'Diffusion Models',
                    'description': 'Understanding and implementing diffusion models',
                    'order': 2,
                    'contents': [
                        {
                            'title': 'Denoising Diffusion Models',
                            'content': 'Implementing a basic diffusion model',
                            'content_type': 'text',
                            'order': 1
                        }
                    ]
                }
            ]
        },
        {
            'title': 'Agentic AI Systems',
            'description': 'Designing and deploying autonomous AI agents',
            'modules': [
                {
                    'title': 'Multi-Agent Systems',
                    'description': 'Designing systems with multiple interacting agents',
                    'order': 1,
                    'contents': [
                        {
                            'title': 'Agent Architectures',
                            'content': 'Design patterns for agent-based systems',
                            'content_type': 'text',
                            'code': 'class Agent:\n    def __init__(self, agent_id):\n        self.agent_id = agent_id\n        self.knowledge = {}\n    \n    def perceive(self, environment):\n        # Process environment state\n        pass\n    \n    def act(self):\n        # Decide on action\n        pass\n\n# Multi-agent system\nclass MultiAgentSystem:\n    def __init__(self, num_agents):\n        self.agents = [Agent(i) for i in range(num_agents)]\n    \n    def run_simulation(self, steps):\n        for _ in range(steps):\n            for agent in self.agents:\n                agent.act()',
                            'language': 'python',
                            'order': 1
                        }
                    ]
                },
                {
                    'title': 'Reinforcement Learning for Agents',
                    'description': 'Training agents using reinforcement learning',
                    'order': 2,
                    'contents': [
                        {
                            'title': 'Q-Learning Implementation',
                            'content': 'Building a simple Q-learning agent',
                            'content_type': 'text',
                            'code': 'import numpy as np\n\nclass QLearningAgent:\n    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.99, epsilon=0.1):\n        self.q_table = np.zeros((n_states, n_actions))\n        self.alpha = alpha  # Learning rate\n        self.gamma = gamma  # Discount factor\n        self.epsilon = epsilon  # Exploration rate\n    \n    def choose_action(self, state):\n        if np.random.random() < self.epsilon:\n            return np.random.randint(0, self.q_table.shape[1])\n        return np.argmax(self.q_table[state])\n    \n    def learn(self, state, action, reward, next_state, done):\n        # Q-learning update rule\n        old_value = self.q_table[state, action]\n        next_max = np.max(self.q_table[next_state])\n        \n        if done:\n            target = reward\n        else:\n            target = reward + self.gamma * next_max\n        \n        self.q_table[state, action] = (1 - self.alpha) * old_value + self.alpha * target',
                            'language': 'python',
                            'order': 1
                        }
                    ]
                }
            ]
        },
        {
            'title': 'LLM Application Development',
            'description': 'Building applications with large language models',
            'modules': [
                {
                    'title': 'Prompt Engineering',
                    'description': 'Designing effective prompts for LLMs',
                    'order': 1,
                    'contents': [
                        {
                            'title': 'Advanced Prompt Patterns',
                            'content': 'Techniques for better LLM responses',
                            'content_type': 'text',
                            'code': 'from openai import OpenAI\n\nclient = OpenAI()\n\ndef get_llm_response(prompt, system_prompt=None):\n    messages = []\n    if system_prompt:\n        messages.append({"role": "system", "content": system_prompt})\n    messages.append({"role": "user", "content": prompt})\n    \n    response = client.chat.completions.create(\n        model="gpt-4",\n        messages=messages,\n        temperature=0.7,\n        max_tokens=1000\n    )\n    return response.choices[0].message.content\n\n# Example usage\nresponse = get_llm_response(\n    prompt="Explain quantum computing in simple terms.",\n    system_prompt="You are a helpful AI assistant that explains complex topics simply."\n)',
                            'language': 'python',
                            'order': 1
                        }
                    ]
                },
                {
                    'title': 'RAG Systems',
                    'description': 'Retrieval-Augmented Generation',
                    'order': 2,
                    'contents': [
                        {
                            'title': 'Building a RAG Pipeline',
                            'content': 'Implementing retrieval-augmented generation',
                            'content_type': 'text',
                            'order': 1
                        }
                    ]
                }
            ]
        }
    ]

    # Function to create modules and contents
    def create_modules(course, modules_data):
        for module_data in modules_data:
            module = Module.objects.create(
                course=course,
                title=module_data['title'],
                description=module_data['description'],
                order=module_data['order']
            )
            
            for content_data in module_data.get('contents', []):
                content = Content(
                    module=module,
                    title=content_data['title'],
                    description=content_data.get('content', ''),
                    code=content_data.get('code', ''),
                    code_language=content_data.get('language', 'python'),
                    order=content_data['order']
                )
                content.save()

    # Create all courses and their modules
    create_modules(cyber_course, cyber_modules)
    create_modules(iot_course, iot_modules)
    create_modules(ds_course, ds_modules)
    
    for ai_course_data in ai_courses:
        course, _ = Course.objects.get_or_create(
            title=ai_course_data['title'],
            defaults={'description': ai_course_data['description']}
        )
        create_modules(course, ai_course_data['modules'])

class Command(BaseCommand):
    help = 'Adds sample courses, modules, and content to the database'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample courses and content...')
        create_course_with_modules()
        self.stdout.write(self.style.SUCCESS('Successfully created sample courses and content!'))
