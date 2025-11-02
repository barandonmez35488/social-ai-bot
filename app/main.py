from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Social Media Bot is running!"}

@app.get("/fetch-trends")
def fetch_trends():
    return {"trends": ["Data Science", "Python", "Cybersecurity"]}
