# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import gui
import wx

#Regler
"""
class NameConvention:

    def __init__(self, input):
        self.new_property = input

    def create_new(self, imp):

        använd inga get setters om det inte gör något innan.
        Tabs är spaces
        Kör nu enligt PEP8
   """

if __name__ == '__main__':
    #Start mainloop
    # app = wx.App(redirect=True,filename="Stalbalk.log")
    app = wx.App()
    frame = gui.MainFrame()
    frame.Show()
    app.MainLoop()