from sqlalchemy.orm import Session
from app.models.models import User, Company, Job, UserRole
from app.core.security import hash_password

sample_jobs = [
    ("Python Backend Developer", "Build scalable APIs using FastAPI and PostgreSQL.", "Python, FastAPI, SQL, Git", "Hyderabad", "Full Time", "Fresher", "Backend", 400000, 800000, False),
    ("React Frontend Developer", "Create modern responsive interfaces for job seekers.", "React, JavaScript, CSS, REST APIs", "Bangalore", "Full Time", "Junior", "Frontend", 500000, 900000, True),
    ("AI Engineer Intern", "Work on AI features like resume scoring and recommendations.", "Python, ML basics, LLMs, APIs", "Hyderabad", "Internship", "Fresher", "AI/ML", 200000, 400000, False),
    ("Full Stack Developer", "Develop end-to-end product features across frontend and backend.", "React, FastAPI, PostgreSQL", "Pune", "Full Time", "Junior", "Full Stack", 600000, 1200000, True),
    ("Data Engineer", "Build ETL pipelines and data models for analytics.", "Python, SQL, PostgreSQL, Spark basics", "Chennai", "Full Time", "Junior", "Data", 500000, 1000000, False),
]

def seed_data(db: Session):
    if db.query(User).first():
        return

    admin = User(name="Admin User", email="admin@jobboard.com", hashed_password=hash_password("admin123"))
    recruiter = User(name="Priya Recruiter", email="recruiter@jobboard.com", hashed_password=hash_password("admin123"))
    candidate = User(name="Charan Candidate", email="candidate@jobboard.com", hashed_password=hash_password("admin123"))
    
    db.add_all([admin, recruiter, candidate])
    db.commit()
    db.refresh(recruiter)

    company = Company(
        name="GlobalCo Technologies",
        description="A product engineering company hiring full-stack and AI talent.",
        website="https://globalco.com",
        location="Hitech City, Hyderabad",
        industry="Software Engineering",
        logo_url="https://dummyimage.com/120x120/2563eb/ffffff&text=G",
        owner_id=recruiter.id,
    )
    db.add(company)
    db.commit()
    db.refresh(company)

    for title, desc, req, loc, jt, exp, cat, smin, smax, remote in sample_jobs:
        db.add(Job(
            title=title,
            description=desc,
            requirements=req,
            responsibilities="Design, build, test, document, and deploy high-quality application features.",
            location=loc,
            job_type=jt,
            experience_level=exp,
            category=cat,
            salary_min=smin,
            salary_max=smax,
            is_remote=remote,
            company_id=company.id,
            recruiter_id=recruiter.id,
        ))
    db.commit()
