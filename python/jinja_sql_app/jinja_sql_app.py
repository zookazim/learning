# 
# Python app to create SQL statements 
# from project requirements
#

import os
from jinja2 import Environment, FileSystemLoader

id = 'p123'
proj_no = '201709.01'
task_no = '001'
proj_title = 'Ovarian Cancer'
princ_invest = 'Jane Doe'

# Specific cohort selection data
columns = [ 'TumourID', 'CancerRegistrationNumber', 'DiagnosisYear','DiagnosisDate','CancerType','Sex' ]
table_name = 'DW_Transformed.WACR.CancerMasterfile'

# Where clauses
criteria_date_field = "DateOfDiagnosis"
criteria_date_min   = "1984-01-01"
criteria_date_max   = "2023-12-31"
icd_code_field      = 'CancerType'
icd_code_list       = ["C56","C48.1","C48.2","C48.8","C57"]
additional_clauses  = {"start_date": "John", "age": 25}


#proj_no=proj_no, task_no=task_no, proj_title=proj_title, princ_invest=princ_invest

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('cohort_select_sql.txt')
output = template.render(
             columns      = columns
            ,table_name   = table_name
            ,proj_no      = proj_no
            ,task_no      = task_no
            ,proj_title   = proj_title
            ,princ_invest = princ_invest
            ,criteria_date_field = criteria_date_field
            ,criteria_date_min   = criteria_date_min
            ,criteria_date_max   = criteria_date_max
            ,additional_clauses = additional_clauses
            ,icd_code_field = icd_code_field
            ,icd_code_list  = icd_code_list
            )

#output = template.render(criteria_date_field="DateOfDiagnosis", criteria_date_min="1984-01-01", criteria_date_max="2023-12-31")

print(output)