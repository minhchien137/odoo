{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Quản lý thư viện sách',
    'description': '''
        Module quản lý thư viện cho phép:
        - Quản lý sách
        - Theo dõi mượn/trả sách
        - Quản lý độc giả
    ''',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/library_data.xml',
        'views/library_book_views.xml',
        'views/library_menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}