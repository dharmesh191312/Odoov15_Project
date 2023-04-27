# teacher.py is for managing the teacher database.
# -*- coding: utf-8 -*-
from odoo import api, fields, models  # , _, tools


# from odoo.osv import expression
# from odoo.exceptions import UserError, ValidationError


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "School Teacher"
    # _rec_name = "age"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    phone = fields.Char(string='Phone Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    address = fields.Text(string="Address")
    student_id = fields.Many2one(comodel_name='school.student', string="Designated Student")

    # @api.depends('name', 'phone')
    # def name_get(self):
    #     res = []
    #     for record in self:
    #         name = record.name
    #         phone = record.phone
    #         if phone:
    #             name = '%s (%s)' % (name, phone)
    #         res.append((record.id, name))
    #     return res

    # date_of_birth = fields.Date(string="Date Of Birth")
    # dob_time = fields.Datetime(string="Date Of Birth & Time")
    # remarks = fields.Text(string="Student Remarks")

    # html_field = fields.Html(string= "HTML Field")
    # fav_subject = fields.Selection([('english','English'),('hindi','Hindi'),('maths','Maths')], string="Favourite Subject")

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
