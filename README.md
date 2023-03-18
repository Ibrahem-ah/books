# books
 
### Open CMD and install


**1- Go to the project folder to create our virtual environment** 

	python -m venv env


**2- Then we will activate our environment** 

	.\env\Scripts\activate
	
	
**3- after that we will install all the packages that i have use by running this command** 

	(env) pip install -r requirements.txt

**4- Start the webserver**

	(env) uvicorn app.main:app --reload
**4- Change the SQLALCHEMY_DATABASE_URL in database.py **

	"postgresql://<username>:<password>@localhost/<database_name>"
