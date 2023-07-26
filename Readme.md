this is fitness metrics project



# create venv folder:
python3 -m venv /Users/shrutiv/DjangoProject/FitnessMetrics/venv

# activate virtual environment:
source venv/bin/activate

# install django
pip install --upgrade pip
pip install django

# create django project
django-admin startproject FMDashboard .

# run django project
python manage.py runserver   

# create django app
django-admin startapp app  

# create frontend:
# Create template folder 
    # app folder -> index.html
    # partials -> base.html and nav.html

# create database in latest postgresql:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fmdashboard',
        'USER': 'postgres',
        'PASSWORD': 'abc123',
        'HOST': 'localhost',
        'PORT': '5434',
    }
}
# create database.py

# create Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash", "-c", "python database.py && python manage.py runserver 0.0.0.0:8000"]



# create docker-compose.yml
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - 8000:8000

# build docker image
docker-compose build

# start conatiner
docker-compose up
