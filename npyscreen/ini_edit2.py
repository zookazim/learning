#!/usr/bin/python
#*************************************************************
# Description : Demo the capabilities of npyscreen
#
# Author      : Dave B
# Date        : MAY-2018
#
# -----------------------------------------------------------
# Modifications
#
# No   Date        User       Description
# --   ----------- ---------  --------------
#
# 0.1  01-MAY-2018 Dave B     Initial Version
#
# ************************************************************


import npyscreen
import sys, ConfigParser


# ------------------------------------------------
# Classes
# ------------------------------------------------

class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)
        print self.myDepartment.value

    def create(self):
       self.myName        = self.add(npyscreen.TitleText, name='Name')
       self.myDepartment  = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
       self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Employed')

class MyApplication(npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', myEmployeeForm, name='New Employee')
       # A real application might define more forms here.......


# ------------------------------------------------
# Functions
# ------------------------------------------------

def get_project_info():
    "Build up list of project value-attributes configs"
    lst_proj = []
    lst_proj.append('Proj No    : ' + config.get('project', 'no'))
    lst_proj.append('Task No    : ' + config.get('project', 'task'))
    lst_proj.append('Principal  : ' + config.get('project', 'pi'))
    lst_proj.append('Title      : ' + config.get('project', 'title'))
    return lst_proj    
    
# ------------------------------------------------
# Main
# ------------------------------------------------


# Get list of files from INI
# --------------------------

config = ConfigParser.ConfigParser()
config.read('checking.ini')


ini_files = []          # list to hold all files in INI
proj_attributes = []    # list to hold project attributes from INI
configs = []            # list to hold configuration attributes from INI

# Get Proj configs for display
proj_attributes = get_project_info()

# Loop through sections of INI
for v_sec in config.sections():
    ini_files.append(v_sec)
    for key, val in config.items(v_sec):
        configs.append(key+' = '+val)


if __name__ == '__main__':
   TestApp = MyApplication().run()
   print "Hello!"
