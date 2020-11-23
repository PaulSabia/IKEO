import mysql.connector as mysqlpyth

class MySQL():
    def __init__(self):
        self.db = mysqlpyth.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            port = 8081,
            db = 'ikeo2'
        )
        self.cursor = self.db.cursor(buffered=True)
        print('Connexion réussi !')

    def deconnexion(self):
        self.db.close
        print('Connexion terminé !')

    def recup_produits(self):
        query = 'SELECT nom_p FROM produits'
        self.cursor.execute(query)
        liste_nom = []
        for nom in self.cursor:
            liste_nom.append(nom)
        return liste_nom

    def recup_produits_usines(self, nom):
        query = f"SELECT nom_u, ville_u FROM usines JOIN produits_usines ON usines.id_u = produits_usines.usine_id JOIN produits ON produits_usines.produit_id=produits.id_p WHERE nom_p = '{nom}'"
        self.cursor.execute(query)
        liste = []
        for elements in self.cursor:
            liste.append(elements)
        return liste

    def recup_facture(self, client, date):
        self.client = client
        self.date = date
        try:
            query = f"SELECT id_f, numero_f FROM factures WHERE id_c={self.client} AND date_f='{self.date}'"
            self.cursor.execute(query)
            liste = []
            for elements in self.cursor:
                liste.append(elements)
            if liste == []:
                return 'Facture non trouvé ou saisi erroné'
            else:
                return liste 
        except:
            return 'Saisi invalide'

    def recup_commande(self, liste):
        query = f"SELECT id_p, quantite_co FROM commandes WHERE id_f={liste[0][0]}"
        self.cursor.execute(query)
        liste = []
        for elements in self.cursor:
            liste.append(elements)
        
        liste2 = []
        for i in range(len(liste)):
            query = f"SELECT nom_p FROM produits WHERE id_p={liste[i][0]}"
            self.cursor.execute(query)
            for elem in self.cursor:
                liste2.append(elem)

        liste3 = []
        for ident_quantite in liste:
            for nom in liste2:
                commande = [ident_quantite[1], nom]
                liste3.append(commande)
        return liste3

    def recup_clients(self):
        query = 'SELECT * FROM clients'
        self.cursor.execute(query)
        liste = []
        for client in self.cursor:
            liste.append(client)
        return liste

    def nouveau_facture(self, date, n_client, n_facture):
        query = f"INSERT INTO factures (date_f, id_c, numero_f) VALUES ('{date}','{n_client}','{n_facture}')"
        self.cursor.execute(query)
        self.db.commit()

    def nouveau_client(self, raison, adresse, type_c, ville, pays):
        query = f"INSERT INTO clients (raison_c, adresse_c, type_c, ville_c, pays_c) VALUES ('{raison}','{adresse}','{type_c}','{ville}','{pays}')"
        self.cursor.execute(query)
        self.db.commit()

    def recup_usine(self):
        query = f"SELECT id_u, nom_u, adresse_u, ville_u FROM usines"
        self.cursor.execute(query)
        liste = []
        for elements in self.cursor:
            liste.append(elements)
        print(liste)
        return liste

    def nouveau_produit(self, nom, ref, descrip, abandon, usine_id):
        query = f"INSERT INTO produits (id_p, nom_p, ref_p, descrip_p, abandon_p) VALUES (NULL, '{nom}', '{ref}', '{descrip}', {abandon})"
        self.cursor.execute(query)
        self.db.commit()

        query = f"SELECT id_p FROM produits WHERE nom_p='{nom}'"
        self.cursor.execute(query)
        for ident in self.cursor:
            identifiant = ident[0]
        
        query = f"INSERT INTO produits_usines (id_pu, usine_id, produit_id) VALUES (NULL, {usine_id}, {identifiant})"
        self.cursor.execute(query)
        self.db.commit()
        return 'Produit enregistré !'

