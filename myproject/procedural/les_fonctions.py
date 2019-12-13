"""
les fonctions
"""



def fonction(param1="val1", *params, **kwargs):
    print("fonction:", param1, params, kwargs)

if __name__ == "__main__":
    fonction()
    fonction("valeur")
    fonction("valeur", 2, 'ijcfi', True)
    fonction("valeur", 2, 'ijcfi', True, c1="v1", c2="v2")