import customtkinter

app = customtkinter.CTk()

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", type(choice))

optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(app,values=["option 1", "option 2"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)
optionmenu.place(x=10, y=10)

app.mainloop()