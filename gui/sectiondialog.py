# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx

class AddISectionDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, title = "Lägg till section", size = (300,300))
        self.panel = wx.Panel(self)

        self.create_buttons()

    def create_buttons(self):
        ok_btn = wx.Button(self.panel, wx.ID_ANY, 'OK')
        cancel_btn = wx.Button(self.panel, wx.ID_ANY, 'Cancel')

        button_sizer = wx.BoxSizer()
        button_sizer.Add(ok_btn, 0, wx.ALL, 5)
        button_sizer.Add(cancel_btn, 0, wx.ALL, 5)

        self.Bind(wx.EVT_BUTTON, self.on_ok, ok_btn)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, cancel_btn)

        self.panel.SetSizer(button_sizer)

    def on_ok(self, event):
        pass

    def on_cancel(self, event):
        self.Close()
