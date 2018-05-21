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

# Application Class
class TestApp(npyscreen.NPSApp):
    def main(self):
    
        # Main Form
        F  = npyscreen.Form(name = "INI Utility",)


        # Widget 1
        w1 = F.add( npyscreen.BoxTitle
                        ,name="Project Info"
                        ,max_height = 6
                        ,max_width=90
                        ,footer = "This is a footer"
                        ,values = proj_attributes
                        ,editable = False
                       )

        # Widget 2
        w2 = F.add( npyscreen.TitleSelectOne
                        #,max_height=20
                         ,max_width=30
                         ,relx=2
                         ,name='Sections'
                         ,footer="Press i or o to insert values"
                         ,values=ini_files
                         ,slow_scroll=False
                         ,value_changed_callback=self.when_inisection_changed()
                        )

        # Widget 3
        w3 = F.add( npyscreen.MultiLineEditableBoxed
                        #max_height=20
                        ,max_width=60
                        ,relx=32
                        ,rely=8
                        ,name='Configuration'
                        #footer="Press i or o to insert values"
                        ,values=configs
                        ,slow_scroll=False
                       )
        
        F.edit()
            
        self._values = w2.get_selected_objects()
        #self.result = ( self._values if self.multi and len(self._values) > 1 else self._values[0] )
        self.result = self._values[0]

    def result(self):
        return self.result
                       
    def when_inisection_changed(self, *args, **keywords):
        #self.name=w2.get_selected_objects()
        print self.result                     # Displays pointer to object - not the value text
        # print result(self)                    # Does not work
        #  print self._values[0]                 # Does not work
        # print "Hello"                           # Works - prints text at top of screen
         
        

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


if __name__ == "__main__":
    App = TestApp()
    App.run()
    #print App.result    # Works
    # print App.when_inisection_changed()  # Works