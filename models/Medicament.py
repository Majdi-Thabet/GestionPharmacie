# Classe médicament qui hérite de la classe Produit
class Medicament(Produit): 
    
    #nom, prix, categorie, fournisseur, quantité, reference, date_expiration
    def __init__(self, nom, prix, reference, quantite_en_stock, date_expiration, fournisseur, categorie, composition):
        super().__init__(nom, prix, reference, quantite_en_stock, date_expiration, fournisseur, categorie)
        self.composition = composition
        


