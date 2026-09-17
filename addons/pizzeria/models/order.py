from odoo import fields, models


class PizzeriaOrder(models.Model):
    _name = 'pizzeria.order'
    _description = 'Commande restaurant'

    name = fields.Char(string='Référence', required=True)
    table_id = fields.Many2one('pizzeria.table', string='Table')
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    state = fields.Selection(
        [
            ('draft', 'Brouillon'),
            ('confirmed', 'Confirmée'),
            ('done', 'Terminée'),
        ],
        string='État',
        default='draft',
    )
