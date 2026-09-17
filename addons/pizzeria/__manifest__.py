{
    'name': 'Pizzeria',
    'version': '1.0',
    'depends': ['sale'],
    'author': 'Abdeljalil',
    'category': 'Sales',
    'summary': 'Extensions pour Pizza Halal Deluxe',
    'installable': True,
    'application': False,
    'data': [
        'security/ir.model.access.csv',
        'views/table_views.xml',
        'views/order_views.xml',
    ],
}
