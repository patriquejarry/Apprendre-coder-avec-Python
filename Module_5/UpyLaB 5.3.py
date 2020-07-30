def duree(debut, fin):
    debut_t = 60 * debut[0] + debut[1]  # in minutes
    fin_t = 60 * fin[0] + fin[1]        # in minutes
    diff = fin_t - debut_t
    if diff < 0:
        diff += 24 * 60  # One day

    duree_h = diff // 60
    duree_m = diff - duree_h * 60

    return duree_h, duree_m


print(duree((14, 39), (18, 45)))  # (4, 6)
print(duree((6, 0), (5, 15)))     # (23, 15)
print(duree((5, 15), (5, 15)))    # (0, 0)
print(duree((5, 15), (5, 25)))    # (0, 10)
