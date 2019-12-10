"""
Created on Fri Nov 15 11:06:39 2019

@author: Roberto Bellarosa
"""

'''
The client shows an interface where put the user id and date to calculate
reputation, data are saved in a file json a sent to the server.
After, the interface shows result.
'''

#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 16, 2019 08:07:11 PM CET  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from PIL import Image, ImageTk

from tkinter import messagebox

import unknown_support
import os.path
from data_handler import data_handler
import requests
import json
from result.result_interface import result_gui

max_user_id = 12462842

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    unknown_support.set_Tk_var()
    top = ff (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_ff(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    unknown_support.set_Tk_var()
    top = ff (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_ff():
    global w
    w.destroy()
    w = None

class ff:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Calibri} -size 13 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("500x425+646+245")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(0, 0)
        top.title("Stack Overflow Client")
        top.configure(background="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.047, height=26, width=82)
        self.Label1.configure(background="white")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''User id:''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.006, rely=0.141, height=28, width=113)
        self.Label2.configure(background="white")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Select a date:''')

        self.TCombobox1 = ttk.Combobox(top,state="readonly")
        self.TCombobox1.place(relx=0.24, rely=0.141, relheight=0.061
                , relwidth=0.174)
        self.value_list = ["2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008"]
        self.TCombobox1.configure(values=self.value_list)        
        self.TCombobox1.configure(font=font9)
        self.TCombobox1.configure(background="#efefef")
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(cursor="fleur")
        self.TCombobox1.current(0)

        self.TCombobox2 = ttk.Combobox(top,state="readonly")
        self.TCombobox2.place(relx=0.44, rely=0.141, relheight=0.061
                , relwidth=0.114)
        self.value_list = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(font=font9)
        self.TCombobox2.configure(background="#efefef")
        self.TCombobox2.configure(takefocus="")
        self.TCombobox2.configure(cursor="fleur")
        self.TCombobox2.current(0)

        self.TCombobox3 = ttk.Combobox(top,state="readonly")
        self.TCombobox3.place(relx=0.6, rely=0.141, relheight=0.061
                , relwidth=0.114)
        self.value_list = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14",
                           "15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(font=font9)
        self.TCombobox3.configure(background="#efefef")
        self.TCombobox3.configure(takefocus="")
        self.TCombobox3.current(0)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.16, rely=0.047,height=24, relwidth=0.548)
        self.Entry1.configure(background="#efefef")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font9)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        
        self.Button1 = tk.Button(top, command=start_calc)
        self.Button1.place(relx=0.32, rely=0.282, height=63, width=180)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#efefef")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Estimate Reputation!''')
                            
        def add_to_list():
            user_id = self.Entry1.get()
            year = self.TCombobox1.get()
            month = self.TCombobox2.get()
            day = self.TCombobox3.get()
            date = year + "-" + month + "-" + day
            try:
                if(int(user_id) >= 0 and int(user_id) <= max_user_id):
                    my_json.update_json(user_id,date)
                    messagebox.showinfo("Message", "User added to the list successfully!")
                else:
                    messagebox.showerror(None, "Wrong user id!")
            except:
                messagebox.showerror(None,"User id wrong, please insert a correct number!")
                
        
        def canc():
            self.Entry1.delete(0,tk.END)
            self.Entry1.insert(0,"")
            self.TCombobox1.current(0)
            self.TCombobox2.current(0)
            self.TCombobox3.current(0)

        self.Button2 = tk.Button(top, command=canc)
        self.Button2.place(relx=0.32, rely=0.518, height=63, width=180)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#efefef")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Reset''')

        self.Button3 = tk.Button(top, command=add_to_list)
        self.Button3.place(relx=0.32, rely=0.753, height=63, width=180)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#efefef")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text=''' Add to list''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.76, rely=0.024, height=80, width=96)
        self.Label3.configure(background="#efefef")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        
        
        photo_location = os.path.join(prog_location,"/somicro.PNG")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img0)
        self.Label3.configure(relief="sunken")
        self.Label3.configure(text='''Label''')
        
#Here the part of code that work for the web service
def start_calc():
    resp =""
    if(my_json.is_null()):
        messagebox.showerror(None, "The list is empty!\nEnter at least one user!")
    else:
        try:
            messagebox.showinfo("WARNING!","Wait for the end of the reconstruction of the reputation!\n(maximum 30 seconds per user)")
            resp = send_request_post()
            if(resp.status_code == requests.codes.ok):
                result_json = resp.json
                estimate()
                my_json.reset()
                result_json.reset()
            else:
                messagebox.showerror(None,"Something wrong!")
        except:
            print(resp)
            messagebox.showerror(None, "Connection could not be established. Persistent rejection of the target computer!")


def send_request_post():
    url = "http://127.0.0.1:8000/information"
    data = my_json.give_json()
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type':'application/json'})
    return response

def estimate():
    result_gui()
    
my_json = data_handler()
my_json.to_json()

def write_result_file(response):
    result = response.json
    file = "result_file"
    with open(file, "w") as to_write:
        json.dump(result, to_write)

if __name__ == '__main__':
    vp_start_gui()

