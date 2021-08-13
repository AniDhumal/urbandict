import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import pymysql.cursors


#Pre-defined height and width parameters for cleaner coding 
HEIGHT = 700
WIDTH = 800


#This function will be used to display the data accordingly in the label
def display_data(data):
    try:
        word = data[0][0]
        meaning1 = data[0][1]
        meaning2 = data[0][2]
        meaning3 = data[0][3]
        final_str = 'The word you have searched for is: %s \n\n\nThe meaning is:\n\n%s\n\n%s\n\n%s' %(word, meaning1, meaning2, meaning3)
    except:
        final_str = 'Sorry this word does not exist yet'
        print(final_str)

    return final_str


#This function will be called once the button is clicked. All the data fetching part from MySQL will be here
def searchForWord(entry):
    print("The word searched is:",entry)
    #Connects to the MySQL sever with the required credentials
    db = pymysql.connect(host="localhost", user="root", password="root", database="final")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM final where words=%s", entry) #The MySQL query to fetch data from our database
    data = cursor.fetchall()
    print(data)
    print(data[0][1])
    print(data[0][2])
    print(data[0][3])
    label['text'] = display_data(data) #Displaying the meanings in the label widget



#The main part of GUI starts from here
root = tk.Tk()
root.title("Urban Dictionary")

#Canvas is the overall screen that will be created in which over widgets will lie
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#Background image that is used in the GUI to make it more interactive
background_image = ImageTk.PhotoImage(Image.open('dicti.png'), size = HEIGHT)
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

#A frame is added to make it look better and cleaner
frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

#This is a textbox which will take the entry from the user
entry = tk.Entry(frame, font=('Comic Sans MS', 18))
entry.place(relwidth = 0.65, relheight = 1)

#The search button which will call the respective function to perform Fetch part
button = tk.Button(frame, text = "Search", font=('Comic Sans MS', 18), command = lambda: searchForWord(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

#Another frame to make it look better and cleaner
lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

#A Label which will display the contents fetched from the database
label = tk.Label(lower_frame, font=('Comic Sans MS', 18), anchor = 'nw', justify='left', bd=4, wraplength=570)
label.place(relwidth = 1, relheight = 1)

#Exiting the GUI
root.mainloop()