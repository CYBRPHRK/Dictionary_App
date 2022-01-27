# Dictionary_App
-----

This is a data dictionary app. In this app, you can search the meaning of any existing word and also, if you make some spelling mistakes, it checks for the similar word and confirm it to show the specific results(meaning). This app is build in Python using json and Tkinter GUI.

### Libraries

The libraries used in this app includes:

* **json** to load the data from a JSON file.
* **difflib** to get close matches of a word if not found.
* **tkinter** to create a GUI interface to interact with the app.

### Main Files: Project Structure

```sh
├── README.md
├── Dictionary_App.py --> The main driver of the app. It includes the code behind the app.
├── data.json --> Contains all the data for the dictionary in json format.
└── .gitignore --> To restrict the extra files from uploading to the repository.
```

### How to run the app

All you need is to [install Python](https://www.python.org/downloads/), if you haven't already, as all the libraries used in this app are pre-installed in Python. Latest testing is done in Python 3.9.1.

To run the app through Command Prompt / Terminal:
```
cd PATH_FOR_DICTIONARY_APP
python3 Dictionary_App.py
```

Or you can also run the app through IDEs like Virtual Studio, Virtual Studio Code, PyCharm, Python IDLE shell and more.
