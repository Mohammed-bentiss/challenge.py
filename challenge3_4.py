# ********************************le menu principale********************************
mes_liste = { 
    'inventaire' : [],
    'produit' : [],
    'quantite' : []   
}

def menu(choix=int):

    print("entre un nomber pour confirmer votre choix")
    print("1_ajouter un produit")
    print("2_recherche ")
    print("3_retirer un produit")
    print("4_modifier un produit")
    print("5_aficher inventaire")
    print("0_pour quitte le programmeq")
    choix=input("entre votre choix:" )
    if choix.isnumeric():
        if int(choix) in [1,2,3,4,5]:
                choix = int(choix)
        else:
                choix = 0
    else:
        choix = 0
    return choix


def ajouter():

    élement_inventaire = input("enter les élement de l'inventaire: ")
    mes_liste['inventaire'].append(élement_inventaire)
    
    élement_produit = input("enter les élement de produit: ")
    mes_liste['produit'].append(élement_produit)
   
    élement_quantite = input("enter les élement de la quantite: ")
    mes_liste['quantite'].append(élement_quantite)

    print(mes_liste)
    return mes_liste


def recherche():

    x = input("enter l'élement que vous recherche: ")
    if x in mes_liste['inventaire']:
        index = mes_liste['inventaire'].index(x)
        print(f"Ce produit existe:{mes_liste['produit'][index]}, quantite:{mes_liste['quantite'][index]}")
    else:
        print("Ce produit n'existe pas")

    return x

def retirer():
    x = input("entre le nom de produit que tu peux retire: ")
    if x in mes_liste['inventaire']:
        index = mes_liste['inventaire'].index(x)
        for key in mes_liste:
            mes_liste[key].pop(index)
        print("Le produit a été supprimé. ")
    else:
        print("Ce produit n'existe pas")

def modifier():
     print("la modification ") 

while True:
    choix = menu()
    if choix == 1:
        ajouter()
    elif choix == 2:
        recherche()
    elif choix == 3:
        retirer()
    elif choix == 0:
        print("quiter le programme")
        break
    else:
        print("Sélection non valide, réessayez.")





          


