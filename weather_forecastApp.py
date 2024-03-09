from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import*
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather Forecast")
root.geometry("890x470+500+300")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="weather_forecastApp")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)} °N, {round(location.longitude, 4)} °E")

    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I : %M %p")
    clock.config(text=current_time)

#Icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images/Rounded Rectangle1.png")
Label(root, image= Round_box, bg="#57adff").place(x=30, y=110)


#labels
label1 = Label(root, text="Temperature", font=("Helvetica",11), fg="white", bg="#203243" )
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetica",11), fg="white", bg="#203243" )
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=("Helvetica",11), fg="white", bg="#203243" )
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=("Helvetica",11), fg="white", bg="#203243" )
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetica",11), fg="white", bg="#203243" )
label5.place(x=50, y=200)

#Search box
Search_image =PhotoImage(file="Images/search.png")
myimage = Label(image = Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weath_image = PhotoImage(file="Images/layer7.png")
weatherimage = Label(root, image=weath_image, bg="#203243")
weatherimage.place(x=300, y=134)

textfield = tk.Entry(root, justify="center", width=15, font=("poppins", 25, "bold"), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=138)
textfield.focus()

Search_icon = PhotoImage(file="images/search_icon2.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y= 134)


#########BOTTOM BOX
frame = Frame(root, width=900, height =180, bg="#212120")
frame.pack(side=BOTTOM)

#Bottom Boxes
firstbox = PhotoImage(file="images/Rounded Rectangle2.png")
secondbox = PhotoImage(file="images/Rounded Rectangle2copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=280, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=380, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=480, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=580, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=680, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=780, y=20)



#We will work on the time over here
clock=Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)


#timezone
timezone=Label(root, font=("Helvetica", 20, ), fg="white", bg="#57adff")
timezone.place(x=650, y=20)

long_lat=Label(root, font=("Helvetica", 10, ), fg="white", bg="#57adff")
long_lat.place(x=660, y=50)










# Application main method
root.mainloop()
