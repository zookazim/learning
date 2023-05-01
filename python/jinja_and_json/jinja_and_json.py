#!/usr/bin/python
#
#-----------------------------------------------------------
# Description : Python app to create SQL statements 
#               from project requirements in JSON docs
#  
# Author      : Dave B  
# Date        : AUG-2017
# -----------------------------------------------------------


# -----------------------------------------------------------
# Libraries
# -----------------------------------------------------------

import os
import json
from jinja2 import Environment, FileSystemLoader
import argparse

# -----------------------------------------------------------
# Functions
# -----------------------------------------------------------

def fn_parse_args():

    """Parse arguments supplied to this script
    
    Args:
        None
        
    Returns:
        args : object containing parsed information
    """

    # Parse arguments supplied by the user
    # for use later in this script
    
    parser = argparse.ArgumentParser(description='Create SQL from project JSON file')
    
    parser.add_argument( dest='json_filename'
                        ,action='store'
                        ,help='Filename of the JSON document')

    args = parser.parse_args()     
    #v_inifile = args.inifilename
    return args

# Opening JSON file
f = open(args.json_filename)

# returns JSON object as a dictionary
data = json.load(f)
  
project = data['project']

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