from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'


    name = fields.Char(
        string='Tên tác giả',
        required=True,
        tracking=True
    )
    date_of_birth = fields.Date(
        string='Ngày sinh',
        help='Ngày sinh của tác giả'
    )   

    phone = fields.Char(
        string='Số điện thoại',
        help='Số điện thoại của tác giả'
    )

    address = fields.Text(
        string='Địa chỉ',
        help='Địa chỉ của tác giả'
    )   

    sex = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính', help='Giới tính của tác giả')


    active = fields.Boolean(
        string='Hoạt động',
        default=True
    )

    email = fields.Char(
        string='Email',
        help='Email của tác giả'
    )   

    biography = fields.Text(
        string='Tiểu sử',
        help='Tiểu sử của tác giả'
    )

    cover_image = fields.Binary(
        string='Ảnh đại diện',
        help='Ảnh đại diện của tác giả'
    )

    @api.constrains('name')
    def _check_name(self): 
        for record in self:
            if not record.name:
                raise ValidationError("Tên tác giả không được để trống")
            if len(record.name) < 3:
                raise ValidationError("Tên tác giả phải có ít nhất 3 ký tự")
            

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError("Email không hợp lệ")
    
    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if record.phone and not record.phone.isdigit():
                raise ValidationError("Số điện thoại không hợp lệ")
            
    @api.constrains('biography')
    def _check_biography(self):
        for record in self:
            if record.biography and len(record.biography) < 10:
                raise ValidationError("Tiểu sử tác giả phải có ít nhất 10 ký tự")
            

    