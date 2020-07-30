def calcul_prix(produits, catalogue):
    """
    produits est un dictionnaire contenant, comme clés, les produits souhaités par Monsieur Germain
    et comme valeurs associées, la quantité désirée de chacun d’entre eux,
    catalogue est un dictionnaire contenant tous les produits du magasin avec leur prix associé.
    La fonction retourne le montant total des achats de Monsieur Germain.
    """
    # total = 0.0
    # for p in produits:
    #     if p in catalogue:
    #         total += produits[p] * catalogue[p]
    # return total

    # total = 0.0
    # for t in [produits[p] * catalogue[p] for p in produits if p in catalogue]:
    #     total += t
    # return total

    total = 0.0
    for t in [produits[p] * catalogue[p] for p in produits if p in catalogue]:
        total += t
    return total

print(calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
                    {"brocoli":1.50, "bouteilles d'eau":1, "bière":2, "savon":2.50, "mouchoirs":0.80}))
# 13.0
