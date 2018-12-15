import tkinter
import capture
import take_photo
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
    capture.capture(name, eye.get(), threshold)

def onPhoto(event):
    take_photo.take_photo()

def eventhandler(event):
    root.quit()    

# Configure the UI
root = tkinter.Tk()
root.title("capture")
root.bind('<Escape>', eventhandler)

photo = tkinter.Label(root, text="photo", relief="groove", width=15, height=10)
photo.bind('<ButtonRelease>', onPhoto)
photo.grid(padx=10, pady=10, row=0, columnspan=3)

tkinter.Label(root, text="Dog name:").grid(padx=10, pady=10, row=1, column=0)

nameEntry = tkinter.Entry(root)
nameEntry.grid(padx=10, pady=10, row=1, column=1, columnspan=2)

tkinter.Label(root, text="Threshold:").grid(padx=10, pady=10, row=2, column=0)

value = tkinter.IntVar()
threEntry = tkinter.Entry(root, textvariable = value)
value.set(200)
threEntry.grid(padx=10, pady=10, row=2, column=1, columnspan=2)

tkinter.Label(root, text="Eye:").grid(padx=10, pady=10, row=3, column=0)

eye = tkinter.StringVar()
eye.set("left")
tkinter.Radiobutton(root, text="left", variable=eye, value="left").grid(padx=10, pady=10, row=3, column=1) 
tkinter.Radiobutton(root, text="right", variable=eye, value="right").grid(padx=10, pady=10, row=3, column=2) 

errLabel = tkinter.Label(root, fg='red')
errLabel.grid(padx=10, pady=10, row=4, columnspan=3)

tkinter.Button(root, text="Start", command = onClick).grid(padx=10, pady=10, row=5, columnspan=3)

# Show the UI
root.mainloop() 