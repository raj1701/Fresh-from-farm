# Fresh-from-farm
E-commerce Django app
## Technology Stack

 - Django (Python)
 - HTML
 - CSS
 - BootStrap
 - SQLite (Database)

## Install components
```bash
sudo apt-get update
sudo apt-get install python-pip 
```

### Setting up Virtual Environment and Install Requirements
```bash
sudo pip install virtualenv
python3 -m venv dbmsenv
source dbmsenv/bin/activate
pip install -r requirements.txt
```

### Running the website locally
```bash
make Debug = True in the settings.py 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
