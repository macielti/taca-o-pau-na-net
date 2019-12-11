import tkinter as tk

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
tk.Label(root, text="Login do Provedor:").grid(row=4, column=0)
provider_login_var = tk.StringVar()
provider_login_entry = tk.Entry(root, textvariable=provider_login_var)
provider_login_entry.grid(row=4, column=1)

# button to make the reclamation
complain_button = tk.Button(root, text="Analisar e Reclamar")
complain_button.grid(row=5, column=0, columnspan=2, ipadx=50, pady=20)

root.mainloop()