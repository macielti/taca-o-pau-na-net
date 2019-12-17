import tkinter as tk
from tkinter import messagebox
import utils
import instabot
from playsound import playsound
import threading

class Main:
    def __init__(self):
        # main frame
        self.root = tk.Tk()
        self.root.title("Taca o Pau na Net")
        # center title of software
        tk.Label(self.root, text="Taca o Pau na Net").grid(row=0, column=0, columnspan=2, ipadx=50, pady=10)

        # user info#

        # entry for instagram login
        tk.Label(self.root, text="Login do Instagram:").grid(row=1, column=0)
        self.login_var = tk.StringVar()
        login_entry = tk.Entry(self.root, textvariable=self.login_var)
        login_entry.grid(row=1, column=1)

        # entry for pasword
        tk.Label(self.root, text="Senha do Instagram:").grid(row=2, column=0)
        self.passwd_var = tk.StringVar()
        passwd_entry = tk.Entry(self.root, textvariable=self.passwd_var, show='*')
        passwd_entry.grid(row=2, column=1)

        # provider info #
        
        # title
        tk.Label(self.root, text="Dados do provedor").grid(row=3, column=0, columnspan=2, ipady=10)
        
        # entry for internet provider instagram username
        tk.Label(self.root, text="Instagram do Provedor:").grid(row=4, column=0)
        self.provider_login_var = tk.StringVar()
        provider_login_entry = tk.Entry(self.root, textvariable=self.provider_login_var)
        provider_login_entry.grid(row=4, column=1)

        # entry for velocity contract
        tk.Label(self.root, text="Velocidade contratadas em Megas:").grid(row=5, column=0)
        self.down_contract_var = tk.DoubleVar()
        velocity_entry = tk.Entry(self.root, textvariable=self.down_contract_var)
        velocity_entry.grid(row=5, column=1)

        # analyse button
        complain_button = tk.Button(self.root, text="Analisar e Reclamar", command=self.calculate)
        complain_button.grid(row=6, column=0, columnspan=2, ipadx=50, pady=20)

    def calculate(self):
        
        result = utils.measure()

        # down velocity in Megas
        self.down_shiped = result['download']/1000000 

        message_box_str = " - Velocidade de download entregue: %.2f Megas \n - Velocidade de download contratada: %.2f Megas \n - O provedor está entregando %.2f%% do que foi contratado. \n\n Deseja reclamar no instagram do Provedor? " % (self.down_shiped, self.down_contract_var.get(), (100*self.down_shiped)/self.down_contract_var.get())
        answer = messagebox.askyesno("Resultados - <Provedor>", message_box_str)

        if answer: # if the user wish to do the post on the instagram
            # use threading to run the playsound in parallel with the do_reclamation function
            # for better effycience
            x = threading.Thread(target=playsound, args=('taca.mp3',))
            x.start()
            self.complain(result)

    
    def complain(self, result):
        """Recieve the result dict object that represent the test results"""

        bot = instabot.Bot(save_logfile=False, log_follow_unfollow=False) # create the instance of the instagram bot
        bot.login(username=self.login_var.get(), password=self.passwd_var.get()) # do login operation
        utils.clear_instabot_files(self.login_var.get()) # clear all the generated files

        try:
            media = bot.get_user_medias(self.provider_login_var.get(), filtration=False)[0] # get the most recent post from the provider perfil
        except Exception:
            messagebox.showerror("Erro", "Não foi possível acessar o Instagram, verifique seu usuário e senha e tente novamente.")
            return False

        reclamation_message = "[RECLAMAÇÃO] - Minha internet está muito lenta, vocês só estão me entregando %.2f Megas, que representa apenas %.2f%% da velocidade contratada que foi de %.2f Megas. Para mais detalhes sobre o teste de qualidade de conexão que realizei aqui em casa: %s" % (self.down_shiped, (100*self.down_shiped)/self.down_contract_var.get(), self.down_contract_var.get(), result['share'])
        bot.comment(media, reclamation_message) # post the results on the instagram
        messagebox.showinfo("Tudo OK...", "A sua reclamação foi postada com sucesso...")



if __name__ == "__main__":
    program = Main()
    program.root.mainloop()
