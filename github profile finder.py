import uvicorn
import webbrowser
from fastapi import FastAPI
github_profiles=FastAPI()
@github_profiles.post("/")
def profiles(username:str):
    url=f"https://github.com/{username}"
    return webbrowser.open(url)
if __name__=="__main__":
    uvicorn.run("github profile finder:github_profiles",host="127.0.0.1",port=8000)