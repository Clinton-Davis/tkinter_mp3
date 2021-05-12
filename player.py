from tkinter import *

root = Tk()
root.title("MP3 Player")
root.geometry("500x400")

#Function to add one tracks
def add_one_track():
    pass

#Function to add many tracks
def add_many_tracks():
    pass

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Add Song Menu
add_track_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Track", menu=add_track_menu)
#Add One Track to Playlist
add_track_menu.add_command(label="Add One Track To Playlist", command=add_one_track)
#Add Many Tracks to Playlist
add_track_menu.add_command(label="Add Many Track To Playlist", command=add_many_tracks)
#Create Playlist Box
playlist_box = Listbox(root, bg="black", fg="lightblue", width=60)
playlist_box.pack(pady=20)

#Define Btn Img For Controls
back_btn_img = PhotoImage(file="img/back.png")
forward_btn_img = PhotoImage(file="img/forward.png")
play_btn_img = PhotoImage(file="img/play.png")
stop_btn_img = PhotoImage(file="img/stop.png")
pause_btn_img = PhotoImage(file="img/pause.png")

#Create Button Frame
control_frame = Frame(root)
control_frame.pack(pady=20)

#Create Control Buttons
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0)
forward_btn = Button(control_frame, image=forward_btn_img, borderwidth=0)
play_btn = Button(control_frame, image=play_btn_img, borderwidth=0)
stop_btn = Button(control_frame, image=stop_btn_img, borderwidth=0)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0)

#Adding Btns to Grid
stop_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
pause_btn.grid(row=0, column=2, padx=10)
back_btn.grid(row=0, column=3, padx=10)
forward_btn.grid(row=0, column=4, padx=10)






root.mainloop()