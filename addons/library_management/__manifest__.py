{
    'name': 'Library Management',  # Tên hiển thị của module
    'version': '18.0.1.0.0',       # Phiên bản (18.0 = Odoo 18)
    'category': 'Tools',           # Danh mục trong Apps
    'summary': 'Quản lý thư viện sáchh', # Mô tả ngắn
    'description': '''                 
        Module quản lý thư viện cho phép:
        - Quản lý sách
        - Theo dõi mượn/trả sách
        - Quản lý độc giả
    ''',
    'author': 'Minh Chien',
    'website': 'https://yourwebsite.com',   # Website
    'depends': ['base', 'mail'],            # Module phụ thuộc
    'data': [                               # Danh sách file dữ liệu
        'security/ir.model.access.csv',
        'data/library_data.xml',
        'views/library_book_views.xml',
        'views/library_author_views.xml', 
        'views/library_menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,                     
    'license': 'LGPL-3',
}