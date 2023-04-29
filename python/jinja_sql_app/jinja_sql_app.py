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
#criteria_date_field = "DateOfDiagnosis"
#criteria_date_min   = "1984-01-01"
#criteria_date_max   = "2023-12-31"
#icd_code_field      = 'CancerType'
#icd_code_list       = ["C56","C48.1","C48.2","C48.8","C57"]
#additional_clauses  = {"behaviour" : ["2","3"], "sex": "2"}

where_clauses = [{"field_name":"DateOfDiagnosis", "criteria":"20100101", "field_data_type":"date"  ,"is_list":"FALSE", "condition_type":">="  }
                ,{"field_name":"DateOfDiagnosis", "criteria":"20221231", "field_data_type":"date"  ,"is_list":"FALSE", "condition_type":"<="  }
                ,{"field_name":"Sex"            , "criteria":"2"       , "field_data_type":"string"  ,"is_list":"FALSE", "condition_type":"="  }
                ,{"field_name":"behaviour"      , "criteria":['1','2'] , "field_data_type":"string","is_list":"TRUE"  , "condition_type":"="}
                ,{"field_name":"icd_code"       , "criteria":["C56","C48.1","C48.2","C48.8","C57"]
                                                                       , "field_data_type":"string","is_list":"TRUE"  , "condition_type":"like"}
                ]



#proj_no=proj_no, task_no=task_no, proj_title=proj_title, princ_invest=princ_invest
 
env = Environment(loader=FileSystemLoader('templates'), lstrip_blocks=True,trim_blocks=True)
template = env.get_template('cohort_select_sql.txt')
output = template.render(
             columns      = columns
            ,table_name   = table_name
            ,proj_no      = proj_no
            ,task_no      = task_no
            ,proj_title   = proj_title
            ,princ_invest = princ_invest
            ,where_clauses = where_clauses
            )

#output = template.render(criteria_date_field="DateOfDiagnosis", criteria_date_min="1984-01-01", criteria_date_max="2023-12-31")

print(output)