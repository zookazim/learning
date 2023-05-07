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


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

# Process input arguments
args = fn_parse_args()


# Opening JSON file
f = open(args.json_filename)

# Returns JSON object as a dictionary
data = json.load(f)
project = data['project']



# Create SQL Using template
env = Environment(loader=FileSystemLoader('templates'), lstrip_blocks=True,trim_blocks=True)


# Cohort selection
# template = env.get_template('cohort_select_sql.txt')
# output = template.render(
#              proj_id       = project["id"]
#             ,proj_no       = project["proj_no"]
#             ,task_no       = project["task_no"]
#             ,proj_title    = project["proj_title"]
#             ,princ_invest  = project["princ_invest"]
#             ,table_name    = project["cohort_specs"][0]["table_name_for_extraction"]
#             ,columns       = project["cohort_specs"][0]["lnk_src_keys"]
#             ,src           = project["cohort_specs"][0]["lnk_src"]
#             ,where_clauses = project["cohort_specs"][0]["criteria"]
#             ,insert_into_table_name = project["cohort_specs"][0]["insert_into_table_name"]
#             )

# Cohort list
# template = env.get_template('cohort_sql.txt')
# output = template.render(
#              proj_id       = project["id"]
#             ,proj_no       = project["proj_no"]
#             ,task_no       = project["task_no"]
#             ,proj_title    = project["proj_title"]
#             ,princ_invest  = project["princ_invest"]
#             ,table_name    = project["cohort_specs"][0]["table_name_for_extraction"]
#             ,columns       = project["cohort_specs"][0]["lnk_src_keys"]
#             ,src           = project["cohort_specs"][0]["lnk_src"]
#             ,where_clauses = project["cohort_specs"][0]["criteria"]
#             ,insert_into_table_name = project["cohort_specs"][0]["insert_into_table_name"]
#             )

# Extraction of data
template = env.get_template('data_extract_sql.txt')
output = template.render(
             proj_id       = project["id"]
            ,proj_no       = project["proj_no"]
            ,task_no       = project["task_no"]
            ,proj_title    = project["proj_title"]
            ,princ_invest  = project["princ_invest"]
            ,table_name    = project["dataset_specs"][0]["table_name_for_extraction"]
            ,columns       = project["dataset_specs"][0]["db_fields_for_extraction"]
            ,src           = project["dataset_specs"][0]["lnk_src"]
            ,src_keys      = project["dataset_specs"][0]["lnk_src_keys"]
            ,insert_into_table_name = project["cohort_specs"][0]["insert_into_table_name"]
            )

 
# Closing file
f.close()

print(output)