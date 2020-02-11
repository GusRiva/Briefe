import requests
import tkinter as tk
import xml.etree.ElementTree as ET
import os 
import webbrowser



dir_path = os.path.dirname(os.path.realpath(__file__))
registerFile = dir_path + '/../../register/register_person.xml'

def sucheGND(searchTerm, v):
    oldRadios = radioFrame.winfo_children()
#    oldGndLinks = gndLinksCol.winfo_children()
    for olr in oldRadios:
        olr.destroy()
#    for oll in oldGndLinks:
#    	olr.destroy()
    response = requests.get(
        "https://lobid.org/gnd/search?q=" + searchTerm + "&filter=type:Person&format=json")
    
    searchResult = []

    for item in response.json()['member']:
        searchResult.append( (item['preferredName'], item['gndIdentifier']) )

    for val, tup in enumerate(searchResult):
        tk.Radiobutton(radioFrame,
                       text= tup[0],
                       height = 2,
                       # padx=20,
                       variable=v,
                       # command= StoreChoice,
                       value= tup[0] + "§" + tup[1]).grid(row = 1 + val, column = 1, sticky = tk.W)
        lbl = tk.Button(radioFrame, text = tup[1], padx = 2, borderwidth = 0, command = lambda j = tup[1]: openURL(j) )
        lbl.grid(row = 1 + val, column = 2, sticky = tk.W)
        

    v.set(searchResult[0][0] +"§" + searchResult[0][1]) # select the first radio
    buttonAdd.config(state="normal")

def updateRegister(selName, selGND, register):
    tree = ET.parse(register)
    root = tree.getroot()
    newPlace = ET.Element('person')
    newPlaceName = ET.SubElement(newPlace, 'persName').text = selName
    newIdno = ET.SubElement(newPlace, 'idno').text = selGND
    root.append(newPlace)

    #To sort the entries
    data = []
    for elem in root:
        key = elem.findtext('persName')
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

def openURL(idno):
	webbrowser.open_new("http://d-nb.info/gnd/" + idno)

master = tk.Tk()
v = tk.StringVar()
master.geometry("900x500") #Width x Height
tk.Label(master,
     text="Suche nach: ").grid(row=0,
                               padx=20,
                               pady=20)

e1 = tk.Entry(master, width=50)
e1.bind('<Return>', get )
e1.focus_set()

e1.grid(row=0, column=2,
        columnspan=2,
#        pady= 4,
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

#gndLinksCol = tk.Frame(master)
#gndLinksCol.grid(row=1, column=3, sticky=tk.W)



tk.mainloop()





