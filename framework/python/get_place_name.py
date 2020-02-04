import requests
import tkinter as tk
import xml.etree.ElementTree as ET

registerFile = './../../register/register_place.xml'

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
                       # command= StoreChoice,
                       value= tup[0] + "§" + tup[1]).grid(row=1 + val, column=1, sticky=tk.W)

    v.set(searchResult[0][0] +"§" + searchResult[0][1])
    buttonAdd.config(state="normal")

def updateRegister(selName, selGND, register):
    tree = ET.parse(register)
    root = tree.getroot()
    newPlace = ET.Element('place')
    newPlaceName = ET.SubElement(newPlace, 'placeName').text = selName
    newIdno = ET.SubElement(newPlace, 'idno').text = selGND
    root.append(newPlace)

    #To sort the entries
    data = []
    for elem in root:
        key = elem.findtext('placeName')
        data.append((key, elem))
    data.sort()
    # insert the last item from each tuple
    root[:] = [item[-1] for item in data]

    tree.write(registerFile)

def get(event):
    sucheGND(event.widget.get(), v)

def addEntry():
    selectedName = v.get().split('§')[0]
    selectedGND = v.get().split('§')[1]
    updateRegister(selectedName,selectedGND, registerFile)
    master.quit()

master = tk.Tk()
v = tk.StringVar()
master.geometry("600x600") #Width x Height
tk.Label(master,
     text="Suche nach: ").grid(row=0,
                               padx=20,
                               pady=20)

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





