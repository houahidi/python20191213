"""
manipulation des exceptions
"""
# definition d'une nouvelle classe de type exception
class MyException(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)

    def __str__(self):
        return "MyException: args={}".format(self.args)

# déclencher une exception  : raise Exception()
# traiter une exception : try except
try:
    print("instruction 1 ")
    print("instruction 2 ")
    print("instruction 3 ")
    raise MyException(1, "message")
    print("instruction 4 ")
except MyException as e:
    print("Erreur : ", e)
except Exception as e:
    print("Erreur : ", e)