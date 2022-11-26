# Flask Notes

## Setup

I followed this guide from Digital Ocean
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3



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

