# MegaLister
A web app capable of smoothly loading and displaying a very long list (10 million) of sorted user names  without freezing the browser.<br>

## Description
- Frontend: react app
- Backend: flask app (python)
- Database: postgresql, one table with index, firstname and lastname
- Trick for the large list load: pagination in requesting the sorted list starting with a specific alphabet, and bulk_insert_mapping to insert the data in batches of 1000 into the database (only once in the first time).
## Instructions to run the app locally for this first version<br>
- Clone the repository<br>
- If you don't have PostgreSql installed in your system, download installer https://www.postgresql.org/download<br>
- Open 'SQL SHELL (psql)' (it's installed alongside PostgreSQL) and connect to the PostgreSQL server using the password you set during installation. (Server, port and username as default.)<br>
- Create a USER <br>
    ``CREATE ROLE imane WITH LOGIN PASSWORD '246';``<br>
- Create a database<br>
  ``CREATE DATABASE usernames_db;``<br>
- Grant privileges<br>
    ``GRANT ALL PRIVILEGES ON DATABASE usernames_db TO imane;``<br>
- Connect to this database<br>
    ``\c usernames_db``<br>
- Create a table 'user' in it<br>
    ``CREATE TABLE user (``<br>
    ``id SERIAL PRIMARY KEY,``<br>
    ``firstname VARCHAR(50) NOT NULL,``<br>
    ``lastname VARCHAR(50) NOT NULL``<br>
    ``);``<br>
- After finishing the database setup, open the terminal and change directory to subfolder Backend and create a python virtual environment and activate it: <br>
#### For Windows system
    python -m venv venv 
    .\venv\scripts\activate
#### For MacOS
    python3 -m venv venv 
    source /venv/bin/activate
- Install requirements<br>
  ``pip install -r requirements.txt ``<br>
- Run the flask app<br>
    ``python run.py``
- keep this terminal openned and open a new terminal then change directory to subfolder Frontend<br>
- Run build<br>
    ``npm run build``<br>
- Start servering<br>
    ``npm install -g serve``<br>
    ``serve -s build``
- Open the browser and paste the local adress and port<br>
    ``http://localhost:3000``
#### To avoid all this work, I'm working on dockerizing this web app.
