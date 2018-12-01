import tkinter
import capture
import os

def onClick():
    name = nameEntry.get().strip()
    if not name:
        errLabel["text"] = 'Please input a dog name.'
        return
    try: 
        os.makedirs(name, exist_ok=False)
    except OSError:
        errLabel["text"] = 'Dog name already exists.'
        return
        
    try:
        threshold = int(threEntry.get())
    except ValueError:
        errLabel["text"] = 'Please input valid threshold.'
        return
    capture.capture(name, threshold)

def eventhandler(event):
    root.quit()    

# Configure the UI
root = tkinter.Tk()
root.title("capture")
root.bind('<Escape>', eventhandler)

tkinter.Label(root, text="Dog name:").grid(padx=10, pady=10, row=0, column=0)

nameEntry = tkinter.Entry(root)
nameEntry.grid(padx=10, pady=10, row=0, column=1)

tkinter.Label(root, text="Threshold:").grid(padx=10, pady=10, row=1, column=0)

value = tkinter.IntVar()
threEntry = tkinter.Entry(root, textvariable = value)
value.set(200)
threEntry.grid(padx=10, pady=10, row=1, column=1)

errLabel = tkinter.Label(root, fg='red')
errLabel.grid(padx=10, pady=10, row=3, columnspan=2)

tkinter.Button(root, text="Start", command = onClick).grid(padx=10, pady=10, row=4, columnspan=2)

# Show the UI
root.mainloop() 