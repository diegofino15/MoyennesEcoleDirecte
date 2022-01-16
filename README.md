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


```console
python3 main.py [identifiant]
python3 main.py [identifiant] [return_type]
```

### Système de compte
Vous pouvez lancer le script en écrivant : "python main.py [identifiant] [return_type] -save" pour sauvegarder les informations, et vous pourrez relancer le script avec aucun arguments encore deux fois avant qu'il faille confirmer le mot de passe.

### Attention
Les moyennes affichées ne sont pas exactes, car École Directe ne fournit pas les coefficients des contrôles, mais les moyennes devraient cependant être assez proches de la réalité.
