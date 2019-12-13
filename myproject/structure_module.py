"""
Le commentaire global du module

"""

# les définitions
MY_VAR__GLOBAL = "variable globale"
def my_print():
    """commentaire print """
    pass


# scénario de tests
if __name__ == "__main__":
    print("__name : ", __name__)
    print("mon scenario : var global = ",  MY_VAR__GLOBAL)
    my_print()