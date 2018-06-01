# flask_structure_example

> This repository contains the source code to accompany ["Structuring Large Flask Applications"](https://www.beta7.io/python/structuring-large-flask-applications.html).  
> For a more in-depth explanation please refer to the post.

An example of how to structure a medium to large sized [Flask](http://flask.pocoo.org/) application, with boilerplate for common setup and configuration.

## Quickstart

To run the example application, first clone the repository to your working directory. From there, activate the virtual environment and install the dependencies before running the application.

```bash
$ # Clone the respository, and change to it
$ git clone https://github.com/jessebraham/flask_structure_example.git && cd $_
$ # Activate the virtual environment and install all dependencies
$ pipenv shell
$ pipenv install
$ # Source the .env file, or export the variables within it
$ source .env
$ # Run the Flask application
$ flask run
```

## Requirements

This project was developed using [**Python 3.6.5**](https://docs.python.org/3/) (however any version of Python 3 *should* work) and [Pipenv](https://docs.pipenv.org/). The only required packages are [Flask](http://flask.pocoo.org/) and [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/).
