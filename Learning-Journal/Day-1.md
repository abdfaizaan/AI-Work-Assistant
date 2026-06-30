## Today's Goal
To create sample app.py and record.py modules for the app and test it locally. 

## What I learned?
- Prompting GitHub Copilot to build the righth code we want.
- Pushing the code to GitHub repo

## New Git commands
- git status
- git add .
- git commit -m "Commit message"
- git push
- git fetch
- git pull

## Notes: 

### Q1. Why use a Python Virtual environment?
- A Python virtual env is not only for executing python code, Python codes can be executed with or without virtual env. A Python env is an isolated Python installation for specific project. it keeps that project's packages seperate from other projects, preventing version conflicts and making the project reproducible in other machines. 

### Q2. What is requirements.txt?
- This file lists the exact Python packages and versions required for this project so anyone can recreate the sam env using `pip install -r requirements.txt`

### Q3. Why do we created seperate app.py and record.py files?
- Each file have one responsibility, if later we change the speech engine, we only modify the speech.py file and not the entire code. 

### Q4. What does git status shows?
- It tells us which files changed, which files are staged, untracked, which branch you're in, whether you are ahead or behind the remote repo.