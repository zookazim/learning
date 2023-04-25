# 
# Python app to create SQL statements 
# from project requirements
#

import os
from jinja2 import Environment, FileSystemLoader

columns = [ 'last_name', 'username', 'email' ]
table_name = 'vw_emergency'
id = 'p123'
proj_no = '201709.01'
task_no = '001'
proj_title = 'Ovarian Cancer'
princ_invest = 'Jane Doe'

#proj_no=proj_no, task_no=task_no, proj_title=proj_title, princ_invest=princ_invest

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('header_sql.txt')
output = template.render(columns=columns, table_name=table_name, proj_no=proj_no, task_no=task_no, proj_title=proj_title, princ_invest=princ_invest)

#output = template.render(criteria_date_field="DateOfDiagnosis", criteria_date_min="1984-01-01", criteria_date_max="2023-12-31")

print(output)