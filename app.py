from tkinter import *
from tkmacosx import Button

#-----------OKNO-----------

okno = Tk()
okno.title("Úkolovník")
okno.minsize(width=700,height=350)
okno.geometry("700x350+800+-400")
okno.resizable(True,True)

#-----------Funkce------------
def close_app():
    exit()


def pridat_polozku():
    text_box.insert(0,user_input.get())
    user_input.delete(0,END)

def vymazat_polozku():
    with open("ukoly.txt","w") as file:
        text_box.delete(ANCHOR)

def vymazat_vse():
    text_box.delete(0,END)
    with open("ukoly.txt","w") as file:
        delete_app = text_box.delete(0,END)

def nacti_data():
    try:
        with open("ukoly.txt","r") as file:
            for one_line in file:
                text_box.insert(END,one_line)
    except:
        print("Chyba funkce")
def ulozit_seznam():
    with open("ukoly.txt","w") as file:
        save_app = text_box.get(0,END)
        for one_save in save_app:
            file.write(f"{one_save}\n")


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
user_input = Entry(vstup_frame,width=83,borderwidth=1,font=main_font,cursor="pencil")
user_input.grid(row=0,column=0)

pridat_cudlik=Button(vstup_frame,text="Přidat",font=("Arial",12),bg=button_color,command=pridat_polozku)
pridat_cudlik.grid(row=0,column=1,pady=6,padx=6)




#text frame - obsah
text_box = Listbox(text_frame,height=17,width=100, font=main_font,cursor="pencil")
text_box.grid()




#Button frame - obsah
remove_button = Button(cudlik_frame,text="Smazat položku",font=main_font,bg=button_color,command=vymazat_polozku)
remove_button.grid(row=0,column=0,pady=6,padx=27)

remove_all_button = Button(cudlik_frame,text="Smazat vše",font=main_font,bg=button_color,activebackground="red",activeforeground="black",command=vymazat_vse)
remove_all_button.grid(row=0,column=1,pady=6,padx=27)

save_button = Button(cudlik_frame,text="Uložit seznam",font=main_font,bg=button_color,command=ulozit_seznam)
save_button.grid(row=0,column=2,pady=6,padx=27)


exit_button = Button(cudlik_frame,text="Konec aplikace",font=main_font,bg=button_color,command=close_app,activebackground="red",activeforeground="black")
exit_button.grid(row=0,column=3,pady=6,padx=27)
#------------Spouštěč--------
nacti_data()
okno.mainloop()