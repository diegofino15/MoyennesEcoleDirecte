# MoyennesEcoleDirecte
Ce programme vous permettra de récupérer des informations sur vos notes et de calculer votre moyenne, il va aussi créer un site internet avec les moyennes affichées de façon rangée et organisée. Vous pouvez aussi choisir que les résultats soient affichés dans le terminal.

Il y a aussi une version de ce programme en site internet disponible à : http://moyennesed.my.to

## Téléchargements

### Pré-requis
Vous devez avoir Python 3 installé ainsi que pip (installé en même temps que Python).
### Installation
La méthode habituelle.

```console
git clone https://github.com/diegofino15/MoyennesEcoleDirecte.git
cd ./MoyennesEcoleDirecte
```

Une fois le repo installé et une fois que vous êtes dedans, installez les modules requis.
```console
pip install requests
pip install sys
pip install json
pip install getpass
```


### Mettre à jour
Pour mettre votre clone à jour,
```console
git pull
```

## Utilisation

Vous pouvez lancer le script avec le terminal, en donnant comme paramètre l'identifiant, et de base cela rend les résultats en forme de tableau dans le terminal. Vous pouvez aussi spécifier le type de rendu que vous désirez.

return_type -> -t = terminal, -s = site internet, -j = json

```console
python3 moyennes.py [identifiant]
python3 moyennes.py [identifiant] [return_type]
```

### Attention
Les valeurs affichées ne sont pas exactes, car École Directe ne fournit pas les coefficients des contrôles, les moyennes devraient être assez proches de la réalité.
