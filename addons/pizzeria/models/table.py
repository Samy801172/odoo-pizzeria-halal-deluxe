# Import des outils Odoo : models = base des tables, fields = types de colonnes
from odoo import fields, models


class PizzeriaTable(models.Model):
    # Héritage de models.Model : obligatoire pour toute table Odoo (comme sale.order).
    # PizzeriaTable = nom de la classe Python (pour nous).
    # models.Model = classe mère qui fournit l'ORM (create, search, write…).

    _name = 'pizzeria.table'
    # Identifiant technique du modèle. Odoo crée la table SQL "pizzeria_table".
    # _name = nouvelle table | _inherit = étendre une table existante

    _description = 'Table de restaurant'
    # Libellé affiché en mode développeur (pas une colonne en base).

    name = fields.Char(string='Numéro de table', required=True)
    # Char = texte court. required=True = obligatoire à la saisie.

    seats = fields.Integer(string='Nombre de places')
    # Integer = nombre entier (2, 4, 6…).

    state = fields.Selection(
        [
            ('free', 'Libre'),        # valeur en base | texte à l'écran
            ('occupied', 'Occupée'),
            ('reserved', 'Réservée'),
        ],
        string='État',
        default='free',               # nouvelle table = Libre par défaut
    )
    # Selection = liste de choix (comme draft/sale sur une commande).
