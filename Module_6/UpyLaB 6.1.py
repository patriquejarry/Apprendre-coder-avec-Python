def inventaire(offres, objets):
    """
    offres est un dictionnaire contenant, comme clés, les objets proposés par les amis du Petit Prince,
    et comme valeurs associées, le nom de l'ami proposant cet objet,
    objets est une liste contenant tous les objets dont a besoin le Petit Prince.
    """
#    amis_a_visiter = set()
#    for f in offres:
#        if f in objets:
#            amis_a_visiter.add(offres[f])
#    return amis_a_visiter
    return {offres[f] for f in offres if f in objets}


print(inventaire({'lit': 'Antoine', 'bibliothèque': 'Sébastien', 'chaise': 'Isabelle', 'livre "le vieil homme et la mer"': 'Ernest', 'sac de bonbons': 'Thierry', 'smartphone': 'Ted', 'table': 'Sophie'}, ['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"']))
# {'Antoine', 'Isabelle', 'Thierry', 'Ernest', 'Sophie'}
print(inventaire({'livre "le vieil homme et la mer"': 'Ernest', 'chaise': 'Isabelle', 'lit': 'Antoine', 'table': 'Sophie', 'smartphone': 'Ted', 'sac de bonbons': 'Thierry', 'bibliothèque': 'Sébastien'}, ['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"']))
# {'Antoine', 'Isabelle', 'Thierry', 'Ernest', 'Sophie'}
print(inventaire({'livre "le vieil homme et la mer"': 'Ernest', 'chaise': 'Isabelle', 'lit': 'Sébastien', 'table': 'Isabelle', 'smartphone': 'Ted', 'sac de bonbons': 'Sébastien', 'bibliothèque': 'Sébastien'}, ['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"']))
# {'Isabelle', 'Ernest', 'Sébastien'}
print(inventaire({'livre "le vieil homme et la mer"': 'Ernest', 'chaise': 'Isabelle', 'lit': 'Sébastien', 'table': 'Isabelle', 'smartphone': 'Ted', 'sac de bonbons': 'Sébastien', 'bibliothèque': 'Sébastien'}, []))
#set()
