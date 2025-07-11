# Python Environments Notes

## Setup

venv is part of python3. No setup required


## Create environment

The following commands will create a new director my_env within the project folder ie. "project_name" and store all the environment files there.

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

## VSCode Notebooks

To activate your environment in VSCode & Jupyter notebook
* create the environment manually as above (not using the VSCode prompt)
* install the Jypyter kernel in your new environment
``` bash
python3 -m ipykernel install --user --name=virtual_env_name
```
* select the python interpreter from your virtual environment
  * `Ctrl + Shift + P` then "Python: Select Interpreter"
  * Enter the interpreter path in your venv's bin


## Remove environment

Simple! Just remove the directory :-)

Use deactivate if it's been previously activated

``` bash
deactivate
rm -r my_env
```

