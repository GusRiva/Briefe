import requests
import json
import tkinter as tk


# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# response = requests.get("https://lobid.org/gnd/search?q=waldorf&filter=type:TerritorialCorporateBodyOrAdministrativeUnit&format=json")
# print(response.status_code)
# resultDict = {}
#
# for item in response.json()['member']:
#     resultDict[item['preferredName']]= item['gndIdentifier']

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

res = tk.Label(master)
res.grid(row=0, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)



tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()




