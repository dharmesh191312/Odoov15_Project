from odoo import api, fields ,models

class example(models.TransientModel):
    _name= "example.something"
    _description= "Creating a Transient Model"

    student_wizard = fields.Many2one('school.student',string='Student Wizard')
    student_name = fields.Char(string='Name')
    remarks = fields.Text(string='Remarks')



# Function for Button in example_something.xml
    def action_cancel(self):
        return