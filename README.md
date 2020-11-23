# IKEO

Vous devez créer un une base de données, IKEO, à partir des listings données en PJ.

**Les régles de gestions sont les suivantes :

* Une usine fabrique plusieurs références et un références peut être construite par plusieurs usines.
* Une facture est destinée à un seul client, un client peut avoir plusieurs facutres.
* Une facture peut avoir plusieurs produits et les produits apparaissent sur plusieurs factures.

**Voici les requêtes à tester sur la base :

Afficher les nom et description de tous les produits,
Afficher tous les meubles qui sont abandonnés,
Effacer le Bo Meuble de brest,
Il y a une erreur sur le nom du meuble Apfelgluk, il faut le récrire Apfelgluck,
Ajouter un nouveau client : Tout à la maison, Place Terreaux, Lyon,
Ajouter une nouvelle facture pour le tout à la maison de Lyon , enregistré le 28/08/2018, à 18h. La commande est composé de 18 Naess,
Retrouver tous les meubles achetés par le Bo Meuble de Paris,
Retrouver toutes les factures enregistrée depuis le 1er juillet 2018.

**Une fois la base de données en place, développez une interface Python qui permet :

D'afficher tous les produits ainsi que leurs sites de production,
D'afficher la facture d'un client à une date choisie,
De saisir une facture (et de la mémoriser en base),
De saisir un nouveau client,
D'afficher tous les sites de productions,
De saisir un nouveau produit et de le ratacher à un site de production.

