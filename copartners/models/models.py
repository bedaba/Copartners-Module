# -*- coding: utf-8 -*-

from odoo import models, fields, api


class copartners(models.Model):
    _name = 'copartners.copartners'
    _inherit = ['mail.thread']
    _description = 'copartners.copartners'

    name = fields.Char(string="Name", required=True, track_visibility='always')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', track_visibility='always')
    country = fields.Char(string="Country", track_visibility='always')
    joining_date = fields.Date(string="Date", track_visibility='always')
    tags = fields.Char(string="Tags", track_visibility='always')
    customers = fields.Many2many('res.users', string="Customers", track_visibility='always')
    company = fields.Many2one('res.company', ondelete='cascade', string="Company", index=True, required=True, track_visibility='always')
    notes = fields.Text(string="Notes", track_visibility='always')
    comments = fields.Char(string="Comments", track_visibility='always')
