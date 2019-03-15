import urllib.request, urllib.error
from bs4 import BeautifulSoup
import tkinter as tk

def scrape():
    collection = []
    url = "https://tarumi-railway.com/news"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    page = soup.find('div', id = "page_news")
    date = page.findAll('p', class_="date")
    time = page.findAll('p', class_="time")
    cont = page.findAll('p', class_="title")

    collection.clear()
    for i in range(4):
        print(date[i].string,' : ',time[i].string,' : ',cont[i].string)
        Str = date[i].string + ' : ' + time[i].string + ' : ' + cont[i].string
        collection.append(Str)
    return collection

with open("ScaduleMemo.txt") as file:
    memoStr = file.read()

collection = scrape()

root = tk.Tk()
root.resizable(0,0)
root.title('樽見鉄道Info')

frame = tk.Frame(root, width = 300, height = 150)
frame.grid()
label = tk.Label(frame, text = '運行情報リスト')
label.grid(row = 0, column = 0, sticky = tk.SW)

val = tk.StringVar(value = collection)
list = tk.Listbox(frame, listvariable = val, height = 8, width = 40)
list.grid(row = 1, column = 0, padx = 5)

scrollbar = tk.Scrollbar(frame, orient = 'vertical', command = list.yview)
list['yscrollcommand'] = scrollbar.set
scrollbar.grid(row = 1, column = 1, sticky = tk.N + tk.S)
scrollbar = tk.Scrollbar(frame, orient = 'horizontal', command = list.xview)
list['xscrollcommand'] = scrollbar.set
scrollbar.grid(row = 2, column = 0, sticky = tk.W + tk.E + tk.N)

def exit_clicked():
    memoStr = memo.get('1.0', 'end -1c')
    with open("ScaduleMemo.txt", mode='w') as file:
        file.write(memoStr)
    root.quit()
exitbutton = tk.Button(frame, text = 'Exit', command = exit_clicked, width = 8)
exitbutton.grid(row = 2, column = 3, sticky = tk.E, padx = 5, pady = 5)

def reload_clicked():
    scrape()
reload = tk.Button(frame, text = 'Reload', command = reload_clicked, width = 8)
reload.grid(row = 2, column = 2, sticky = tk.E, padx = 5, pady = 5)

def cltb():
    memo.delete('1.0', 'end')
textclear = tk.Button(frame, text = '✖', command = cltb)
textclear.grid(row = 0, column = 3, sticky = tk.E)

memoL = tk.Label(frame, text = 'memo(save with Finish)')
memoL.grid(row = 0, column = 2, sticky = tk.SW, columnspan = 2)
memo = tk.Text(frame, height = 8, width = 23)
memo.grid(row = 1, column = 2, padx = 5, pady = 0, sticky = tk.N, columnspan = 2)
memo.insert('1.0', memoStr)

root.mainloop()
