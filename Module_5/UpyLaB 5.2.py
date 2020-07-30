def est_adn(chaine_adn):
    ADN = 'ACGT'

    if chaine_adn == '':
        return False
    for i in chaine_adn:
        if i not in ADN:
            return False
    return True


print(est_adn("ATGGT"))  # True
print(est_adn("ISA"))    # False
print(est_adn(""))       # False
