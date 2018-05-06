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

    def create(self):
       self.myName        = self.add(npyscreen.TitleText, name='Name')
       self.myDepartment  = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
       self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Employed')


class TestApp(npyscreen.NPSApp):
    def main(self):
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t = F.add(npyscreen.MultiLineEditableBoxed,
                        max_height=20,
                        name='List of Values',
                        footer="Press i or o to insert values",
                        values=ini_files,
                        slow_scroll=False)

        # This lets the user play with the Form.
        F.edit()      


class MyApplication(npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', TestApp, name='New Employee')
       # A real application might define more forms here.......


# ------------------------------------------------
# Main
# ------------------------------------------------      


# Get list of files from INI
# --------------------------

 
config = ConfigParser.ConfigParser()
config.read('checking.ini')

 
ini_files = []  # list to hold all files in INI

 
# Loop through sections of INI
for v_sec in config.sections():
    ini_files.append(v_sec)
    #for key, val in config.items(v_sec):
                    # Build the string that will contain the array assignment for shell
                    # eg. Project[proj_no]="201601.01"


if __name__ == "__main__":
    App = TestApp()
    App.run() 