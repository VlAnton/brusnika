python3 -m venv brusnika;
source brusnika/bin/activate;
pip install -r requirements.txt;
cd ./brusnika_project;

python manage.py makemigrations;
python manage.py migrate;
python manage.py runserver