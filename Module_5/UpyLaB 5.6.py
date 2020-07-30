def transcription_arn(chaine_adn):
    # return chaine_adn.replace('T','U')
    chaine_arn = chaine_adn[:]
    for i in range(len(chaine_arn)):
        if chaine_arn[i] == 'T':
            chaine_arn = chaine_arn[:i] + 'U' + chaine_arn[i+1:]
    return chaine_arn


print(transcription_arn('AGTCTTACCGATCCAT'))  # 'AGUCUUACCGAUCCAU'
print(transcription_arn('TGTCTTACCGATCCAT'))  # 'TGUCUUACCGAUCCAU'
