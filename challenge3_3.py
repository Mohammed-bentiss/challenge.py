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
    menu()
    return mes_liste

def recherche():
    x = int(input("enter l'élement que vous recherche: "))
    if x in mes_liste.key():
        print(x)
    menu()
    return x

     
     

     
# def afichage():
#     mes_liste()
#     print('inventaire')
#     print('produit')
#     print('quantite')
    
#     menu()

choix = menu() 
match choix:
    case 1:
          ajouter()
    case 2:
          recherche()
    # # case 3:
    # #       print(retirer)
    # # case 4:
    # #       print(modifier)
    #         break
    # # case 5:
    # #       print(aficher)





          

