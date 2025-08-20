from flask import Flask, render_template

app = Flask(__name__)

# ===== Data Section =====

summary = ("Aspiring DevOps Engineer with hands-on experience in cloud platforms (AWS), "
           "CI/CD pipelines, and containerized deployments. Skilled in automation, scripting, "
           "and infrastructure management through academic projects and self-driven practice. "
           "Strong problem-solving mindset with a focus on scalability, monitoring, and collaboration.")

skills = [
    "AWS (EC2, S3, IAM, Cognito)",
    "Docker & Kubernetes (EKS basics)",
    "CI/CD – GitHub Actions, Jenkins",
    "Automation: Python, Bash, n8n workflows, Linux",
    "Version Control: Git, GitHub",
    "System Monitoring: Netdata",
    "Programming: Python, C, C++, HTML"
]

projects = [
    {
        "title": "QuickNotes Web App – DevOps Deployment (2025)",
        "desc": "Containerized a Vite + Tailwind + TypeScript app using Docker. Deployed on AWS EC2 via GitHub Actions CI/CD. Integrated AWS S3 for storage & Cognito for authentication."
    },
    {
        "title": "Monitoring EC2 Instance with Netdata (2025)",
        "desc": "Configured Netdata on AWS EC2 to collect system metrics. Analyzed logs and strengthened understanding of infrastructure monitoring & alerting workflows."
    },
    {
        "title": "CI/CD Pipeline Practice – Sample App (2025)",
        "desc": "Built a Jenkins pipeline for automated build, test, and deployment of a Node.js app. Deployed containerized app on AWS EC2 with Docker."
    }
]

tasks_learnings = [
    "Practiced GitHub Actions workflows for CI/CD automation",
    "Learned fundamentals of cloud infrastructure setup with AWS EC2 and IAM",
    "Explored container orchestration with Minikube and Kubernetes basics",
    "Developed automation scripts using Bash",
    "Built small workflows with n8n for process automation"
]

internship = {
    "title": "APSSDC Summer Internship – DevOps & Cloud (2025)",
    "desc": ("Successfully completed Summer Online Internship Program focused on DevOps and Cloud practices, "
             "conducted by APSSDC (Andhra Pradesh State Skill Development Corporation), Department of Skills Development & Training, "
             "Government of Andhra Pradesh.")
}

education = [
    {"degree": "B.Tech in Electrical and Electronics Engineering",
     "inst": "Rajiv Gandhi University of Knowledge Technologies – Ongole",
     "years": "2022–2026",
     "cgpa": "7.7"},
    {"degree": "Pre University Course (MPC Stream)",
     "inst": "Rajiv Gandhi University of Knowledge Technologies – Ongole",
     "years": "2020–2022",
     "cgpa": "8.7"},
    {"degree": "SSC",
     "inst": "Kamala Concept School – Markapur",
     "years": "2020",
     "cgpa": None}
]

contacts = {
    "email": "venkatapathirajupadidapu@gmail.com",
    "phone": "+91 7288821934",
    "location": "Andhra Pradesh, India",
    "github": "https://github.com/raju200539",
    "linkedin": "https://linkedin.com/in/rajupadidapu"
}

# ===== Routes =====

@app.route("/")
def home():
    return render_template("index.html", 
                           summary=summary, 
                           skills=skills, 
                           projects=projects,
                           tasks_learnings=tasks_learnings, 
                           internship=internship,
                           education=education, 
                           contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
