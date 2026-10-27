def cell_metabolism(G,O):
    def energy_output():
        if O==6*G:
            nATP=38*G
        elif G>O//6:
            nATP=38*(O//6)
        else:
            nATP=38*G
        return nATP
    return energy_output()
print(cell_metabolism(1,11))



