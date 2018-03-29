# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx

class AddISectionDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, title = "Lägg till section", size = (300,300))
        self.panel = wx.Panel(self)

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.main_sizer)


        self.input_dict = {}

        self.create_buttons_sizer()


    def create_input_widgets(self):
        widget_dict = {'Överfläns': ['Bredd [mm]', 'Tjocklek [mm]'],
                       'Liv': ['Bredd [mm]', 'Tjocklek [mm]'],
                       'Underfläns':['Bredd [mm]', 'Tjocklek [mm]']}

        for key, labels in widget_dict.iteritems():
            outher_box = wx.StaticBox(self, -1, key)
            sizer = wx.StaticBoxSizer(outher_box, wx.HORIZONTAL)

            for text in labels:
                text_on_panel = wx.StaticText(self, -1, text[0], 0, wx.ALL, 5)
                self.input_dict[key + ' ' + text] = wx.TextCtrl(self.panel, wx.ID_ANY, '')
                sizer.Add(text, 0, wx.ALL, 5)


    def create_buttons_sizer(self):
        ok_btn = wx.Button(self.panel, wx.ID_ANY, 'OK')
        cancel_btn = wx.Button(self.panel, wx.ID_ANY, 'Cancel')

        button_sizer = wx.BoxSizer()
        button_sizer.Add(ok_btn, 0, wx.ALL, 5)
        button_sizer.Add(cancel_btn, 0, wx.ALL, 5)

        self.main_sizer.Add(button_sizer, 0, wx.ALL, 5)

        self.Bind(wx.EVT_BUTTON, self.on_ok, ok_btn)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, cancel_btn)

    def on_ok(self, event):
        pass

    def on_cancel(self, event):
        self.Close()
