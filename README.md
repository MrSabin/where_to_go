# "Where to go" website

Working test version of site can be found [here](http://mrsabin.pythonanywhere.com)

## Installation:

1. Python 3 should be already installed.
2. Clone this repository by running

```bash
git clone https://github.com/MrSabin/where_to_go
```

3. Install dependencies by running

```bash
python3 -m pip install -r requirements.txt
```
4. Create `.env` file with app settings. Use `env_example` file as template.
5. Initialize database by running

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

7. Create superuser by running

```bash
python3 manage.py createsuperuser
```

## Running project:

To run development server, type

```bash 
python3 manage.py runserver
```

Site can be accessed on [127.0.0.1:8000](http://127.0.0.1:8000).

To access admin panel, use [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and use created superuser login/password.

## How to load place info to DB:

You can use `load_places` management command to load place info directly into database. Type

```bash
python3 manage.py load_places "json_url"
```
where "json_url" is the URL of JSON containing place info. JSON must be formatted like in json_example file.