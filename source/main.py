import tkinter as tk
from tkinter import messagebox
import utils

# main frame
root = tk.Tk()
root.title("Taca o Pau na Net")

# title
tk.Label(root, text="Taca o Pau na Net").grid(row=0, column=0, columnspan=2, ipadx=50, pady=10)

# entry instagram login
tk.Label(root, text="Login do Instagram:").grid(row=1, column=0)
login_var = tk.StringVar()
login_entry = tk.Entry(root, textvariable=login_var)
login_entry.grid(row=1, column=1)

# entry for password
tk.Label(root, text="Senha do Instagram:").grid(row=2, column=0)
passwd_var = tk.StringVar()
passwd_entry = tk.Entry(root, textvariable=passwd_var, show='*')
passwd_entry.grid(row=2, column=1)

# title
tk.Label(root, text="Dados do provedor").grid(row=3, column=0, columnspan=2, ipady=10)

# entry for internet provider instagram username
tk.Label(root, text="Instagram do Provedor:").grid(row=4, column=0)
provider_login_var = tk.StringVar()
provider_login_entry = tk.Entry(root, textvariable=provider_login_var)
provider_login_entry.grid(row=4, column=1)

# entry for velocity contract
tk.Label(root, text="Velocidade contratadas em Megas:").grid(row=5, column=0)
velocity_var = tk.StringVar()
velocity_entry = tk.Entry(root, textvariable=velocity_var)
velocity_entry.grid(row=5, column=1)

# button to make the reclamation
def calculate():
    global velocity_var
    
    result = utils.measure()

    down_contract = velocity_var.get()
    down_shiped = result['download']/1000000

    message_box_str = " - Velocidade de download entregue: %.2f Megas \n - Velocidade de download contratada: %.2f Megas \n - O provedor está entregando %.2f%% do que foi contratado. \n\n Deseja reclamar no instagram do Provedor? " % (down_shiped, float(down_contract), (100*down_shiped)/float(down_contract))
    answer = messagebox.askyesno("Resultados - <Provedor>", message_box_str)
    if answer: # if the user wish to do the post on the instagram
        #TODO - call the reclamation procedure.
        pass

complain_button = tk.Button(root, text="Analisar e Reclamar", command=calculate)
complain_button.grid(row=6, column=0, columnspan=2, ipadx=50, pady=20)

# show results
#messagebox.showinfo(
#        "Gabarito: ( ͡╥ ᖨ ͡╥)", "O seu Gabarito está triste pois não deram um nome para ele.")

root.mainloop()