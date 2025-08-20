{
    'name': 'SVN2 Sigma - Quản lý thư viện sách',           # Tên hiển thị của module
    'version': '18.0.1.0.0',              # Phiên bản (18.0 = Odoo 18)
    'category': 'Tools',                   # Danh mục trong Apps
    'summary': 'SVN2 - Quản lý thư viện sách',    # Mô tả ngắn
    'description': '''...''',              # Mô tả chi tiết
    'author': 'Sigma',                 # Tác giả
    'website': 'https://sigmaworldwide.io/',  # Website
    'depends': ['base', 'mail'],           # Module phụ thuộc
    'data': [
        'security/ir.model.access.csv',     # Phân quyền
        'views/library_book_views.xml',     # View cho sách
        'views/library_menus.xml',          # Menu
        'data/library_data.xml',            # Dữ liệu mẫu
        ],                       
    'installable': True,                   # Có thể cài đặt
    'auto_install': False,                 # Không tự động cài
    'application': True,                   # Là ứng dụng chính
    'license': 'LGPL-3',                  # Giấy phép
}