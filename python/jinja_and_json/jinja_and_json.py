# 
# Python app to create SQL statements 
# from project requirements
#

import os
import json
from jinja2 import Environment, FileSystemLoader

# Opening JSON file
f = open('201709.01_001_project.json')
  
# returns JSON object as a dictionary
data = json.load(f)
  
project = data['project']

#where_clauses = [{"field_name":"DateOfDiagnosis", "value":"20100101", "field_data_type":"date"  ,"is_list":"FALSE", "condition_type":">="  }
#                ,{"field_name":"DateOfDiagnosis", "value":"20221231", "field_data_type":"date"  ,"is_list":"FALSE", "condition_type":"<="  }
#                ,{"field_name":"Sex"            , "value":"2"       , "field_data_type":"string"  ,"is_list":"FALSE", "condition_type":"="  }
#                ,{"field_name":"behaviour"      , "value":['1','2'] , "field_data_type":"string","is_list":"TRUE"  , "condition_type":"="}
#                ,{"field_name":"icd_code"       , "value":["C56","C48.1","C48.2","C48.8","C57"]
#                                                                       , "field_data_type":"string","is_list":"TRUE"  , "condition_type":"like"}
#                ]
#where_clauses = [{'field_name': 'DateOfDiagnosis', 'value': '20100101', 'field_data_type': 'date', 'is_list': 'FALSE', 'condition_type': '>='}, {'field_name': 'DateOfDiagnosis', 'value': '20221231', 'field_data_type': 'date', 'is_list': 'FALSE', 'condition_type': '<='}, {'field_name': 'Sex', 'value': '2', 'field_data_type': 'string', 'is_list': 'FALSE', 'condition_type': '='}, {'field_name': 'behaviour', 'value': ['1', '2'], 'field_data_type': 'string', 'is_list': 'TRUE', 'condition_type': '='}, {'field_name': 'icd_code', 'value': ['C56', 'C48.1', 'C48.2', 'C48.8', 'C57'], 'field_data_type': 'string', 'is_list': 'TRUE', 'condition_type': 'like'}]
#where_clauses = [{"field_name": "DateOfDiagnosis", "value": "20100101", "field_data_type": "date", "is_list": "FALSE", "condition_type": ">="}, {"field_name": "DateOfDiagnosis", "value": "20221231", "field_data_type": "date", "is_list": "FALSE", "condition_type": "<="}, {"field_name": "Sex", "value": "2", "field_data_type": "string", "is_list": "FALSE", "condition_type": "="}, {"field_name": "behaviour", "value": ["1", "2"], "field_data_type": "string", "is_list": "TRUE", "condition_type": "="}, {"field_name": "icd_code", "value": ["C56", "C48.1", "C48.2", "C48.8", "C57"], "field_data_type": "string", "is_list": "TRUE", "condition_type": "like"}]

env = Environment(loader=FileSystemLoader('templates'), lstrip_blocks=True,trim_blocks=True)
template = env.get_template('cohort_select_sql.txt')
output = template.render(
             table_name   = project["cohort_specs"][0]["table_name_for_extraction"]
            ,columns      = project["cohort_specs"][0]["db_fields_for_extraction"]
            ,proj_no      = project["proj_no"]
            ,task_no      = project["task_no"]
            ,proj_title   = project["proj_title"]
            ,princ_invest = project["princ_invest"]
            ,where_clauses = project["cohort_specs"][0]["criteria"]
            )

print(project["cohort_specs"][0]["criteria"])

# Closing file
f.close()

print(output)