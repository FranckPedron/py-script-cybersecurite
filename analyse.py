import argparse

from modules.log_reader import LogReader


def main():
    parser = argparse.ArgumentParser(description="Script d'analyse de logs")
    parser.add_argument("repertoire", help="Chemin vers le répertoire contenant les fichiers de logs", type=str)
    parser.add_argument("--pattern", help="Pattern pour filtrer les fichiers de logs (par défaut 'secure*')", type=str,
                        default="secure*")
    args = parser.parse_args()

    # Créer une instance de LogReader avec le chemin du répertoire
    lecteur = LogReader(args.repertoire)

    # Trouver tous les fichiers de logs correspondant au pattern dans le répertoire
    fichiers_logs = lecteur.trouver_fichiers_logs(pattern=args.pattern)

    # Si des fichiers de logs sont trouvés, les lire un par un
    if fichiers_logs:
        for fichier_log in fichiers_logs:
            print(f"\nLecture du fichier : {fichier_log}")
            lecteur.lire_logs(fichier_log)  # Lire le fichier de logs

        # Afficher les lignes lues
        lecteur.afficher_lignes_lues()
    else:
        print(f"Aucun fichier de logs correspondant au pattern '{args.pattern}' n'a été trouvé dans le répertoire.")


if __name__ == "__main__":
    main()
