from tkinter import *
from tkmacosx import Button

#-----------OKNO-----------

okno = Tk()
okno.title("Lubošova knihovna")
okno.minsize(width=350,height=350)
okno.geometry("700x350+800+-400")
okno.resizable(True,True)

#-----------Funkce------------
def close()

#------------Stylizace-------

#barvy proměnné
main_font=("Times New Roman",12)
main_color = "#e6ffff"
button_color = "#00b3b3"
#stylizace okna
okno.config(bg=main_color)




#-------------Frames----------
vstup_frame = Frame(okno,width=20,bg=main_color)
text_frame = Frame(okno,bg=main_color)
cudlik_frame = Frame(okno,bg=main_color)
vstup_frame.pack()
text_frame.pack()
cudlik_frame.pack()


#input frame - obsah
user_input = Entry(vstup_frame,width=20,borderwidth=1,font=main_font)
user_input.grid(row=0,column=0)
pridat_cudlik=Button(vstup_frame,text="Přidat",font=("Arial",12),bg=button_color)
pridat_cudlik.grid(row=0,column=1)

#text frame - obsah
text_box = Listbox(text_frame,height=17,width=100,borderwidth=1,font=main_font)
text_box.grid()

#Button frame - obsah
remove_button = Button(cudlik_frame,text="Smazat položku",font=main_font,bg=button_color)
remove_button.grid(row=0,column=0)

remove_all_button = Button(cudlik_frame,text="Smazat vše",font=main_font,bg=button_color)
remove_all_button.grid(row=0,column=1)

save_button = Button(cudlik_frame,text="Uložit seznam",font=main_font,bg=button_color)
save_button.grid(row=0,column=2)


exit_button = Button(cudlik_frame,text="Konec aplikace",font=main_font,bg=button_color,command=)
exit_button.grid(row=0,column=3)
#------------Spouštěč--------
okno.mainloop()