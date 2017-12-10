# Django Celery Example

Django sample app that uses celery to queue tweets for posting to twitter.
https://django-celery-example.herokuapp.com


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Install system dependencies using a package manager. E.g. for OSX, using homebrew:

    brew install python3 rabbitmq
    brew install postgresql  # optional, will use sqlite if not available

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/django-celery-example.git

Create a virtualenv using Python 3 and install dependencies. I recommend using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv django_celery_example --python=/path/to/python3
    pip install -r requirements.txt

Set environment variables as desired. Recommended dev settings:

    export DJANGO_DEBUG=1
    export DJANGO_ENABLE_SSL=0

Optional environment variables, generally only required in production:

    DJANGO_SECRET_KEY
    
You can add the exporting of environment variables to the virtualenv activate script so they are always available.

Install postgresql if desired. If you don't use postgresql, the app will use sqlite. If you use postgresql, you need an additional environment variable:

    export DATABASE_URL='postgres://<username>@127.0.0.1:5432/django_celery_example'

Set up db:

    createdb django_celery_example
    python manage.py migrate
    python manage.py createsuperuser  # Creates a superuser for the Admin, necessary to configure Facebook

Set up Twitter integration:

    Create a Twitter application at https://apps.twitter.com/
    python manage.py runserver
    Log into the Django admin
    Edit the Site to have the correct localhost url
    Create a Social application with info from Twitter (Client id == Consumer Key, Secret key = Consumer Secret, select site)

Check code style:

    flake8
    
Run celery:

    celery -A django_celery_example worker -l info  # Handles celery tasks

Run server:

    python manage.py runserver
    
Or run using gunicorn:

    gunicorn django_celery_example.wsgi

### Continuous Integration and Deployment

This project is already set up for deployment to Heroku.

Make a new Heroku app, and add the following addons:

    Heroku Postgres
	RabbitMQ Bigwig
