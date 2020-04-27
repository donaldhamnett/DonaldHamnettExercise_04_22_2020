# Backend Screening Exercise

### Installation Instructions
1) Clone this repository and create a Python3.7 virtualenv in the repository root.
2) After activating the virtualenv, navigate to `./src` and run `pip install -r requirements.txt` or `pip install -e .` to install the required dependencies.
3) Before starting the app, run `python manage.py create_questions` to setup the database schemas.
4) To start the app, invoke `python run.py`. The Flask development server should be running on `http://127.0.0.1:5000/`.

### Usage Instructions
Opening `localhost:5000` in your browser will bring you to the home page. There are 3 navigation options other than the home page:
* **Create** (`localhost:5000/create`) allows you to enter a new question into the database. 
* **Update** (`localhost:5000/update`) allows you to change question text given its ID. 
* **History** (`localhost:5000/history`) allows you to view the changes to a question over time, given its ID.

The create, update, and history functionality is also exposed via a REST API at `localhost:5000/api/v1/questions`, where their respective request types are post, patch, and get. Any required data is sent either form-encoded or as JSON.

### What Went Well
Building the REST API and database schemas for the questions went well, as I have some experience with this and it is fresh in my mind.

### What Was Difficult
I don't have much frontend experience, so going with a command line app might have allowed me to spend more time on the backend. There were also some JSON Decode errors that took up way too much time and which I ended having to hack around.

### What I Would Improve
Definitely the way I'm doing my audit tables, which I read can be done using triggers instead of manually. Also, I'd build out the question response table and API which only exists as a commented-out file. I know there is Flask support for Users, so I would have liked to implement that. Lastly, I'd work in some actual data checking and giving useful error reports and suggestions upon failure instead of blindly catching every exception.

### Acknowledgements
I have been lucky to work with some Flask at my current internship, so that helped me get up and running. I was especially helped by [this tutorial](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one) from which I heavily borrowed when implementing the web frontend.

## Thanks!
-Donald
