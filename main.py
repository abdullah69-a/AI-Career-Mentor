

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
from pydantic import BaseModel
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# Aik hi baar app initialize karein
app = FastAPI()

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model Load karein
try:
    model = pickle.load(open('best_model.pkl', 'rb'))
except FileNotFoundError:
    print("Error: 'best_model.pkl' nahi mili!")

ROADMAPS_DATA = {
    "AI Engineer": {
        "title": "Artificial Intelligence Specialist",
        "duration": "6 Months",
        "overview": "Master Neural Networks and Generative AI.",
        "monthly_plan": ["Month 1: Foundations", "Month 2: Deep Learning", "Month 3: Computer Vision", "Month 4: NLP", "Month 5: GenAI", "Month 6: Deployment"],
        "essential_tools": ["PyTorch", "TensorFlow", "HuggingFace"],
        "resources": "DeepLearning.ai, Fast.ai"
    },
    "Data Scientist": {
        "title": "Data Science Expert",
        "duration": "6 Months",
        "overview": "Extract insights from data using ML.",
        "monthly_plan": ["Month 1: Pandas/NumPy", "Month 2: EDA", "Month 3: Classical ML", "Month 4: XGBoost", "Month 5: SQL", "Month 6: Projects"],
        "essential_tools": ["Jupyter", "Scikit-Learn", "Pandas"],
        "resources": "Kaggle, StatQuest"
    },
    "Web Developer": {
        "title": "Full-Stack Developer (MERN)",
        "duration": "5 Months",
        "overview": "Build modern web applications.",
        "monthly_plan": ["Month 1: HTML/CSS", "Month 2: JS", "Month 3: React", "Month 4: Node.js", "Month 5: DevOps"],
        "essential_tools": ["VS Code", "GitHub", "Postman"],
        "resources": "FreeCodeCamp, MDN"
    },
    
    "Cloud Engineer": {
        "title": "Cloud Infrastructure & Solutions Architect",
        "duration": "5 Months",
        "overview": "Design and manage scalable infrastructure on AWS/Azure.",
        "monthly_plan": [
            "Month 1: Networking (VPC, Subnets, DNS, Load Balancers)",
            "Month 2: Compute & Storage (EC2, S3, Lambda, EBS)",
            "Month 3: Identity & Security (IAM, Security Groups, Encryption)",
            "Month 4: IaC (Terraform Basics, CloudFormation)",
            "Month 5: Serverless & Auto-scaling (K8s basics, CloudWatch)"
        ],
        "essential_tools": ["AWS Console", "Terraform", "CLI", "Docker"],
        "resources": "AWS Cloud Practitioner, Adrian Cantrill, CloudGuru"
    },
    "Cyber Security Analyst": {
        "title": "Information Security & Ethical Hacking Specialist",
        "duration": "6 Months",
        "overview": "Protect systems from threats using defensive and offensive tactics.",
        "monthly_plan": [
            "Month 1: Networking (OSI Model, TCP/IP, Wireshark)",
            "Month 2: Linux & Scripting (Bash, Python for Security)",
            "Month 3: Vulnerability Assessment (Nmap, SQL Injection, XSS)",
            "Month 4: Offensive Security (Metasploit, Burp Suite, Pentesting)",
            "Month 5: Defensive Security (SIEM, Incident Response, Log Analysis)",
            "Month 6: Compliance (ISO 27001, GDPR, NIST Framework)"
        ],
        "essential_tools": ["Kali Linux", "Wireshark", "Metasploit", "Burp Suite"],
        "resources": "TryHackMe, HackTheBox, CompTIA Security+"
    },
    "DevOps Engineer": {
        "title": "CI/CD & Automation Specialist",
        "duration": "6 Months",
        "overview": "Automate development and operations using modern tools.",
        "monthly_plan": [
            "Month 1: Linux Mastery & Shell Scripting",
            "Month 2: Version Control & CI/CD (GitHub Actions, Jenkins)",
            "Month 3: Containerization (Docker Images & Networking)",
            "Month 4: Orchestration (Kubernetes: Pods, Services, Helm)",
            "Month 5: Monitoring (Prometheus, Grafana, ELK Stack)",
            "Month 6: IaC & Config Management (Terraform, Ansible)"
        ],
        "essential_tools": ["Docker", "Kubernetes", "Jenkins", "Ansible", "Terraform"],
        "resources": "KodeKloud, Nana (YouTube), DevOps Roadmap"
    },
    "Software Engineer": {
        "title": "Professional Software Developer (Core Engineering)",
        "duration": "6 Months",
        "overview": "Focus on high-quality code and system architecture.",
        "monthly_plan": [
            "Month 1: Advanced DSA (Trees, Graphs, DP, Complexity)",
            "Month 2: OOP & SOLID Principles (Design Patterns)",
            "Month 3: DB Design (Normalization, Indexing, ACID)",
            "Month 4: System Design (Microservices, Caching, Scaling)",
            "Month 5: Testing (Unit, Integration, Swagger Documentation)",
            "Month 6: SDLC (Agile/Scrum, Code Reviews, Git Flow)"
        ],
        "essential_tools": ["VS Code", "Git", "Docker", "Postman", "JUnit"],
        "resources": "LeetCode, NeetCode, System Design Primer"
    },
    "Database Administrator": {
        "title": "Database Management & Optimization Expert",
        "duration": "4 Months",
        "overview": "Manage, secure, and tune high-performance databases.",
        "monthly_plan": [
            "Month 1: Advanced SQL (Stored Procs, Triggers, Joins)",
            "Month 2: Admin (Installation, Backup & Recovery)",
            "Month 3: Performance Tuning (Execution Plans, Indexing)",
            "Month 4: High Availability (Replication, Clustering, NoSQL)"
        ],
        "essential_tools": ["MySQL", "PostgreSQL", "MongoDB", "pgAdmin"],
        "resources": "Oracle University, SQLZoo, Brent Ozar"
    }

    # Baqi roles bhi isi format mein add karein...
}

roles_map = {0: "AI Engineer", 1: "Cloud Engineer", 2: "Cyber Security Analyst", 3: "Data Scientist", 
             4: "Database Administrator", 5: "DevOps Engineer", 6: "Software Engineer", 7: "Web Developer"}

class StudentData(BaseModel):
    Python: int
    SQL: int
    Statistics: int
    MachineLearning: int
    HTML_CSS: int
    JavaScript: int
    Cloud: int
    ProblemSolving: int
    Communication: int
    Creativity: int
    CGPA: float
    Interest_AI: int
    Interest_Cloud: int
    Interest_Data: int
    Interest_Database: int
    Interest_Development: int
    Interest_Security: int

@app.post("/predict")
def predict(data: StudentData):
    input_features = [data.Python, data.SQL, data.Statistics, data.MachineLearning, data.HTML_CSS, 
                      data.JavaScript, data.Cloud, data.ProblemSolving, data.Communication, 
                      data.Creativity, data.CGPA, data.Interest_AI, data.Interest_Cloud, 
                      data.Interest_Data, data.Interest_Database, data.Interest_Development, 
                      data.Interest_Security]
    
    prediction_num = int(model.predict([input_features])[0])
    final_role = roles_map.get(prediction_num, "Web Developer") # Default role agar model fail ho
    
    info = ROADMAPS_DATA.get(final_role, ROADMAPS_DATA["Web Developer"])
    
    # Ye structure Frontend ke liye perfect hai
    return {
        "predicted_role": final_role,
        "roadmap_details": info
    }


