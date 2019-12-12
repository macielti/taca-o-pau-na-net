import tkinter as tk
from tkinter import messagebox
import utils
import instabot
from playsound import playsound
import threading

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

# post the reclamation function
def do_reclamation(result):
    """Recieve the result dict object that represent the test results"""
    global login_var
    global passwd_var
    global provider_login_var
    global velocity_var

    down_contract = velocity_var.get()
    down_shiped = result['download']/1000000
    
    bot = instabot.Bot(save_logfile=False, log_follow_unfollow=False) # create the instance of the instagram bot
    bot.login(username=login_var.get(), password=passwd_var.get()) # do login operation
    utils.clear_instabot_files(login_var.get()) # clear all the generated files
    try:
        media = bot.get_user_medias(provider_login_var.get(), filtration=False)[0] # get the most recent post from the provider perfil
    except Exception:
        messagebox.showerror("Erro", "Não foi possível acessar o Instagram, verifique seu usuário e senha e tente novamente.")
        return False

    reclamation_message = "[RECLAMAÇÃO] - Minha internet está muito lenta, vocês só estão me entregando %.2f Megas, que representa apenas %.2f%% da velocidade contratada que foi de %.2f Megas. Para mais detalhes sobre o teste de qualidade de conexão que realizei aqui em casa: %s" % (down_shiped, (100*down_shiped)/float(down_contract), float(down_contract), result['share'])
    bot.comment(media, reclamation_message) # post the results on the instagram
    messagebox.showinfo("Tudo OK...", "A sua reclamação foi postada com sucesso...")




# button to make the reclamation
def calculate():
    global velocity_var
    
    result = utils.measure()

    down_contract = velocity_var.get()
    down_shiped = result['download']/1000000

    message_box_str = " - Velocidade de download entregue: %.2f Megas \n - Velocidade de download contratada: %.2f Megas \n - O provedor está entregando %.2f%% do que foi contratado. \n\n Deseja reclamar no instagram do Provedor? " % (down_shiped, float(down_contract), (100*down_shiped)/float(down_contract))
    answer = messagebox.askyesno("Resultados - <Provedor>", message_box_str)
    if answer: # if the user wish to do the post on the instagram
        # use threading to run the playsound in parallel with the do_reclamation function
        # for better effycience
        x = threading.Thread(target=playsound, args=('taca.mp3',))
        x.start()
        #playsound('taca.mp3')
        do_reclamation(result)

complain_button = tk.Button(root, text="Analisar e Reclamar", command=calculate)
complain_button.grid(row=6, column=0, columnspan=2, ipadx=50, pady=20)

# show results
#messagebox.showinfo(
#        "Gabarito: ( ͡╥ ᖨ ͡╥)", "O seu Gabarito está triste pois não deram um nome para ele.")

root.mainloop()