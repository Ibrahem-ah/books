# books
 
### Open CMD and install

**1-Install virtualenv**

	pip install virtualenv

**1- Go to the project folder to create our virtual environment** 

	python -m venv env


**2- Then we will activate our environment** 

	.\env\Scripts\activate
	
	
**3- after that we will install all the packages that i have use by running this command** 

	(env) pip install -r requirements.txt

**5- Start the webserver**

	(env) uvicorn app.main:app --reload
