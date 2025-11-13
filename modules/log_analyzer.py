import pandas as pd

class LogAnalyzer:
    def __init__(self, df_logs):
        """
Constructeur qui initialise l'objet LogAnalyzer avec un DataFrame contenant les logs extraits.

        :param df_logs: Le DataFrame contenant les informations extraites des logs.
        """
        self.df_logs = df_logs

    def analyser_frequence_ips(self, intervalle_temps='1min', seuil_alerte=10):
        """
        Analyse la fréquence d'apparition des adresses IP dans les logs.
        Détecte les adresses IP suspectes dépassant un seuil d'alerte.

        :param intervalle_temps: Intervalle de temps pour grouper les requêtes (par défaut '1min').
        :param seuil_alerte: Nombre de requêtes au-delà duquel une adresse IP est considérée comme suspecte.
        :return:
        """
        if not self.df_logs.empty:
            # Convertir la colonne 'Date/Heure' en datetime si ce n'est pas déjà fait
            try:
                self.df_logs['DateHeure'] = pd.to_datetime(self.df_logs['DateHeure'], format='%b %d %H:%M:%S')
            except Exception as e:
                print(f"Erreur lors de la conversion des dates : {e}")
                return

            # Grouper par adresse IP et intervalle de temps
            acces_par_ip = self.df_logs.set_index('DateHeure').groupby(
                [pd.Grouper(freq=intervalle_temps), 'AdresseIP']
            ).size()

            # Filtrer les groupes qui dépassent le seuil d'alerte
            acces_suspects = acces_par_ip[acces_par_ip > seuil_alerte]

            # Afficher les résultats
            if not acces_suspects.empty:
                print(f"\nAccès suspects détectés (plus de {seuil_alerte} accès par IP dans {intervalle_temps}) :")
                print(acces_suspects)
            else:
                print(f"Aucun accès suspect détecté dans l'intervalle de {intervalle_temps}.")
        else:
            print("Le DataFrame est vide. Veuillez charger les logs avant l'analyse.")