## Installation

# Ready the server

```sh
git clone https://github.com/gugi9000/keongom
cd keongom
python3 -m venv .
. bin/activate
pip install -r requirements.txt
cd keongom
python manage.py migrate
sed -i -e "s/DEBUG = True/DEBUG = False/g" keongom/settings.py
sed -i -e "s/ALLOWED_HOSTS = \[]/ALLOWED_HOSTS = \['your.server.tld']/g" keongom/settings.py
## Add your domain to the settings file too.
## Honestly, deploying Django is a chore.. I'll create a script.

mkdir staticfiles
# jeez - there is also some static config, you have to set up in settings.py

python manage.py collectstatic
## and make you reverse proxy rewrite /static/foo to /foo
# check your server
gunincorn keongom.wsgi 
```


# Set up the monitor

And then add ´echo `pwd`/../bin/python `pwd`/manage.py check_http` to cron every 5 minutes or such

```crontab
*/5 * * * * /path/to/venv/bin/python /path/to/venv/keongom/keongom/manage.py check_http
 ### or
 0,5,10,15,20,25,30,35,40,45,50,55  </path/to/venv>/bin/python </path/to/venv/>keongom/keongom/manage.py check_http
```


# Configure supervisor

Edit or create a new file `/etc/supervisor/conf.d/keongom.conf`:
`sudo vim /etc/supervisor/conf.d/keongom.conf`

```conf
[program:keongeom]
command=/path/to/venv/bin/gunicorn keongom.wsgi
directory=/path/to/venv/keongom/
user=bs
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```