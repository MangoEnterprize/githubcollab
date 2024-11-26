# About
### This app is a demo for UniPortal, a networking platform for students used to connect them with resources such as scholarships, jobs, internships, writing support, etc. 

Built with Flask, HTML, CSS, JS

---

# Setup

### Running on Windows

- If .venv and requirements are already installed, just navigate to the scripts, run source activate, then do the run py thing, no need to reinstall venv and all that 
```bash
    # Create virtual envrionment
    python -m venv .venv

    # Activate virtual environment
    cd .venv/Scripts
    source activate
    cd ../../
    
    # Install packages
    pip install -r requirements.txt
    
    # Run server
    python run.py
```

- View the local server at http://127.0.0.1:5000
- Commands may vary by os and terminal
    - See for more details: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/