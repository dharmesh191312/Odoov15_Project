# book.py is for managing the book database.
# -*- coding: utf-8 -*-
from odoo import api, fields, models #, _, tools 
# from odoo.osv import expression
# from odoo.exceptions import UserError, ValidationError


class SchoolBook(models.Model):
    _name = "school.book"
    _description = "School Book"

    name = fields.Char(string='Title')
    author = fields.Char(string='Author', required=True)
    publisher = fields.Char(string='Publisher')
    pages = fields.Integer(string='Number of Pages')
    price = fields.Float(string='Price')
    student_taken_ids= fields.Many2many('school.student', string='Students')


    
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