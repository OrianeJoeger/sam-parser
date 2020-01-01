# Analyse de fichier SAM


## Installation

Utiliser la version 3.6 de python pour lancer le projet

```bash
sudo apt-get install python3.6
```

## Usage

Affichage d'une aide à l'utilisation

```bash
python3 sam-parser.py --help
```
```output
Utilisation: python3 main.py [FICHIER] [METHOD]
[FICHIER] fichier de type SAM
[METHOD] la méthode utilisé doit être 'flag' or 'cigar'
```

### Methode Cigar
```bash
python3 sam-parser.py data/mapping.sam cigar
```

### Methode Flag
```bash
python3 sam-parser.py data/mapping.sam flag
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.