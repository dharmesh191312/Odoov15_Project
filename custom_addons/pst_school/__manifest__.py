# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'School Management',  #The name of the application
    'author': 'Dharmesh',  #For changing/creating a author name.
    'version': '1.0.0',     #Version Name, can give any.
    'category': 'School',   # Category of the model/application.
    'summary': 'School Management System',   #Visible in summary field
    'description': """School Management System in pst_school module in custom_addons.""",  #Visible in description field
    'depends': [ ],  #
    'data': ['security/ir.model.access.csv',
             'wizard/example_something.xml',
             'views/menu.xml',
             'views/student_view.xml',
             'views/teacher_view.xml',
             'views/book_view.xml'],    #to import the xml files.
    'demo': [ ],     #
    'application': True,   #As the name suggests, but after applying it description is not visible.
    'installable': True,    #makes the model/application installable
    'auto_install': False,   #auto installs the modules
    'sequence': '-100',  #determines the visibility of the created model in the apps list
    # 'icon': '/pst_school/static/description/icon.png',
    # 'assets': { },
    # 'post_init_hook': '_synchronize_cron',
    'license': 'LGPL-3',  #visible in license field
}
