#Les classes de mon projet Gestion_Stock_Pharmacie:
'''
Produit, ProduitPack, Medicamaent, Commande, Employe
'''
'''
Les méthodes: Ajouter, Supprimer, Modifier, Afficher

'''

class Produit:
    #constructeur non paramétré
    def __init__(self):
        pass
    # Constructeur paramétré pour initialiser les attributs
    def __init__(self, nom, prix, categorie, fournisseur, quantité, reference, date_expiration):
        self.nom = nom
        self.prix = prix
        self.categorie = categorie
        self.fournisseur = fournisseur
        self.quantité = quantité
        self.reference = reference
        self.date_expiration = date_expiration
        
        

# Les méthodes créés:
'''
public void afficher() {
		System.out.println("id:" + id + ", libelle:" + libelle + ", marque:" + marque + ", prix:" + prix
				+ ", date expiration:" + dateExp);

	}
        '''
        
def afficher(self):
    print(f"id: {self.id}, libelle: {self.libelle}, marque: {self.marque}, prix: {self.prix}, date expiration: {self.dateExp}")

        
    