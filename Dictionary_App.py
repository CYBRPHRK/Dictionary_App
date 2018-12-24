import json
import difflib as dl
import tkinter as tk


class Dict:
    def __init__(self):
        self.word = ""
        self.temp = ""
        self.mean = ""
        self.checkl = []
        self.e2 = tk.Entry(root)
        self.label3 = tk.Label(root)
        self.button3 = tk.Button(root)
        self.label4 = tk.Label(root)
    def meaning(self,k):
        if k in data.keys():
            return data[k]
        elif k.lower() in data.keys():
            return data[k.lower()]
        elif k.title() in data.keys():
            return data[k.title()]
        elif k.upper() in data.keys():
            return data[k.upper()]
        elif len(dl.get_close_matches(k.lower(), data.keys(), cutoff = 0.8)) > 0:
            self.label3 = tk.Label(root, justify=tk.LEFT, text = "Did you mean %s? If yes, enter 'Y' or else enter anything." % (dl.get_close_matches(k.lower(), data.keys(), cutoff = 0.8)[0]))
            self.label3.pack()
            self.temp = dl.get_close_matches(k.lower(), data.keys(), cutoff = 0.8)[0]
            self.e2 = tk.Entry(root)
            self.e2.pack()
            self.button3 = tk.Button(root, text='OK', command=self.choiceButton, width=15)
            self.button3.pack()
        else:
            return ("Word Not found. Try Again.")

    def choiceButton(self):
        choice = self.e2.get().lower()
        if(choice == 'y'):
            self.mean = self.meaning(dl.get_close_matches(self.temp, data.keys(), cutoff = 0.8)[0])
            self.display()
        else:
            self.display("Word Not found. Try Again.")

    def find(self):
        checkb = self.button3
        if checkb in root.winfo_children():
            self.e2.destroy()
            self.label3.destroy()
            self.button3.destroy()
            if(type(self.mean) == list):
                i=0
                for m in self.mean:
                    self.checkl[i].destroy()
                    i+=1
            else:
                self.label4.destroy()
        elif self.label4 in root.winfo_children():
            if(type(self.mean) == list):
                i=0
                for m in self.mean:
                    self.checkl[i].destroy()
                    i+=1
            else:
                self.label4.destroy()
        self.word = e1.get()
        self.mean = self.meaning(self.word)
        self.display()

    def display(self):
        if(type(self.mean) == list):
            self.checkl = []
            i=0
            for m1 in self.mean:
                self.label4 = tk.Label(root, justify=tk.LEFT, text = m1)
                self.checkl.append(self.label4)
                self.checkl[i].pack()
                i+=1
        else:
            self.label4 = tk.Label(root, justify=tk.LEFT, text = self.mean)
            self.label4.pack()

root = tk.Tk()
root.title("Dictionary")

data = json.load(open("data.json"))
d1 = Dict()

message = "A program developed by CyberPhreak"
tk.Label(root, justify=tk.LEFT, text = message, font="TimesNewRoman 12").pack()
tk.Label(root, justify=tk.LEFT, text = "Enter a word: ").pack()

e1 = tk.Entry(root)
e1.pack()

tk.Button(root, text='Find', command=d1.find, width=15).pack()
tk.Button(root, text='Quit', command=root.destroy, width=15).pack()

