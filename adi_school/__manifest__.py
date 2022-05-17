{
    'name' : 'School Management',
    'version' : '1.1',
    'author' : 'Planet Odoo',
    'description': """ First Project of Aditya Nachan""",
    'sequence':1,
    'category': '',
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/school_view.xml',
        'views/student_details_view.xml',

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
