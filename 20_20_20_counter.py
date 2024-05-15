from customtkinter import *
from tkinter import *
import winsound



set_appearance_mode("dark")
set_default_color_theme("green") 

root = CTk()
root.geometry('250x200')
root.title('20/20/20')
root.attributes("-alpha", 0.9)


isRunning = False
workTime = 1259

def start():
    global isRunning
    if not isRunning:
        isRunning = True
    timeLabel.configure(font = ('Book Antiqua', 25))
    infoLabel.configure(font = ('Freestyle script', 35))
    counter()

    
def stop():
    global isRunning 
    if isRunning:
        isRunning = False

def reset():
    global isRunning
    global workTime
    if isRunning:
        isRunning = False
    workTime = 10
    timeText = str(workTime) + ' MIN'
    timeLabel.configure(text = timeText)

def start_rest():
    global workTime
    workTime -= 1
    restButton.place_forget()
  

def counter():
        global workTime
    
        if isRunning:
            if workTime > 1255:
                timeText = str(workTime//60) + ' MIN'
                infoText = 'Start work'
                workTime -= 1
            elif workTime > 60:
                timeText = str(workTime//60) + ' MIN'
                infoText = 'work'
                workTime -= 1
            elif (workTime == 60):
                timeText = ' '
                infoText = 'Start rest'
                winsound.Beep(500,100)
                restButton.place(relx = 0.5, rely = 0.3, relwidth = 0.3, relheight = 0.15, anchor = 'center')
            elif (workTime < 60 and workTime > -1):
                timeText = str(workTime) + ' SEC'
                infoText = 'rest'
                workTime -= 1
            elif workTime == -1:
                timeText = '  '
                infoText = '   '
                workTime += 1260
                
            
    
            timeLabel.configure(text = timeText)
            infoLabel.configure(text = infoText)
                        
            root.after(1000, counter)
            

           

timeLabel = CTkLabel(root, text = 'Hello!', justify = 'center', width = 200, font= ('Freestyle script', 50))
timeLabel.place(relx = 0.5, rely = 0.3, relwidth = 0.8, relheight = 0.3, anchor = 'center')


infoLabel = CTkLabel(root, text = 'Ready to start your work?', font = ('Calibri', 15))
infoLabel.place(relx = 0.5, rely = 0.55, relwidth = 0.8, relheight = 0.3, anchor = 'center')

restButton = CTkButton(root, text = 'Start rest', command = start_rest, font = ('Calibri', 15), corner_radius=10)


startButton = CTkButton(root, text = 'Start', command = start, font = ('Calibri', 15), corner_radius=10)
startButton.place(relx = 0.25, rely = 0.85, relwidth = 0.22, relheight = 0.15, anchor = 'center')

stopButton = CTkButton(root, text = 'Stop', command = stop, font = ('Calibri', 15), corner_radius=10)
stopButton.place(relx = 0.5, rely = 0.85, relwidth = 0.22, relheight = 0.15, anchor = 'center')

resetButton = CTkButton(root, text = 'Reset', command = reset, font = ('Calibri', 15), corner_radius=10)
resetButton.place(relx = 0.75, rely = 0.85, relwidth = 0.22, relheight = 0.15, anchor = 'center')

root.after(201, lambda :root.iconbitmap('C:\\Users\\prius\\Downloads\\hd.ico'))
root.mainloop()


