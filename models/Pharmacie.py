'''
 Classe qui a un nom de pharmacie, une adresse, capacité de pharmacie,
 et un ensemble de produit
 
 Ajouter un nouveau produit à la pharmacie , tout en 
 prenant en considération qu’
 un pharmacie peut contenir au maximum 50 produits.
 
 Afficher le nom et le prix de l’ensemble ses produits. 
'''


'''public class Magasin {
	String nom;
	String adresse;
	protected Produit[] produits;
	public int nbProduits;// nombre actuel de produits
	final int CAPACITE_E = 20; // constante

public boolean ajouterProduit(Produit p) {
		if (nbProduits < CAPACITE_P) {
			produits[nbProduits] = p;
			nbProduits++;
			return true;
		}
		return false;
	}'''
 
class Magasin:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.produits = [None] * 20  # Initialiser la liste avec une capacité de 20
        self.nbProduits = 0

    #Ajouter Produit
    def ajouterProduit(self, p):
        if self.nbProduits < len(self.produits):
            self.produits[self.nbProduits] = p
            self.nbProduits += 1
            return True
        return False
    
    
    #Chercher Produit
    def chercherProduit(self, p):
        i = 0
        while i < self.nbProduits and not p.comparer(self.produits[i]):
            i += 1
            return p.comparer(self.produits[i]) if i < self.nbProduits else False

    #Ajouter un nouveau produit une seule fois
    def ajouterNouveauProduit(self, p):
        if self.nbProduits < self.CAPACITE_P and not self.chercherProduit(p):
            self.produits[self.nbProduits] = p
            self.nbProduits += 1
        return True
        return False
