# MoyennesEcoleDirecte
Ce programme vous permettra de récupérer des informations sur vos notes et de calculer votre moyenne, il va aussi créer un site internet avec les moyennes affichées de façon rangée et organisée. Vous pouvez aussi choisir que les résultats soient affichés dans le terminal.

Il y a aussi une version de ce programme en site internet disponible à : http://moyennesed.my.to

## Téléchargements

### Pré-requis
Il y a besoin de Python3, ainsi que pip.
### Installation

```console
git clone https://github.com/diegofino15/MoyennesEcoleDirecte.git
cd ./MoyennesEcoleDirecte
```

Installez les modules requis, si vous ne les avez pas.
```console
pip install requests
pip install sys
pip install os
pip install json
pip install getpass
```


### Mettre à jour
```console
git pull
```

## Utilisation

Vous pouvez lancer le script avec le terminal, en donnant comme paramètre l'identifiant, et cela va de base rendre les résultats en forme de tableau dans le terminal. Vous pouvez aussi spécifier le type de rendu que vous désirez.

return_type -> 

-t = terminal,

-j = json,

-s = site internet

### Système de compte
Plusieurs systèmes sont disponibles : 
```console
python3 main.py -user [identifiant] [return_type] -save
python3 main.py [return_type]
python3 main.py -user [identifiant] -remove
python3 main.py -user [identifiant] [return_type]
```

### Attention
Les moyennes affichées ne sont pas exactes, car École Directe ne fournit pas les coefficients des contrôles, mais les moyennes devraient cependant être assez proches de la réalité.
