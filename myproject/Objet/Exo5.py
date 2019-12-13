"""
Exercice 5 - libre
"""

import sys

class virtualMachine:
    """
    Objet : machine virtuelle
    """
    def __init__(self, net, os, nom):
        if net:
            try:
                self.net = dict(net)
            except ValueError:
                print("Le paramètre net doit etre un dictionnaire [ip, masque, passerelle]")
        else:
            print("Un network doit etre renseigné !")
            sys.exit(1)

        if os:
            try:
                self.os = str(os)
            except ValueError:
                print("Le paramètre os doit etre un string ex : os='Debian'")
        else:
            print("Un os doit etre renseigné !")
            sys.exit(1)

        if nom:
            try:
                self.nom = str(nom)
            except ValueError:
                print("Le paramètre nom doit etre un string ex : nom='Client'")
        else:
            print("Un nom doit etre renseigné !")
            sys.exit(1)

    def __str__(self):
        return "\nLa machine {} est sous {} et possède l'ip {}".format(self.nom, self.os, self.net['ip'])

    def changer_ip(self, ip=None):
        """
        Change l'ip de la machine virtuelle
        :param ip:
        :return:
        """
        try:
            self.net['ip'] = str(ip)
        except ValueError:
            print("Le paramètre ip doit etre un string ")

    def changer_os(self, os=None):
        """
        Change le nom de l'Os de la machine virtuelle
        :param os:
        :return:
        """
        try:
            self.os = str(os)
        except ValueError:
            print("Le paramètre os doit etre un string ")

    def changer_nom(self, nom=None):
        """
        Change le nom de la machine virtuelle
        :param nom:
        :return:
        """
        try:
            self.nom = str(nom)
        except ValueError:
            print("Le paramètre nom doit etre un string ")

    def test_sous_reseau(self, machine):
        """
        Test si l'objet mis en paramètre est dans le meme sous réseau que la première machine
        :param machine:
        :return:
        """
        test = False
        if self.net['mask'] == machine.net['mask']:
            for block in range(0, len(self.net['ip'].split('.'))):
                if block < 3:
                    if self.net['ip'].split('.')[block] == machine.net['ip'].split('.')[block]:
                        test = True
                    else:
                        test = False
        return test


if __name__ == "__main__":
    # Construction de la machine virtuelle vm
    vm = virtualMachine({'ip': "192.168.16.7", 'mask': "255.255.255.0", 'passerelle': "192.168.16.254"}, "Debian", "Client")
    print(vm)
    vm.changer_nom("HTTPServer")
    print(vm)
    # Construction de la machine virtuelle vm2
    vm2 = virtualMachine({'ip': "192.168.16.8", 'mask': "255.255.255.0", 'passerelle': "192.168.16.254"}, "CentOS", "Client")
    print(vm2)
    # Test si vm1 et vm2 sont sur le meme sous réseau
    if vm.test_sous_reseau(vm2):
        print("\n -> vm1 et vm2 sont sur le meme sous réseau")
    else:
        print("\n -> vm1 et vm2 NE sont PAS sur le meme sous réseau")
