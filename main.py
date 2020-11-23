import tkinter as tk
from PIL import Image, ImageTk
import sql
from functools import partial

link = sql.MySQL()

class Ikeo(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('IKEO')
        self.geometry('900x720')
        self.config(bg="#CE0036")
        # logo = Image.open('ikeo_titre.png')
        # logo = ImageTk.PhotoImage(logo)
        # logo_label = tk.Label(bd = 0, image=logo)
        # logo_label.image= logo
        # logo_label.pack(side="top")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo) :
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.config(bg="#CE0036")
        label = tk.Label(self, text="Page Produits")
        label.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Rechercher une facture", command=lambda: controller.show_frame(PageOne))
        button.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        button.pack()

        button2 = tk.Button(self, text="Nouveau client",command=lambda: controller.show_frame(PageTwo))
        button2.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        button2.pack()

        self.afficher_produits()

    def afficher_produits(self):
        variable = tk.StringVar(self)
        commande = partial(self.afficher_usine, variable)
        menu = tk.OptionMenu(self, variable, *link.recup_produits(), command=commande)
        menu.config(width=13, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        menu.pack()

        self.label_usines = tk.Label(self, text="")
        self.label_usines.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        self.label_usines.pack()

    def afficher_usine(self, *args):
        usines = link.recup_produits_usines(args[1][0])
        affichage_usine = ""
        for usine in usines:
            affichage_usine += f"{usine}\n"
            affichage_usine.replace('{','').replace('}','')
        self.label_usines.configure(text=affichage_usine, font=('Consolas', 13), fg='yellow', bg="#CE0036", padx=15, pady=15)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#CE0036")
        label = tk.Label(self, text="Rechercher une facture")
        label.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Page Produits",command=lambda: controller.show_frame(StartPage))
        button1.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        button1.pack()
        button2 = tk.Button(self, text="Nouveau client",command=lambda: controller.show_frame(PageTwo))
        button2.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        button2.pack()

        date = tk.Label(self, text="Date (AAAA-MM-JJ) :")
        date.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=15)
        date.pack()
        self.entry_date = tk.Entry(self)
        self.entry_date.pack()
        num_client = tk.Label(self, text='Numero client :')
        num_client.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=15)
        num_client.pack()
        self.entry_nclient = tk.Entry(self)
        self.entry_nclient.pack()
        bouton_recherche = tk.Button(self, text='Rechercher', command=self.rechercher_facture)
        bouton_recherche.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        bouton_recherche.pack()
        self.label_facture = tk.Label(self, text="")
        self.label_facture.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=15)
        self.label_facture.pack()

    def rechercher_facture(self):
        date = self.entry_date.get()
        numero_client = self.entry_nclient.get()
        self.facture = link.recup_facture(numero_client, date)
        self.label_facture.configure(text=f"Résultat : {self.facture}")

        if self.facture == 'Facture non trouvé ou saisi erroné' or self.facture == 'Saisi invalide':
            pass           
        else:
            bouton_commande = tk.Button(self, text="Afficher la commande", command=self.rechercher_commande)
            bouton_commande.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
            bouton_commande.pack()
            self.label_commande = tk.Label(self, text="")
            self.label_commande.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=15)
            self.label_commande.pack()

    def rechercher_commande(self):
        commande = link.recup_commande(self.facture)
        self.label_commande.configure(text=f"{commande}")

            

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#CE0036")
        label = tk.Label(self, text="Nouveau client :")
        label.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=15)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Page Produits",command=lambda: controller.show_frame(StartPage))
        button1.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        button1.pack()

        button2 = tk.Button(self, text="Rechercher une facture",command=lambda: controller.show_frame(PageOne))
        button2.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        button2.pack()

        # Widgets
        label_raison = tk.Label(self, text='Raison social :')
        label_raison.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=5)
        label_raison.pack()
        self.entry_raison = tk.Entry(self)
        self.entry_raison.pack()
        label_adresse = tk.Label(self, text='Adresse : ')
        label_adresse.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=5)
        label_adresse.pack()
        self.entry_adresse = tk.Entry(self)
        self.entry_adresse.pack()
        label_type = tk.Label(self, text='Type : ')
        label_type.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=5)
        label_type.pack()
        self.entry_type = tk.Entry(self)
        self.entry_type.pack()
        label_ville = tk.Label(self, text='Ville : ')
        label_ville.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=5)
        label_ville.pack()
        self.entry_ville = tk.Entry(self)
        self.entry_ville.pack()
        label_pays = tk.Label(self, text='Pays :')
        label_pays.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=5)
        label_pays.pack()
        self.entry_pays = tk.Entry(self)
        self.entry_pays.pack()
        bouton_valide = tk.Button(self, text='Valider', command=self.valider_client)
        bouton_valide.config(width=25, font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0)
        bouton_valide.pack()
        self.label_clients = tk.Label(self, text="")
        self.label_clients.config(font=('Consolas', 15), bg="#CE0036", fg="yellow", activebackground="#CE0036", activeforeground="yellow", highlightthickness=0, padx=15, pady=15)
        self.label_clients.pack()

    def valider_client(self):
        raison = self.entry_raison.get()
        adresse = self.entry_adresse.get()
        type_c = self.entry_type.get()
        ville = self.entry_ville.get()
        pays = self.entry_pays.get()
        if raison=="" or adresse=="" or type_c=="" or ville=="" or pays=="":
            self.label_clients.configure(text='Veuillez remplir tout les champs !')
        else:
            link.nouveau_client(raison, adresse, type_c, ville, pays)
            liste_clients = link.recup_clients()
            clients = ""
            for client in liste_clients:
                clients += f"{client}\n"
            self.label_clients.configure(text="Saisi réussi !" + "\n" + clients)
        

app = Ikeo()
app.mainloop()
