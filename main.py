# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import view
import wx
from controller import Controller

#Regler
"""
class NameConvention:

    def __init__(self, input):
        self.new_property = input

    def create_new(self, imp):

        anv�nd inga get setters om det inte g�r n�got innan.
        Tabs �r spaces
        K�r nu enligt PEP8
   """

if __name__ == '__main__':
    #Start mainloop
    # app = wx.App(redirect=True,filename="Stalbalk.log")
    app = wx.App()
    c = Controller()
    app.MainLoop()