{
    'name': 'Sakan',
    'author': 'Mohamad Ismail',
    'category': 'Uncategorized',
    'version': '17.0.0.1.0',
    'depends': ['base','sale_management','account','mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'views/base_menu.xml',
        'views/university_view.xml',
        'views/unit_view.xml',
        'views/rooms_view.xml',
        'views/student_view.xml',
        'views/sale_order_view.xml',
        'views/register_student_view.xml',
        'views/room_history.xml',
        'wizard/change_state_wizard_view.xml',
        'reports/student_report.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'Sakan/static/src/css/student.css',
            'Sakan/static/src/css/rooms.css']
    },
    'license': 'LGPL-3'
}
