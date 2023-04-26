# Flask Notes

## Setup

I followed this guide from Digital Ocean
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

### Install Flask

``` bash
source my_env2/bin/activate
pip install flask
```

Now check the version installed
``` bash
python -c "import flask; print(flask.__version__)"
```

## Run Flask App

### When using Virtual Box 
1. Open settings > network register port 5000 
2. Get flask to listen on all ports on the VM 

``` bash        
flask run --host=0.0.0.0
```

### Running Flask from the command line

``` bash    
export FLASK_APP=app.py
export FLASK_ENV=development        
flask run
```


## SQLAlchemy

### Create the database (first time)

``` bash
from proj_meta_app import create_app
app = create_app()
app.app_context().push()
from proj_meta_app import db
db.create_all()

```

### Create a new table added to models.py ###

This example is adding the table Project. From the python prompt;

``` bash
from proj_meta_app import create_app
app = create_app()
app.app_context().push()
from proj_meta_app import db
from proj_meta_app.models import Project
Project.__table__.create(db.session.bind)
```


## Create New Blueprint ##

### General Design ###

* Create subdirectory for blueprint eg. "projects"
* Make subdirectory python package using "__init.py"
* Add forms.py
* Add routes.py
* Add template page

#### Create New Subdirectory ####

Add a new subdirectory under the main app directory eg.

``` bash
cd my_app
mkdir projects
```

#### Designate Python Package ####

Set directory as a python package

``` bash
cd my_app/projects
touch __init.py__
```

#### Add Forms ####

``` bash
cd my_app/projects
touch forms.py
```

#### Add Routes ####

``` bash
cd my_app/projects
touch routes.py
```

#### Add Template Page ####

``` bash
cd my_app/templates
touch projects.html
```

