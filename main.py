# Fichier d'entree principal du projet.
# C'est ce fichier qu'il faudra appeler principalement pour executer le programme.

# on peut s'inspirer de cet exemple :

# https://github.com/voirinprof/geo_pipeline_sample

# on peut essayer de séparer les fonctions 
# dans plusieurs modules : ingest.py, process.py, analyse.py, ...

# donc j'utiliserais le code de mon collègue pour le module ingest.py, et je vais l'importer ici.

from src.ingest import read_grid

filename = "data/raw/image_spuk.grd"

lines = read_grid(filename)

print(f"Nombre de lignes dans le fichier déchiffré : {len(lines)}")
