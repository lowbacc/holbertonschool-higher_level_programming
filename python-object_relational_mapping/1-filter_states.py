#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )

    # Créer un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Exécuter une requête SQL
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupérer les résultats de la requête
    rows = cursor.fetchall()

    # Afficher les résultats
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()