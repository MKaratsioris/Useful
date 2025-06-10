# Basic Setup for PostgreSQL

## Download
- `sudo apt update`
- `sudo apt install postgresql postgresql-contrib`
- PostgreSQL creates a system user called postgres which has admin privileges on the database server. Switch to that user: `sudo -i -u postgres`
- Open the PostgreSQL interactive terminal: `psql`
- Change PostgreSQL authentication method to md5 (password-based). Edit the PostgreSQL `pg_hba.conf` file (Your PostgreSQL version might be different; adjust the path accordingly): `sudo nano /etc/postgresql/14/main/pg_hba.conf`
	- In lines like: `local..........all..........all.........peer`
	- Change them to:  `local..........all..........all.........md5`

## Create a Database
- `CREATE DATABASE spotify_db;`

## Create User
- `CREATE USER michalis WITH PASSWORD '123';`
- `CREATE USER michalis WITH SUPERUSER CREATEDB LOGIN;`
- `GRANT ALL PRIVILEGES ON DATABASE spotify_db TO michalis;
- `psql -d spotify_db -U michalis -W`
------------------------------------
- sudo -i -u postgres
- psql
- `ALTER ROLE michalis WITH LOGIN PASSWORD '123';`
- `GRANT ALL PRIVILEGES ON DATABASE spotify_db TO michalis;`
- `ALTER DATABASE spotify_db OWNER TO michalis;`
- Confirm that michalis is superuse: `\du michalis`

## Django coupling
- `pip install psycopg2-binary`
```python
# settings.py
DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.postgresql',
	'NAME': 'spotify_db',
	'USER': 'michalis',
	'PASSWORD': 'your_password_here',
	'HOST': 'localhost',
	'PORT': '5432',
    }
}
```

## Backup
If you want to backup or export your database, the recommended way is using: `pg_dump spotify_db > spotify_db_backup.sql`


