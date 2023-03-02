from tkinter import *

#-----------OKNO-----------

okno = Tk()
okno.title("Lubošova knihovna")
okno.minsize(width=350,height=350)
okno.geometry("700x350+800+-400")
okno.resizable(True,True)



#------------Stylizace-------

#barvy proměnné
main_font=("Times New Roman",12)
main_color = "#009933"
button_color = "#003300"
#stylizace okna
okno.config(bg=main_color)


#------------Spouštěč--------
okno.mainloop()