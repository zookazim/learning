#!/usr/bin/python
#*************************************************************
# Description : Demo the capabilities of npyscreen
#               Pass values between forms
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

import npyscreen as np

class EmployeeForm(np.ActionForm):
    def create(self):
        self.myName = self.add(np.TitleText, name='Name')
        self.myDepartment = self.add(np.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
        self.myDate = self.add(np.TitleDateCombo, name='Date Employed')

    def afterEditing(self):
        self.parentApp.getForm('CONFIRMFM').wgName.value = self.myName.value
        self.parentApp.switchForm('CONFIRMFM')

class EmployeeConfirmForm(np.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.value = None
        self.wgName  = self.add(np.TitleFixedText, name = "Name:",)
        self.wgDept = self.add(np.TitleText, name = "Dept:")
        self.wgEmp      = self.add(np.TitleText, name = "Employed:")

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

class myApp(np.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', EmployeeForm, name='Employee Entry')
        self.addForm('CONFIRMFM', EmployeeConfirmForm, name='Employee Confirmation')

if __name__ == '__main__':
    TestApp = myApp().run()