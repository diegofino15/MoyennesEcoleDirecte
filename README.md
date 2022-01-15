# MoyennesEcoleDirecte
Ce programme vous permettra de récupérer des informations sur vos notes et de calculer votre moyenne, avec une simple 
connexion à EcoleDirecte.

## Téléchargement

### Pré-requis
Vous devez avoir Python 3 installé ainsi que pip (installé en même temps que Python).
### Installation
La méthode habituelle.

```console
$ git clone https://github.com/diegofino15/MoyennesEcoleDirecte.git
$ cd ./MoyennesEcoleDirecte
```

Une fois le repo installé et une fois que vous êtes dedans, installez les modules requis.
```
requests
json
getpass
```


### Mettre à jour
Pour mettre votre clone à jour,
```console
$ git pull
```

## Utilisation

Le script ne marche qu'avec les comptes `E` (Eleve). Les comptes famille ne sont pas supportés. Ouvrez le script depuis le terminal ou en cliquant sur l'icône dans le File Explorer.
```console
$ python3 moyennes.py
```

### Valeurs montrées
Le script va générer un site internet, avec votre nom, votre moyenne générale, et vos moyennes de chaque matière et de chaque trimestre de l'année.

### Attention
Les valeurs affichées ne sont pas exactes, car École Directe ne fournit pas les coefficients des contrôles, les moyennes devraient être assez proches de la réalité.
