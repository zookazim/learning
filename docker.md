# Docker

DaveB APR-2022


## 1. Get a list of containers and their status

```bash
daveb@DOH-DIS-DE-DCKR:/opt/docker/compose/nginx$ sudo docker container ls -a
[sudo] password for daveb:
CONTAINER ID   IMAGE                        COMMAND                  CREATED        STATUS                     PORTS                                               NAMES
72e3bb6f2ee7   health/airflow-test:latest   "/usr/bin/dumb-init …"   3 weeks ago    Up 3 weeks                 8080/tcp, 0.0.0.0:5021->80/tcp, :::5021->80/tcp     oto_test_2_branch_webserver
a481de37afa9   health/airflow-test:latest   "/opt/airflow/script…"   3 weeks ago    Up 3 weeks                 8080/tcp                                            oto_test_2_branch_scheduler
68d263674e4c   health/nginx:0.0.2           "/docker-entrypoint.…"   3 weeks ago    Up 3 weeks                 80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp       nginx_web_1
2bc37fdf5cca   postgres:13                  "docker-entrypoint.s…"   3 weeks ago    Up 3 weeks                 5432/tcp                                            oto_test_2_branch_postgres
30d2250e1d87   health/airflow-test:latest   "/usr/bin/dumb-init …"   5 weeks ago    Up 2 weeks                 8080/tcp, 0.0.0.0:5020->80/tcp, :::5020->80/tcp     test_webserver
574ff31ca1ee   health/airflow-test:latest   "/opt/airflow/script…"   5 weeks ago    Up 3 weeks                 8080/tcp                                            test_scheduler
b4f5d801b95c   2cc9f1ab9aa4                 "/bin/bash -o pipefa…"   5 weeks ago    Exited (100) 5 weeks ago                                                       kind_saha
ef34520badae   postgres:13                  "docker-entrypoint.s…"   5 weeks ago    Up 3 weeks                 5432/tcp                                            test_postgres
b4f54aaf9f84   health/airflow-test:latest   "/usr/bin/dumb-init …"   5 weeks ago    Up 3 weeks                 8080/tcp, 0.0.0.0:5051->80/tcp, :::5051->80/tcp     documentation01_branch_webserver
14195049eacb   health/airflow-test:latest   "/opt/airflow/script…"   5 weeks ago    Up 3 weeks                 8080/tcp                                            documentation01_branch_scheduler
829cc8750118   postgres:13                  "docker-entrypoint.s…"   5 weeks ago    Up 3 weeks                 5432/tcp                                            documentation01_branch_postgres
```

# 2. SSH into a particular machine

sudo docker exec -it test_webserver /bin/bash