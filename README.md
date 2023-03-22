# DjangoCourseJatoba
This repository is one exemple of build project with Django Framework

https://pyup.io/repos/github/brjatoba92/DjangoCourseJatoba/shield.svg
https://pyup.io/repos/github/brjatoba92/DjangoCourseJatoba/python-3-shield.svg


Install libs:

1. Django:
```console
pip install django
```

2. python-decouple
```console
pip install python-decouple
```

3. dj-database-url
```console
pip install dj-database-url
```

4. psycopg2 lib
```console
pip install psycopg2-binary
```

5. gunicorn:
```console
pip install gunicorn
```

6. Whitenoise:
```console
pip install whitenoise
```

6. Generate requirements.txt
```console
pip freeze > requirements.txt
```


Start Project

1. Create manage.py file:
```console
django-admin startproject fly_django_project .
```

2. Run server project with manage.py:
```console
python manage.py --help
python manage.py runserver
```


Fly.io (Changindo in place heroku for deploy api):

1. Install flyctl

```console
curl -L https://fly.io/install.sh | sh
```

2. Manually add the directory to your $HOME/.bash_profile (or similar)
```console
export FLYCTL_INSTALL="/home/brunojat/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"
```

3. Save the .bashrc
```console
source .bashrc
```

4. Create .bash_aliases file with alias fly
```console
alias fly='/home/brunojat/.fly/bin/flyctl'
source .bash_aliases
```

5. Fly auth login
```console
fly auth login
```

6. Run fly launch
```console
fly launch
fly-django-jatoba
choose the region (rio de janeiro)
Would you like to set up a Postgresql database now? y
Development - Single node, 1x shared CPU, 256MB RAM, 1GB disk

DATABASE_URL=postgres://fly_django_jatoba:sYh8whbxjkARML0@fly-django-jatoba-db.flycast:5432/fly_django_jatoba?sslmode=disable

Would you like to set up an Upstash Redis database now? N
```

7. Fly deploy

```console
fly deploy
```

8. Fly secret list show the secrets keys:

```console
fly secret list
fly secrets set ALLOWED_HOSTS=fly-django-jatoba.fly.dev,
```

9. Edit fly.toml and add in final this line:

```console
[deploy]
  release_command = "python manage.py migrate --noinput"

[[statics]]
  guest_path = "/code/public"
  url_prefix = "/static/"
```

10. Create superuser:

```console
fly ssh console -t
user
email
password
```


Docker:

1. Docker install:

```console
https://github.com/codeedu/wsl2-docker-quickstart
```

2. Docker commands: 

```console
docker --help
docker --version
sudo service docker start
sudo service docker status
sudo service docker restart
docker build -t fly-deploy .
docker ps
docker stop 381a4e2e55f0
docker stop fly_django_project
```

```console
docker run --rm -it -p 8000:8000 -e SECRET_KEY=secret -e ALLOWED_HOSTS=localhost, fly-deploy .
sudo chmod +x start.sh
```

```console
docker run --name  fly_django_project -it -p 8000:8000 -e SECRET_KEY=secret -e ALLOWED_HOSTS=localhost, fly-deploy python manage.py migrate --noinput + python manage.py collectstatic --noinput
docker run --rm -it -p 8000:8000 -e SECRET_KEY=secret -e ALLOWED_HOSTS=localhost, fly-deploy python manage.py migrate
```

Documments:

1. Settings.py 

```console
from decouple import config, Csv
from dj_database_url import parse as db_url
...
DEBUG = config('DEBUG', cast=bool, default=False)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='localhost,') 

### ['fly-django-jatoba.fly.dev']

SECRET_KEY = config('SECRET_KEY')
...
INSTALLED_APPS = [
    ...
    'fly_django_project',
]

MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]

DATABASES = {
    'default': config(
        'DATABASE_URL', 
        default='sqlite: ///' + str(BASE_DIR / 'db.sqlite3'), 
        cast=db_url
    )
}
...
STATIC_ROOT = BASE_DIR / 'public'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
...
CSRF_TRUSTED_ORIGINS = ['https://fly-django-jatoba.fly.dev/']

```

2. Dockerfile
```console
# No used with whitenoise 
# RUN python manage.py collectstatic --noinput

# replace demo.wsgi with <project_name>.wsgi
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "fly_django_project.wsgi"]
```

3. .env file:
- Create .env and storage the variabel SECRET_KEY available in settings.py. Add DEBUG=True and ALLOWED_HOSTS=localhost, this file

4. Create .env.example and copy all the contents of the .env file changing the SECRET_KEY=secret

5. Start.sh (no used)

6. Create .dockerignore and add .env for not send the .env file
- Model:
```console
https://github.com/GoogleCloudPlatform/getting-started-python/blob/main/optional-kubernetes-engine/.dockerignore
```


Run Server and Migrate Commands:

1. Migrate:

```console
python manage.py migrate
```

2. Run server:
```console
python manage.py runserver
http://localhost:8000/
```


Whitenoise

1. settings.py:
```console
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]

...

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```


Github Actions

1. Create django.yml
```console
https://github.com/brjatoba92/DjangoCourseJatoba/actions/new
```
2. Test
