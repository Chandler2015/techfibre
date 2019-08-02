from tkinter import *



def click():
    #get the 3 keywords
    keyword1 = textentry1.get()  
    keyword2 = textentry2.get() 
    keyword3 = textentry3.get()
    
    #if nothing matched
    result = "No product found, please try other keywords."

    #3 lists after 3 keywords filtered 
    filtered_list1 = []
    filtered_list2 = []
    filtered_list3 = []
    key_result = []

    index = 0
    #search algorithm
    for value in values:
        key = keys[index]
        if keyword1 in value and keyword1 != "":          
            if key not in key_result:
                key_result.append(key)
            filtered_list1.append(key)
        if keyword2 in value and keyword2 != "":          
            filtered_list2.append(key)
            if key not in key_result:
                key_result.append(key)
        if keyword3 in value and keyword3 != "" :          
            filtered_list3.append(key)
            if key not in key_result:
                key_result.append(key)
        index += 1

    total_list = filtered_list1+filtered_list2+filtered_list3
    key_rank = {}
    for key in key_result:
        frequency = total_list.count(key)
        key_rank[key] = frequency
    
    key_rank = sorted(key_rank, key=key_rank.get, reverse=True)  

    #empty the text box
    output.delete(0.0, END)
    #show result 
    output.insert(END, key_rank)

#close the window
def leave():
    window.destroy()
    exit()

#database
data_dictionary = {"apple":"apple fruit red sweet","orange":"orange fruit yellow sour"
,"phone":"phone device android ios daily","laptop":"laptop device mac windows daily"}
keys = list(data_dictionary.keys())
values = list(data_dictionary.values())

window = Tk()
window.title("Techfibre")
window.configure(background = "black")

brand_photo = PhotoImage(file = "tech.png")
Label(window, image = brand_photo, bg = "black").grid(row=0,column =0,sticky = W)

Label(window, text = "Enter the keywords for the product: ",bg = "black",fg= "white").grid(row=3,column =0,sticky=W)

textentry1 = Entry(window,width = 20, bg = "white")
textentry1.grid(row = 5,column = 0,sticky = W)

textentry2 = Entry(window,width = 20, bg = "white")
textentry2.grid(row = 7,column = 0,sticky = W)

textentry3 = Entry(window,width = 20, bg = "white")
textentry3.grid(row = 9,column = 0,sticky = W)

Button(window,text = "Submit",width = 6,fg= "blue",command = click).grid(row=11,column=0,sticky = W)

Label(window, text = "The products most closely match you searched are: ",bg = "black",fg= "white").grid(row=13,column =0,sticky=W)

output = Text(window, width = 50, height = 3, wrap = WORD,background = "white")
output.grid(row = 15, column = 0, columnspan = 2, sticky = W)

Button(window,text = "Exit",width = 6,fg= "blue",command = leave).grid(row=17,column=0,sticky = E)





window.mainloop()