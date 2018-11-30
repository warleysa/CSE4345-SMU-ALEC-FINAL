# SMU ALEC Tutor Session Tracker

This repo contains the code to be deployed on a AWS EC2 Instance to be run with the database included.

Steps to run: 

Prerequisites:
	1) Python 3 installed

	2) Port 80 and 8080 open to 0.0.0.0 inbound traffic on EC2

	3) Virtual Environment installed

Install python req on Ubuntu/Unix:

	Run: "sudo apt-get install python3.5-dev libmysqlclient-dev"

	Run: "sudo apt-get install python3-numpy"

Requirements:
	1) Create a virtual environment within the parent directory
	
			Run: "python3 -m venv env"
			
	2) Activate the Virtual Environment
	
			Run: "source env/bin/activate"
			
	3) Make sure pip is updated
	
			Run: "pip install --upgrade pip"
			
	4) Update the setuptools
	
			Run: "pip install --upgrade setuptools"
			
	5) Install Package dependencies
	
			Run: "pip install -r requirements.txt"
			
	6) Finally, run the website on the server through your network IP on port 80
	
			Run: "python manage.py runserver -h 0.0.0.0 -p 80"
			
