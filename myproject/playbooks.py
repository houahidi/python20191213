"""
playbook
"""


class Playbook:

    def __init__(self, job: str, inventaire: list):
        """

        Parameters
        ----------
        job : script ksh
        inventaire : liste de serveur
        """
        self.job = job
        self.inventaire = inventaire


    def preparer(self):
        """
        preparer la liste des actions à entreprendre
        Returns
        -------

        """
        print( "Le script ", str(self.job) , " sera exécuter sur les serveurs suivants : " , str(self.inventaire))
        script_par_serveur = []
        for serveur in self.inventaire :
            #print(self.job , "  " , serveur)
            script_par_serveur.append(self.job + "  " + serveur)

        return script_par_serveur

    def enlever_serveur(self, serveur):
        print("enlever le serveur ", serveur)
        self.inventaire.remove(serveur)

if __name__ == "__main__":
    PLAY1 = Playbook("super_script.ksh", ['server_1','server_2', 'server_3'])
    # preparer les actions
    list_script_vs_serveurs = PLAY1.preparer()
    # Scenario II
    print("----- EXECUTION I -------")
    # Executer les actions
    for execution in list_script_vs_serveurs :
        print(execution)

    # Scenario II
    print("----- EXECUTION II -------")
    # preparer les actions
    PLAY1.enlever_serveur("server_2")
    list_script_vs_serveurs = PLAY1.preparer()
    # Executer les actions
    for execution in list_script_vs_serveurs :
        print(execution)




