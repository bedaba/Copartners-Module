{
'name': "copartners",
'summary': """The Copartners module is designed to help businesses manage partnerships and collaborations with other companies""",
'description': """
his Odoo (v15 community) module, named "copartners", allows users to create a new model with Kanban, Form, and List views. The model includes fields such as Name, Gender, Country, Joining Date, Tags, Customers (multiple selection from Odoo default customers model), Company (selection from Odoo default Companies official model), Notes (a long text field in a new tab named Notes), and Comments (a short text field in a new tab named Comments).

Additionally, the module features a message logger that tracks any change made in the fields and hides the create button from the form view using JavaScript. Moreover, the module allows the generation of a PDF report that contains all the fields except the message logger.
""",
'author': "Bedaba Edward Marko",
'category': 'Sales',
'sequence': 1,
'version': '0.1',
'depends': [
'base',
'mail',
],
'data': [
'reports/copartners_report.xml',
'views/views.xml',
# 'views/templates.xml',
'security/ir.model.access.csv',
],
'license': 'AGPL-3',
'installable': True,
'application': True,
'auto_install': False,
}