# !/user/bin/env Python3
import tkinter as tk
from tkinter import filedialog, dialog
import re
import os
import csv
from functions import loadTwee, findKey

window = tk.Tk()
window.title('Title') # Title
window.geometry('1000x500') # Window Size
text1 = tk.Text(window, width=100, height=15, bg='white', font=('Arial', 12))
entry1=tk.Entry(window,width=50, bg="white",fg="black")

file_path = file_text = ''
twi = list()
data = dict()
keys = list()

def load_csv(path):
    documents_list = []
    if file_path is not None:
        with open(file=file_path, newline='',encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                documents_list.append(row['content'])
        print("Total Number of Documents:",len(documents_list))
    return documents_list

def open_file():
    global file_path
    global file_text
    global twi
    global data

    file_path = filedialog.askopenfilename(title=u'Choose file', initialdir=(os.path.expanduser('H:/')))
    print('Open File：', file_path)

    file_text = load_csv(file_path)
    
    for i in range(len(file_text)):
        file_text[i] = file_text[i].lower()
        file_text[i] = re.sub("[\.\!\[\]\-\=\;\{\}\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]", "",file_text[i])
        twi.append(file_text[i].split())	
    
    data = loadTwee(twi)
    dialog.Dialog(None, {'title': 'File Open', 'text': 'Load Complete!', 'bitmap': 'warning', 'default': 0,
                'strings': ('OK', 'Cancle')})
    print('Load Complete!')

 
def save_file():
    global file_path
    global file_text
    file_path = filedialog.asksaveasfilename(title=u'Store File')
    print('Store File：', file_path)

    output = text1.get('1.0', tk.END)
    if file_path is not None:
        with open(file=file_path, mode='w+', encoding='utf-8') as file:

            file.writelines(str(len(twi)))
            file.writelines("\n")
            for line in twi:
                outline = str(len(line))
                for word in line:
                    outline = outline + " " + word
                file.writelines(outline)
                file.writelines("\n")

        text1.delete('1.0', tk.END)
        dialog.Dialog(None, {'title': 'File Modified', 'text': 'Store Complete!', 'bitmap': 'warning', 'default': 0,
                'strings': ('OK', 'Cancle')})
        print('Store Complete!')

def search():
    global keys
    global data
    if(text1.get('1.0', tk.END)!=""):
        text1.delete('1.0', tk.END)
    str1 = entry1.get()
    str1 = str1.lower()
    str1 = re.sub("[\.\!\[\]\-\=\;\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",str1)
    keys = str1.split()
    result = findKey(data,keys)
    for i in result:
        if(i == -1):
            break
        text1.insert('insert', twi[i])	
        text1.insert('insert', "\n\n")

def main():
    
    text1.pack()

    bt1 = tk.Button(window, text='Open File', width=15, height=2, command=open_file)
    bt2 = tk.Button(window, text='Store File', width=15, height=2, command=save_file)
    bt1.pack()
    bt2.pack()
            
    entry1.pack()

    button=tk.Button(window,text="Submit", width=15, height=2, command=search) 
    button.pack()#load window

    window.mainloop() # Display

if __name__ == "__main__":
    main()