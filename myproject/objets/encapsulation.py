



class MaClasse:
    def __init__(self, param):
        self.__attribut = param
    def __get_attribut(self):
        print("get_attribut")
        return self.__attribut
    def __set_attribut(self, val):
        print("set_attribut")
        self.__attribut = val
    attribut = property(__get_attribut, __set_attribut, None, "attribut publique")




class MaClasseBis:
    def __init__(self, param):
        self.__attribut = param
    @property
    def attribut(self):
        "attribut public"
        print("get_attribut")
        return self.__attribut

    @attribut.setter
    def attribut(self, val):
        print("set_attribut")
        self.__attribut = val


if __name__ == "__main__":
    O_1 = MaClasseBis("val1")
    print(O_1.attribut)
    O_1.attribut ="new val"
    print(O_1.attribut)
    #del(O_1.attribut)
    help(O_1)

