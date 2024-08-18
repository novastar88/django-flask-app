# Instalation

1. `git clone <github_repo_url>`
2. Create `./env` according to `env_example.txt`

## Dev environment
### Local
#### flask-service
1. `cd service`
2. Install virtual environment for Python 2.7.18
3. `pip install -r requirements.txt`
4. Run `app.py`

#### django-web
1. `cd web`.
2. Install virtual environment for Python 3.12.2
3. `pip install -r requirements.txt`
4. Db init
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py migrate --run-syncdb`
5. Generate static files`python manage.py collectstatic`
6. Create super user `python manage.py createsuperuser --noinput`
7. Test: `python mange.py test`
8. Run: `python manage.py runserver`

### Docker
1. Install docker - [Guide](https://docs.docker.com/desktop/install/windows-install/)
2. Check `docker-compose.yml` to see if any of the left-side ports are currently being used by any of your existing services to avoid internal connection problems
3. Check that `./.env` is set correctly (template file: `env_example_docker.txt`)
4. Run `docker compose -f docker-compose.yml`

## Production environment
At this stage the application is not production ready as nginx is not implemented.

# Endpoints
## flask-service
1. GET `/vehicle_status/<int:vehicle_id>`
Get Current state of the vehicle of given id.

## django-web
### Models endpoints
For all models (vehicle, driver, route):
1. GET `<root>/api/model/`
List of all model records.
2. POST `<root>/api/model/create/`
Insert to db one new record.
3. GET `<root>/api/model/<int:pk>/`
Get record by id,
4. PATCH `<root>/api/model/<int:pk>/update/`
Partial update record of specified id.
5. DELETE `<root>/api/model/<int:pk>/delete/`
Delete record of specified id.

### Other
1. `<root>/admin/`
Django admin
2. `<root>/users-management/...`
[djoser](https://djoser.readthedocs.io/en/latest/base_endpoints.html)
3. `<root>/auth/...`
[dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html#basic)
