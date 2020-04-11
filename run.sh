python3 -m venv env;
source env/bin/activate;
pip install -r requirements.txt;
cd ./restraunt_menu;

python manage.py migrate;
python manage.py runserver