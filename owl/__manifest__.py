{
    'name': 'OWL Tutorial',
    'author': 'Mohamad',
    'description': """OWL Tutorial Custom Dashboard""",
    'category': 'OWL',
    'sequence': -1,
    'version': '17.0.0.1.0',
    'depends': ['base', 'web', 'sale', 'board'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/sales_dashboard.xml',
    ],
    'demo': [
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'owl/static/src/components/*/*.js',
    #         'owl/static/src/components/*/*.xml',
    #         'owl/static/src/components/*/*.scss',
    #     ],
    # },
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
