import json
import os
import sys
from sympasoap import Client
from sympasoap.client import Fault


class SympaController:

    def __init__(self, url: str, login: str, password: str):
        self.sympa_url = url
        self.login = login
        self.password = password
        self.client = SympaController.get_connect_to_sympa(self)

    def get_connect_to_sympa(self) -> Client:
        """
        Méthode de connexion au serveur Sympa.

        :returns: Un client de connexion
        """
        try:
            client = Client(self.sympa_url)
            client.login(self.login, self.password)
            return client
        except Fault as e:
            msg = f"Erreur, pas de connexion à Sympa : {str(e)}."
            raise Fault(msg)

    def get_list_in_list(self) -> None:
        """
        Méthode pour récupérer des listes de diffusion comme membre dans des listes de diffusion.
        """
        conn = self.client
        sympa_lists = []
        lists_raw = conn.all_lists()
        for mailing_list in lists_raw:
            subscribers = conn.get_subscribers(mailing_list.list_address, emails_only=True)
            datas = {
                "name": mailing_list.list_address,
                "members": subscribers,
            }
            sympa_lists.append(datas)
        list_in_list = []
        for mailing_list in lists_raw:
            for list in sympa_lists:
                members = list.get("members")
                if mailing_list.list_address in members:
                    datas = {
                        "list_address_name": list.get("name"),
                        "list_hidden_in_list": mailing_list.list_address
                    }
                    list_in_list.append(datas)

        file_name = "lists_hidden_in_lists.json"
        file_path = os.path.join(file_name)
        folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_path)
        try:
            with open(folder, "w") as file:
                json.dump(list_in_list, file, indent=2)
        except FileExistsError as e:
            msg = f"Erreur dans la tentative d'écriture et de génération du fichier JSON : {str(e)}"
            raise FileExistsError(msg)


def main(kwargs: list[str]) -> None:
    # sympa env
    sympa_url = kwargs[0]
    sympa_login = kwargs[1]
    sympa_password = kwargs[2]
    sc = SympaController(sympa_url, sympa_login, sympa_password)
    print("Recherche en cours....")
    sc.get_list_in_list()
    print("Recherche terminée. Fichier JSON disponible dans le dossier du script.")
    sys.exit(0)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
