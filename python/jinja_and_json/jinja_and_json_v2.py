#!/usr/bin/python
#
#-----------------------------------------------------------
# Description : Python app to create SQL statements 
#               from project requirements supplied in JSON format
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

    parser.add_argument( dest='pStrJson'
                        ,action='store'
                        ,help='JSON text describing project')

    args = parser.parse_args()     
    #v_inifile = args.inifilename
    return args


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def fn_parse_args():

    # Initial Setup
    # ---------------

    # Process input arguments
    args = fn_parse_args()

    # Load JSON
    data = json.loads(args.pStrJson)

    # Create a list to hold all SQL statements
    lstSQL = []

    # SQL Generation
    # ---------------
    # Create all SQL statements and populate the list (lstSQL) 
    # of records (a dictionary called dictSQL) which will be passed back as a JSON document

    # Create SQL Using template
    env = Environment(loader=FileSystemLoader('templates'), lstrip_blocks=True,trim_blocks=True)
    #Cohort selection
    template = env.get_template('cohort_select_sql.txt')


    project = data['project']
    # Loop through cohorts
    # for cohort_spec in project["cohort_specs"]:
    #     sql_txt = template.render(
    #                 proj_id       = project["id"]
    #                 ,proj_no       = project["proj_no"]
    #                 ,task_no       = project["task_no"]
    #                 ,proj_title    = project["proj_title"]
    #                 ,princ_invest  = project["princ_invest"]
    #                 ,coh_id        = cohort_spec["id"]
    #                 ,table_name    = cohort_spec["table_name_for_extraction"]
    #                 ,columns       = cohort_spec["lnk_src_keys"]
    #                 ,src           = cohort_spec["lnk_src"]
    #                 ,where_clauses = cohort_spec["criteria"]
    #                 ,insert_into_table_name = cohort_spec["insert_into_table_name"]
    #                 )
        
    #     dictSQL = {"proj_id":project["id"], "coh_id":cohort_spec["id"], "sql_type":"cohort_select", "sql_txt":sql_txt}
    #     lstSQL.append(dictSQL.copy())

        #print(output)

    # Cohort list
    # template = env.get_template('cohort_sql.txt')
    # for cohort_spec in project["cohort_specs"]:
    #     sql_txt = template.render(
    #                 proj_id       = project["id"]
    #                 ,proj_no       = project["proj_no"]
    #                 ,task_no       = project["task_no"]
    #                 ,proj_title    = project["proj_title"]
    #                 ,princ_invest  = project["princ_invest"]
    #                 ,coh_id        = cohort_spec["id"]
    #                 ,table_name    = cohort_spec["table_name_for_extraction"]
    #                 ,columns       = cohort_spec["lnk_src_keys"]
    #                 ,src           = cohort_spec["lnk_src"]
    #                 ,where_clauses = cohort_spec["criteria"]
    #                 ,insert_into_table_name = cohort_spec["insert_into_table_name"]
    #             )

    #     #print(output)
    #     dictSQL = {"proj_id":project["id"], "coh_id":cohort_spec["id"], "sql_type":"cohort", "sql_txt":sql_txt}
    #     lstSQL.append(dictSQL.copy())


    # Extraction of data
    # template = env.get_template('data_extract_sql.txt')
    # for cohort_spec in project["dataset_specs"]:
    #     sql_txt = template.render(
    #                 proj_id       = project["id"]
    #                 ,proj_no       = project["proj_no"]
    #                 ,task_no       = project["task_no"]
    #                 ,proj_title    = project["proj_title"]
    #                 ,princ_invest  = project["princ_invest"]
    #                 ,coh_id        = cohort_spec["id"]
    #                 ,table_name    = cohort_spec["table_name_for_extraction"]
    #                 ,columns       = cohort_spec["lnk_src_keys"]
    #                 ,src           = cohort_spec["lnk_src"]
    #                 ,where_clauses = cohort_spec["criteria"]
    #                 ,insert_into_table_name = cohort_spec["insert_into_table_name"]
    #                 )

        #print(output)
        # dictSQL = {"proj_id":project["id"], "coh_id":cohort_spec["id"], "sql_type":"extraction", "sql_txt":sql_txt}
        # lstSQL.append(dictSQL.copy())


    # # QA Checks
    # template = env.get_template('checks_sql.txt')
    # for cohort_spec in project["cohort_specs"]:
    #     for cohort_check in cohort_spec["checks"]:
    #         #output = 'coh_id={}'.format(cohort_spec["id"])

    #         sql_txt = template.render(
    #                     proj_id       = project["id"]
    #                     ,proj_no       = project["proj_no"]
    #                     ,task_no       = project["task_no"]
    #                     ,proj_title    = project["proj_title"]
    #                     ,princ_invest  = project["princ_invest"]
    #                     ,coh_id        = cohort_spec["id"]
    #                     ,cohort_name   = cohort_spec["name"]
    #                     ,table_name    = cohort_spec["table_name_for_extraction"]
    #                     ,check         = cohort_check
    #                     ,src           = cohort_spec["lnk_src"]
    #                     ,src_keys      = cohort_spec["lnk_src_keys"]
    #                     ,insert_into_table_name = cohort_spec["insert_into_table_name"]
    #                     )

    #         #print(output)
    #         dictSQL = {"proj_id":project["id"], "coh_id":cohort_spec["id"], "sql_type":"cohort_checks", "sql_txt":sql_txt}
    #         lstSQL.append(dictSQL.copy())

    # Use for string output of only one sql type
    # for dictSQL in lstSQL:
    #     if dictSQL["sql_type"] == 'cohort_checks':
    #         print(dictSQL["sql_txt"])

    # QA Data Extraction Checks
    template = env.get_template('checks_sql.txt')
    for group_spec in project["dataset_specs"]:
        for cohort_check in group_spec["checks"]:

            #sql_txt = 'Check for ' & cohort_check

            sql_txt = template.render(
                        proj_id       = project["id"]
                        ,proj_no       = project["proj_no"]
                        ,task_no       = project["task_no"]
                        ,proj_title    = project["proj_title"]
                        ,princ_invest  = project["princ_invest"]
                        ,grp_id        = group_spec["id"]
                        ,cohort_name   = group_spec["name"]
                        ,table_name    = group_spec["table_name_for_extraction"]
                        ,check         = cohort_check
                        ,src           = group_spec["lnk_src"]
                        ,src_keys      = group_spec["lnk_src_keys"]
                        ,insert_into_table_name = group_spec["insert_into_table_name"]
                        )


            dictSQL = {"proj_id":project["id"], "grp_id":group_spec["id"], "sql_type":"data_extract_checks", "sql_txt":sql_txt}
            lstSQL.append(dictSQL.copy())


    jsonSQL = json.dumps(lstSQL)
    print(jsonSQL)

