from tkinter import *

import customtkinter
from tkmacosx import Button
from customtkinter import *
from termcolor import colored

#-----------OKNO-----------

okno = customtkinter.CTk()
okno.title("Úkolovník")
okno.minsize(width=750,height=420)
okno.geometry("750x350+800+-420")
okno.resizable(True,True)

#-----------Funkce------------


def close_app():
    exit()


def pridat_polozku():
    pocet = text_box.size() + 1
    

    ui = f"{pocet}: {user_input.get()}"
    text_box.insert(0,ui)

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
            if one_save.endswith("\n"):
                file.write(f" {one_save}")
            else:
                file.write(f" {one_save}\n")




#------------Stylizace-------

#barvy proměnné

#stylizace okna
okno.configure(fg_color="#1f2e2e")




#-------------Frames----------
vstup_frame = customtkinter.CTkFrame(okno,width=20,fg_color="#1f2e2e")
text_frame = customtkinter.CTkFrame(okno)
cudlik_frame = customtkinter.CTkFrame(okno,fg_color="#1f2e2e")
vstup_frame.pack()
text_frame.pack()
cudlik_frame.pack()


#input frame - obsah
user_input = customtkinter.CTkEntry(vstup_frame,width=200,placeholder_text="text...",fg_color="#8cd9b3")
user_input.grid(row=0,column=0)

pridat_cudlik=customtkinter.CTkButton(vstup_frame,text="Přidat",font=("Arial",12),command=pridat_polozku)
pridat_cudlik.grid(row=0,column=1,pady=6,padx=6)






#text frame - obsah
text_box = Listbox(text_frame,height=17,width=70,cursor="pencil",borderwidth=3,bg="#8cd9b3")
text_box.grid()




#Button frame - obsah
remove_button = customtkinter.CTkButton(cudlik_frame,text="Smazat položku",command=vymazat_polozku)
remove_button.grid(row=0,column=0,padx=11,pady=10)

remove_all_button = customtkinter.CTkButton(cudlik_frame,text="Smazat vše",command=vymazat_vse)
remove_all_button.grid(row=0,column=1,padx=11,pady=10)

save_button = customtkinter.CTkButton(cudlik_frame,text="Uložit seznam",command=ulozit_seznam)
save_button.grid(row=0,column=2,padx=11,pady=10)


exit_button = customtkinter.CTkButton(cudlik_frame,text="Konec aplikace",command=close_app)
exit_button.grid(row=0,column=3,padx=11,pady=10)
#------------Spouštěč--------
nacti_data()
okno.mainloop()