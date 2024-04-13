# UDEMY APACHE AIRFLOW NOTES

## Using Virtual Machine

### Udemy course create DAG


1. Startup VirtualBox machine
2. Open VS Code
3. F1 to get commands -> SSH login -> local machine
4. Open terminal (you are now in virtual machine)
5. $> source sandbox/bin/activate


### Startup airflow

airflow scheduler
airflow webserver (in another ssh session)


### Airflow SSH Setup

host : airflow@localhost
port : 2222

### GUI

http://localhost:8080/home
user: admin
pwd : admin

## Using Docker

### Installing Docker

Refer to "Section 2 : Getting Started With Airflow" of the Udemy course part 13 [Practice] Installing Apache Airflow

### Running Airflow

#### Container Startup
In Windows startup the docker GUI and check all the Airflow containers are running.

You can check Airflow is running from the command line by using the Terminal (I did it in VS Code) and open the directory where the docker yaml file is stored. If you followed the section above "Installing Docker" then you can open Documents/materials directory.

I have it saved here;
C:\learning\airflow_udemy_course\materials

Then type in the Terminal "docker-compose ps"

<code>
PS C:\learning\airflow_udemy_course\materials> docker-compose ps
NAME                            COMMAND                  SERVICE             STATUS              PORTS
materials-airflow-init-1        "/bin/bash -c 'funct…"   airflow-init        exited (0)
materials-airflow-scheduler-1   "/usr/bin/dumb-init …"   airflow-scheduler   running (healthy)   8080/tcp
materials-airflow-triggerer-1   "/usr/bin/dumb-init …"   airflow-triggerer   running (healthy)   8080/tcp
materials-airflow-webserver-1   "/usr/bin/dumb-init …"   airflow-webserver   running (healthy)   0.0.0.0:8080->8080/tcp
materials-airflow-worker-1      "/usr/bin/dumb-init …"   airflow-worker      running (healthy)   8080/tcp
materials-postgres-1            "docker-entrypoint.s…"   postgres            running (healthy)   5432/tcp
materials-redis-1               "docker-entrypoint.s…"   redis               running (healthy)   6379/tcp
</code>

#### GUI

Open the browser;
//localhost:8080

Sign in with : user "Airflow", pwd "Airflow"

