{
    'name': 'Inherit',
    'author': 'Mohamad Ismail',
    'category': 'project',
    'version': '17.0.0.1.0',
    'depends': ['base','sale','sale_timesheet','project','sale_management'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/project.xml',
        'views/report.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'images': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}
