{
    'name': 'Sakan',
    'author': 'Mohamad Ismail',
    'category': 'Uncategorized',
    'version': '17.0.0.1.0',
    'depends': ['base','sale_management','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/university_view.xml',
        'views/unit_view.xml',
        'views/rooms_view.xml',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'Sakan/static/src/css/student.css']
    },
    'license': 'LGPL-3'
}
