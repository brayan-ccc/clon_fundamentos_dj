#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### 📄 Archivo 2: `Procfile` (sin extensión)
```
web: gunicorn configuracion.wsgi:application
```

### 📄 Archivo 3: actualiza `requirements.txt`
Agrega estas líneas al final:
```
gunicorn==21.2.0
whitenoise==6.7.0
dj-database-url==2.2.0