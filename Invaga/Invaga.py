import tkinter as tk
from tkinter  import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def Main():

	input1 = raw_input("Web Address:")

	window = tk.Tk()

	window.configure(background="black")

	window.title("inbredspecies")

	window.geometry("620x520")

	title = tk.Label(bg="black", fg="white", text="Web devs suck - inbredspecies")
	title.place(x=210, y=60)

	Links = "--#Links#--"
	Paragrahps = "--#Paragrahps#--"
	Comments = "--#Comments#--"
	hypertext1 = "--#Text[<h1>#--"

	r = requests.get(input1)

	soup = BeautifulSoup(r.content, "lxml")

	for link1 in soup.find_all("a"):
		for link2 in soup.find_all("p"):
			for link3 in soup.find_all("br"):

				results = Links, "\n\n", link1, "\n\n", Paragrahps, "\n\n", link2, "\n\n", Comments, "\n\n", hypertext1
		text = tk.Text(height=30, width=80)
		text.place(x=30, y=80)
		text.insert(tk.END, results,)
	scroll = tk.Scrollbar()

	window.mainloop()

Main()
