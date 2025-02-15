## Installation

```sh
git clone https://github.com/gugi9000/keongom
cd keongom
python3 -m venv .
. bin/activate
pip install -r requirements.txt
cd keongom
python manage.py migrate
python manage.py runserver
sed -i -e "s/DEBUG = True/DEBUG = False/g" keongom/settings.py
sed -i -e "s/ALLOWED_HOSTS = \[]/ALLOWED_HOSTS = \['\*']/g" keongom/settings.py
```
