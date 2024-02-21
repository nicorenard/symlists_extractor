# Utilitaire CLI : symlists_extractor

## Objectif

Récupérer d'un serveur SYMPA, la liste des listes de diffusions inscrite en tant que membre d'une autre liste de diffusion et non *incluse*
comme le veut la bonne pratique... ;)
Ce script utilise la librairie [sympasoap](https://gitlab.com/animath/si/py-sympa-soap) pour fonctionner.

## Utilisation 
* Avoir python d'installé (v3.12)
* Créer un environnement virtuel : 
  * ``$ python -m venv .venv``
* Le lancer: 
  * ``$ source .venv/bin/activate`` (Linux)
  * ``$ call C:\chemin\vers\projet\env_nom_du_projet\Scripts\activate.bat`` (windows)
  * ou ``C:\chemin\vers\projet\env_nom_du_projet\Scripts\Activate.ps1`` (windows powershell)
* Installer avec pip les dépendances du fichier requirements.txt
  * ``$ pip install -r requirements.txt``
* Dans un terminal, à la racine du script faire la commande suivante -environnement virtuel activé- :

``
$ python symlist_extractor.py *arg1 *arg2 *arg3
``

* Les arguments sont **OBLIGATOIRES** dans l'ordre strict suivant : 
  * arg1 = url serveur sympa sans /wsdl à la fin ( ex: http://nom_de_domaine.fr/sympa)
  * arg2 = login administrateur ( ex : listmaster@sympa.nom_de_domaine.fr)
  * arg3 = mot de passe administrateur (ex : mon_beau_mdp)

**/!\ Note : Mettre plus de 3 arguments => pas de prise en compte et moins de 3 arguments => le script sera en erreur.**

Après quelques minutes, vous obtiendrez en résultat un fichier JSON avec la structure suivante dans le dossier du script : 

```json=
[
  {
     "list_address_name": "security@nom_de_domaine.fr",
     "list_hidden_in_list": "abuse@nom_de_domaine.fr"
  },
  {...}
]
```

## Changlog

2024 : v.0.0.1

## Licence

GPLv3

## Auteur

Nicolas.renard_at_uha.fr