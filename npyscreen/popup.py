#!/usr/bin/python
#
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
# 0.1  13-MAY-2018 Dave B     Initial Version
#
# ************************************************************


import npyscreen as np

class myPop(np.NPSApp):

    def setopt(self, title, oList, multi):
        self.title = title
        self.options = oList
        self.multi = multi
        self.height = len(self.options)+1

    def main(self):
        F = np.Popup(name="Choose an option")
        if self.multi:
            opt = F.add(np.TitleMultiSelect, name=self.title, max_height=self.height, values=self.options, scroll_exit=True)
        else:
            opt = F.add(np.TitleSelectOne, name=self.title, max_height=self.height, values=self.options, scroll_exit=True)
        F.edit()
        self._values = opt.get_selected_objects()
        self.result = ( self._values if self.multi and len(self._values) > 1 else self._values[0] )

    def result(self):
        return self.result

def ChooseOption(title, oList, multi=False):

    pop = myPop()
    pop.setopt(title, oList, multi)
    pop.run()
    return pop.result

# Show a popup with radiobuttons to select 1 item from a list
print ChooseOption('choose a single element', ['a','b','c','d'])

# Show a popup with radiobuttons to multi-select items from a list
# print ChooseOption('choose multi-elements', ['a','b','c','d'], True)
