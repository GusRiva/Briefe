import requests
import json
import tkinter as tk


# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

selectedName = ""
selectedGND = ""

def StoreChoice():
    selectedName = v.get().split('§')[0]
    selectedGND = v.get().split('§')[1]
    print((selectedGND))



def sucheGND(searchTerm, v):
    oldRadios = radioFrame.winfo_children()
    for olr in oldRadios:
        olr.destroy()
    print(searchTerm)
    response = requests.get(
        "https://lobid.org/gnd/search?q=" + searchTerm + "&filter=type:TerritorialCorporateBodyOrAdministrativeUnit&format=json")
    print(response.status_code)
    searchResult = []

    for item in response.json()['member']:
        searchResult.append( (item['preferredName'], item['gndIdentifier']) )

    print(searchResult)


    for val, tup in enumerate(searchResult):
        tk.Radiobutton(radioFrame,
                       text= tup[0],
                       # padx=20,
                       variable=v,
                       command= StoreChoice,
                       value= tup[0] + "§" + tup[1]).grid(row=1 + val, column=1, sticky=tk.W)

    v.set(searchResult[0][0] +"§" + searchResult[0][1])
    buttonAdd.config(state="normal")


master = tk.Tk()
v = tk.StringVar()
master.geometry("600x600") #Width x Height
tk.Label(master,
     text="Suche nach: ").grid(row=0,
                               padx=20,
                               pady=20)

def get(event):
    sucheGND(event.widget.get(), v)

def addEntry():
    print(selectedName, selectedGND)
    # master.quit()

e1 = tk.Entry(master, width=50)
e1.bind('<Return>', get )
e1.focus_set()

e1.grid(row=0, column=2,
        columnspan=2,
        pady= 4,
        sticky=tk.W)


tk.Button(master, text='Search'
          ,command= lambda: sucheGND(e1.get(),v)
          ).grid(row=0, column=4,
                 padx=10,
                 sticky=tk.W)

buttonAdd = tk.Button(master, text='Add',
          command= addEntry,
          state= 'disabled')
buttonAdd.grid(row=0, column=5, padx=10, sticky=tk.W)

radioFrame = tk.Frame(master)
radioFrame.grid(row=1, column=2, sticky=tk.W)



tk.mainloop()





