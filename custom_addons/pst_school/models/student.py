# student.py is for managing the student database.
# -*- coding: utf-8 -*-
from odoo import api, fields, models  # , _, tools
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


# from odoo.osv import expression
# from odoo.exceptions import UserError, ValidationError


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"
    _rec_name = "name"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    date_of_birth = fields.Date(string="Date Of Birth")
    dob_time = fields.Datetime(string="Date Of Birth & Time")
    remarks = fields.Text(string="Student Remarks")
    html_field = fields.Html(string="HTML Field")
    fav_subject = fields.Selection([('english', 'English'), ('hindi', 'Hindi'), ('maths', 'Maths')],
                                   string="Favourite Subject")
    teachers_ids = fields.One2many('school.teacher', 'student_id' , string='Designated Teacher')
    books_taken_ids = fields.Many2many('school.book', string='Books')
    total_price = fields.Float(string ='Total Price', compute='_compute_total_price')

    # def just_cancel(self):
    #     return

    @api.depends('books_taken_ids.price')
    def _compute_total_price(self):
        for record in self:
            total_price = sum(record.books_taken_ids.mapped('price'))
            record.total_price = total_price

    @api.onchange('date_of_birth')
    def onchange_dob(self):
        if self.date_of_birth:
            date_of_birth = datetime.strptime(str(self.date_of_birth), '%Y-%m-%d').date()
            today = date.today()
            age = relativedelta(today, date_of_birth).years
            self.age = age

    @api.model
    def create(self, vals):
        print("Values are :", vals)
        print("self", self)
        student = super(SchoolStudent, self).create(vals)
        print("Return Statement", student)
        return student

    def write(self, vals):
        student = super(SchoolStudent, self).write(vals)
        print("Return Statement", student)
        return student

    def unlink(self):
        print(self)
        student = super(SchoolStudent, self).unlink()
        print("Return Statement", student)
        return student

    @api.model
    def update_orm(self):
        record = self.search([('name', '=', 'Dharmesh')])
        record.write({'gender': 'Male'})
        print("Updated the blood group of 'Dharmesh'")



# name = fields.Char(string='Account Type', required=True, translate=True)
    # include_initial_balance = fields.Boolean(string="Bring Accounts Balance Forward", help="Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.")
    # type = fields.Selection([
    #     ('other', 'Regular'),
    #     ('receivable', 'Receivable'),
    #     ('payable', 'Payable'),
    #     ('liquidity', 'Liquidity'),
    # ], required=True, default='other',
    #     help="The 'Internal Type' is used for features available on "\
    #     "different types of accounts: liquidity type is for cash or bank accounts"\
    #     ", payable/receivable is for vendor/customer accounts.")
