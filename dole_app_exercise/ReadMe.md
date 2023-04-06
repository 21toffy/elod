####Dole App Take Home Interview

Thank you for taking out time to work on this application. 

To get started, you should familiarize yourself with the structure of this application.

This is a Flask Application. Its HTML files live in the `app/templates` folder and its Javascript and CSS files should live 
in the `app/static` directory. This project uses the `Blueprint` structure provided natively by Flask. 

All Database Model Objects live in the `app/models.py` file. 

All migration files are in the `dole_migrations/versions` directory. `Alembic` is the tool used for database migrations. 

`instance/config.py` houses all configurations for this application.  

All required dependencies are in `requirements.txt` file. 

A virtual environment - `venv` - was created for this project as well.

Sqlite database [`instance/dole_app_db.db`]
 
####Getting Started
Before you get started, you should execute these exports:
```
export FLASK_APP=application.py;
export APP_SETTINGS=instance.config.DoleAppConfig;
export FLASK_ENV=development;
```

####Tips
To create a new versioned migration file, run:

```flask db migrate -m <name_of_file>```

To run a database upgrade operation, execute:

```flask db upgrade```

To run a database downgrade operation, execute:

```flask db downgrade```

To start the application, execute:

```flask run```

When you start the application, visit http://127.0.0.1:5000/home/all/users to ensure the application starts correctly. 

###Instructions

This is meant to be a simple application. What we are looking for is not just an application that works. Rather, we value good engineering at Fedha and, to us, this consists good code, great architect, optimized calls and lovely designs.
Attached herewith is a spreadsheet containing the list of employees at Company X. These employees have mmoved around different units in the company.

Your task is to create a solution where a user (an admin, possibly) can visit this application, upload a file as the one attached and they can see the following:

1. The number of years each user spent in each unit.
2. The cumulative number of years each employees has spent in the company.
3. A way to tell, with a graph, the number of years spent in each unit by all employees. For example, if employee A spent 5 years in Unit D and employee B spent 6 years, we should have 11 years attributed to Unit D.
 
#### EVALUATION CRITERIA

Your solution will be evaluated for:
1. Design/Architecture Quality -- this is very crucial to us.
2. Code Quality -- this is very crucial to us.
3. Input (Form) validation
4. User Experience (Frontend) -- this carries a lot of weight.
5. DB Migration
6. Tests

In addition, please, style pages with CSS and/or JavaScript; as you see fit to demonstrate front-end capabilities.

Send your finished work as a zipped file named as `Firstname_Lastname_Dole_Challenge` to `fedha@fedha.co`. The subject of your email should be `Dole App Take Home Interview`.
 
Again, thank you for considering joining our burgeoning team. 

