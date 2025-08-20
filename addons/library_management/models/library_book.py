from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(
        string='Tên sách',
        required=True,
        tracking=True
    )
    
    author = fields.Char(
        string='Tác giả',
        required=True,
        tracking=True
    )
    
    isbn = fields.Char(
        string='ISBN',
        help='Mã số sách quốc tế'
    )
    
    publisher = fields.Char(
        string='Nhà xuất bản'
    )
    
    publication_date = fields.Date(
        string='Ngày xuất bản'
    )
    
    pages = fields.Integer(
        string='Số trang'
    )
    
    category = fields.Selection([
        ('fiction', 'Tiểu thuyết'),
        ('non_fiction', 'Phi tiểu thuyết'),
        ('science', 'Khoa học'),
        ('technology', 'Công nghệ'),
        ('history', 'Lịch sử'),
        ('biography', 'Tiểu sử'),
        ('other', 'Khác')
    ], string='Thể loại', default='other')
    
    state = fields.Selection([
        ('available', 'Có sẵn'),
        ('borrowed', 'Đã mượn'),
        ('maintenance', 'Bảo trì'),
        ('lost', 'Mất')
    ], string='Trạng thái', default='available', tracking=True)
    
    borrower_id = fields.Many2one(
        'res.partner',
        string='Người mượn',
        domain=[('is_company', '=', False)]
    )
    
    borrow_date = fields.Date(
        string='Ngày mượn'
    )
    
    return_date = fields.Date(
        string='Ngày trả dự kiến'
    )
    
    description = fields.Text(
        string='Mô tả'
    )
    
    cover_image = fields.Binary(
        string='Ảnh bìa'
    )
    
    active = fields.Boolean(
        string='Hoạt động',
        default=True
    )

    @api.constrains('isbn')
    def _check_isbn(self):
        for record in self:
            if record.isbn and len(record.isbn.replace('-', '').replace(' ', '')) not in [10, 13]:
                raise ValidationError("ISBN phải có 10 hoặc 13 chữ số")

    @api.constrains('pages')
    def _check_pages(self):
        for record in self:
            if record.pages and record.pages <= 0:
                raise ValidationError("Số trang phải lớn hơn 0")

    @api.constrains('borrow_date', 'return_date')
    def _check_dates(self):
        for record in self:
            if record.borrow_date and record.return_date:
                if record.return_date < record.borrow_date:
                    raise ValidationError("Ngày trả không thể nhỏ hơn ngày mượn")

    def action_borrow(self):
        """Hành động mượn sách"""
        self.write({
            'state': 'borrowed',
            'borrow_date': fields.Date.today()
        })
        
    def action_return(self):
        """Hành động trả sách"""
        self.write({
            'state': 'available',
            'borrower_id': False,
            'borrow_date': False,
            'return_date': False
        })

    def action_maintenance(self):
        """Đưa sách vào bảo trì"""
        self.write({'state': 'maintenance'})

    def action_available(self):
        """Đánh dấu sách có sẵn"""
        self.write({'state': 'available'})