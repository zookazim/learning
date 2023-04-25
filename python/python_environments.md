# Python Environments Notes

## Setup

venv is part of python3. No setup required


## Create environment

### Linux
``` bash
mkdir project_name
cd project_name
python3 -m venv my_env
```

### Windows
``` bash
mkdir project_name
cd project_name
python3 -m venv my_env
```

## Use environments

### Linux
``` bash
# From the project directory created above
source my_env/bin/activate
```

### Windows
``` bash
# From the project directory created above
my_env\Scripts\activate
```


## Remove environment

Simple! Just remove the directory :-)

Use deactivate if it's been previously activated

``` bash
deactivate
rm -r my_env
```

