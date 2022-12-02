import logging
from typing import Optional

import wx


class AppWindow(wx.Frame):
    """Class containing the required functionality of a basic ListBox App"""

    def __init__(self, parent: Optional[wx.Frame], title: str) -> None:
        super().__init__(parent, title=title)
        self.SetSize((400, 400))

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.hbox, flag=wx.ALL | wx.CENTER)
        self.listbox: Optional[wx.ListBox] = None
        self.textbox: Optional[wx.TextCtrl] = None

        # layout
        self.add_label()
        self.add_listbox()
        self.add_textbox()
        self.add_buttons()

        self.SetSizer(self.vbox)
        self.Center()
        self.Show()

    def add_label(self) -> None:
        """Add the topmost label to the GUI"""
        label = wx.StaticText(self, label="Basic List")
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True)
        label.SetFont(font)
        self.hbox.Add(label, flag=wx.ALL, border=10)

    def add_listbox(self) -> None:
        """Add the main listbox that will contain all the items"""
        self.listbox = wx.ListBox(self, size=(120, 150))
        self.vbox.Add(self.listbox, flag=wx.ALL | wx.CENTER, border=5)

    def add_textbox(self) -> None:
        """Add the main textbox used for adding items to the listbox"""
        label = wx.StaticText(self, label="List item name")
        self.textbox = wx.TextCtrl(self)
        self.vbox.Add(label, flag=wx.ALL | wx.CENTER)
        self.vbox.Add(self.textbox, flag=wx.ALL | wx.CENTER, border=5)

    def add_buttons(self) -> None:
        """Add the buttons for performing basic operations on the listbox"""
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        insert_button = wx.Button(self, label="Insert Item")
        insert_button.Bind(wx.EVT_BUTTON, self.on_insert_btn_click)
        hbox.Add(insert_button, flag=wx.ALL | wx.CENTER, border=5)

        remove_button = wx.Button(self, label="Remove Item")
        remove_button.Bind(wx.EVT_BUTTON, self.on_remove_btn_click)
        hbox.Add(remove_button, flag=wx.ALL | wx.CENTER, border=5)

        self.vbox.Add(hbox, flag=wx.ALL | wx.CENTER)

        rename_button = wx.Button(self, label="Rename Item")
        rename_button.Bind(wx.EVT_BUTTON, self.on_rename_btn_click)
        self.vbox.Add(rename_button, flag=wx.ALL | wx.CENTER, border=5)

    def on_insert_btn_click(self, _: wx.CommandEvent) -> None:
        self.listbox.Append(self.textbox.GetValue())

    def on_remove_btn_click(self, _: wx.CommandEvent) -> None:
        selected_element_idx: int = self.listbox.GetSelection()
        if selected_element_idx != wx.NOT_FOUND:
            self.listbox.Delete(selected_element_idx)
        elif self.listbox.GetCount() == 0:
            logging.warning("ListBox is empty!")

    def on_rename_btn_click(self, _: wx.CommandEvent) -> None:
        selected_element_idx: int = self.listbox.GetSelection()
        if selected_element_idx != wx.NOT_FOUND:
            self.listbox.SetString(selected_element_idx, self.textbox.GetValue())
        elif self.listbox.GetCount() == 0:
            logging.warning("ListBox is empty!")
        else:
            logging.warning("No item was selected")


if __name__ == "__main__":
    app = wx.App()
    AppWindow(None, "ListBox App")
    app.MainLoop()
