# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx


class EditSectionDialog(wx.Dialog):

    def __init__(self, parent, section_names_list):
        wx.Dialog.__init__(self, parent, title="Modifiera sektion")
        self.panel = wx.Panel(self)
        self.choice_list = section_names_list

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.create_input_widgets()
        self.create_buttons_sizer()

        self.panel.SetSizer(self.main_sizer)
        self.panel.Fit()
        self.Fit()

    def create_input_widgets(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self.panel, 0, 'Välj tvärsnitt:')
        self.choice_widget = wx.Choice(self.panel, style=wx.CB_SORT, choices=self.choice_list, size=(120,-1))

        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(self.choice_widget, 0, wx.EXPAND | wx.ALL, 5)

        self.main_sizer.Add(sizer, 0, wx.ALL, 10)

    def create_buttons_sizer(self):
        ok_btn = wx.Button(self.panel, wx.ID_ANY, 'OK')
        cancel_btn = wx.Button(self.panel, wx.ID_ANY, 'Cancel')

        button_sizer = wx.BoxSizer()
        button_sizer.Add(ok_btn, 0, wx.ALL, 5)
        button_sizer.Add(cancel_btn, 0, wx.ALL, 5)

        self.main_sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 5)

        self.Bind(wx.EVT_BUTTON, self.on_ok, ok_btn)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, cancel_btn)

    def on_ok(self, event):
        self.chosen_section_name = self.choice_widget.GetString(self.choice_widget.GetSelection())
        self.EndModal(True)

    def on_cancel(self, event):
        self.EndModal(False)