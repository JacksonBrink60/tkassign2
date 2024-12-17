from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser, filedialog
window = Tk()
window.geometry("600x550")
window.title("Alien Invader HQ Control Panel")
frametop = Frame(window, width=600)
frametop.pack()
Label(frametop, font=("Arial", 32), text="👽").pack()
framemid = Frame(window)
framemid.pack()
framebottom = Frame(window)
framebottom.pack()


def change():
    color = colorchooser.askcolor()
    spaceship_display.config(bg=color[1])
    status.config(text=f"Changed color of the spaceship to: {color[1]}")


def send():
    print(f"Alien Message:\n{message_alien_pilots.get(1.0, END)}")
    status.config(text="Message sent")


def open_file():
    file = filedialog.askopenfilename(
        title="open file", filetypes=(("Text File", "*.txt"), ("Any File", "*.*")))
    print(file)
    if file:
        with open(file, "r") as file:
            content = file.read()
            print(content)
            status.config(text="Opened file")


def launch_plan():
    lan = messagebox.askyesno(
        "Confirm Launch", f"Are you sure you want to launch {box.get(ACTIVE)}")
    if lan == True:
        print(f"{box.get(ACTIVE)} launched!")
        status.config(text=f"{box.get(ACTIVE)} launched!")
    else:
        print("Launch Aborted!")
        status.config(text="Launch Aborted!")


def exi():
    window.quit()


Button(framemid, text="Upload Secret File",
       command=open_file).grid(row=2, column=0)
spaceship_display = Label(framemid, bg="gray", width=23, height=5)
spaceship_display.grid(row=0, column=0, padx=10)
change_color = Button(framemid, text="Change Spaceship Colour",
                      font=("Comic Sans MS", 10), command=change)
change_color.grid(row=0, column=0, padx=10)


message_alien_pilots = Text(framemid, font=(
    "Comic Sans MS", 10), width=40, height=4)
message_alien_pilots.grid(row=0, column=2, columnspan=3)
Button(framemid, font=("Comic Sans MS", 10),
       text="Send Message", command=send).grid(row=1, column=2)
Label(framemid, font=("Comic Sans MS", 10),
      text="Select Invasion Plan:").grid(row=2, column=2)

box = Listbox(framemid, width=25, height=4)
box.grid(row=3, column=2)
box.insert(0, "Plan A: Earth Takeover")
box.insert(1, "Plan B: Moon Domination")
box.insert(2, "Plan C: Mars Colonization")
launch = Button(framemid, font=("Comic Sans MS", 10),
                text="Launch Plan", command=launch_plan)
launch.grid(row=4, column=2)
status = Label(framebottom, font=("Comic Sans MS", 10),
               text="Open Program", width=80, borderwidth=3, anchor="w", bg="#F0F0F0", relief="sunken")
status.pack(anchor="w")
Button(framebottom, font=("Comic Sans MS", 10),
       text="Exit", command=exi).pack()

window.mainloop()
