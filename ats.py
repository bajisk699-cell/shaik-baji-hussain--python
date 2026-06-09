class Candidate:
    def __init__(self, candidate_id, name, email, age):
        self.candidate_id = candidate_id
        self.name = name
        self.email = email
        self.age = age          
        self.applied_jobs = []
    def apply_job(self, job):
        self.applied_jobs.append(job.job_id)
class Job:
    def __init__(self, job_id, title, company, location):
        self.job_id = job_id
        self.title = title
        self.company = company
        self.location = location 
class interview:
    def __init__(self, candidate, job):
        self.candidate = candidate
        self.job = job
interview= Candidate(1, "Alice", "alice@example.com", 30)
job = Job(1, "Software Engineer", "Tech Corp", "New York")  
interview.apply_job(job)
print(interview.applied_jobs)
print(job.title)
class Recruitment:
    def __init__(self, candidate_id, name, email, age):
        self.candidate_id = candidate_id
        self.name  = name
        self.email = email
        self.age = age          
        self.applied_jobs = []
    def apply_job(self, job):
        self.applied_jobs.append(job.job_id)
Recruitment = Candidate(2, "Bob", "bob@example.com", 25)
job2 = Job(2, "Data Analyst", "Data Inc", "San Francisco")
Recruitment.apply_job(job2)
print(Recruitment.applied_jobs)
print(job2.title)   