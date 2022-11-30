from typing import Optional

import wx


class AppWindow(wx.Frame):
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
        label = wx.StaticText(self, label="Basic List")
        self.hbox.Add(label, flag=wx.ALL, border=10)

    def add_listbox(self) -> None:
        self.listbox = wx.ListBox(self, size=(120, 150))
        self.vbox.Add(self.listbox, flag=wx.ALL | wx.CENTER, border=5)

    def add_textbox(self) -> None:
        self.textbox = wx.TextCtrl(self)
        self.vbox.Add(self.textbox, flag=wx.ALL | wx.CENTER, border=5)

    def add_buttons(self) -> None:
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        insert_button = wx.Button(self, label="Insert Item")
        insert_button.Bind(wx.EVT_BUTTON, self.on_insert_btn_click)
        hbox.Add(insert_button, flag=wx.ALL | wx.CENTER, border=5)

        remove_button = wx.Button(self, label="Remove Item")
        remove_button.Bind(wx.EVT_BUTTON, self.on_remove_btn_click)
        hbox.Add(remove_button, flag=wx.ALL | wx.CENTER, border=5)

        self.vbox.Add(hbox, flag=wx.ALL | wx.CENTER)

    def on_insert_btn_click(self, _: wx.CommandEvent) -> None:
        self.listbox.Append(self.textbox.GetValue())

    def on_remove_btn_click(self, _: wx.CommandEvent) -> None:
        selected_element = self.listbox.GetSelection()
        if selected_element != wx.NOT_FOUND:
            self.listbox.Delete(selected_element)
        else:
            print(f"Warning listbox is empty!")


if __name__ == "__main__":
    app = wx.App()
    AppWindow(None, "ListBox App")
    app.MainLoop()
