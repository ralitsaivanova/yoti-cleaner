Hello Yoti people,

#### to start the server and test the endpoint

- Please create a virtual environment with python 3 or my use of f strings will be an insurmountable problem.
- Install the requirements in requirements.txt

A big assumption I am making here is that you are running a Postgres database.
- Please add your database credentials in [config.py](https://github.com/ralitsaivanova/yoti-cleaner/blob/master/yoti-cleaner/app/config.py)
- Assuming you are using virtualenv wrapper, please add the [root directory](https://github.com/ralitsaivanova/yoti-cleaner/tree/master/yoti-cleaner) to your virtualenv
- create the database and the table where the input and the output will be persisted by calling
```
python database/create_database.py
```
- start the flask server
```
FLASK_APP=app/endpoint.py flask run
```

Finally, after all these configurations you can run a request with
```
python call_webapp.py
```
It will print in the console the status and the text of the response.

#### to run the tests

```
pytest tests/
```
