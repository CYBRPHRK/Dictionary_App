import json
import difflib as dl
import tkinter as tk


class Dict:
    def __init__(self):
        self.word = ""
        self.temp = ""
        self.e2 = ""
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
            tk.Label(root, justify=tk.LEFT, text = "Did you mean %s? If yes, enter 'Y' or else enter anything." % (dl.get_close_matches(k.lower(), data.keys(), cutoff = 0.8)[0])).pack()
            self.temp = dl.get_close_matches(k.lower(), data.keys(), cutoff = 0.8)[0]
            self.e2 = tk.Entry(root)
            self.e2.pack()
            tk.Button(root, text='OK', command=self.choiceButton, width=15).pack()
        else:
            return ("Word Not found. Try Again.")

    def choiceButton(self):
        choice = self.e2.get().lower()
        if(choice == 'y'):
            mean = self.meaning(dl.get_close_matches(self.temp, data.keys(), cutoff = 0.8)[0])
            self.display(mean)
        else:
            self.display("Word Not found. Try Again.")

    def find(self):
        self.word = e1.get()
        mean = self.meaning(self.word)
        self.display(mean)

    def display(self,m):
        if(type(m) == list):
            i = 0;
            for m1 in m:
                tk.Label(root, justify=tk.LEFT, text = m1).pack()
                i+=1
        else:
            tk.Label(root, justify=tk.LEFT, text = m).pack()

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


