from odoo import models, fields, api
from odoo.fields import Many2one
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"
    certificates_id = fields.One2many("vehicle.certificate", "customer_crm")
    department = fields.Many2many("traffic.department")
