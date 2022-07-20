from odoo import models, fields, api
from odoo.fields import Many2one
from odoo.exceptions import UserError, ValidationError
import re
import datetime
from datetime import date
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class VehicleCertificate(models.Model):
    _name = "vehicle.certificate"
    _description = "menus to view/create vehicle validation certificates"
    _rec_name = "customer_crm"
    serial_number = fields.Char(required=True)
    vehicle_type = fields.Selection([
        ("Car", "Car"),
        ("Bus", "Bus"),
        ("Minibus", "Minibus"),
        ("Microbus", "Microbus"),
    ])

    certificate_type = fields.Many2one('certificate.type')
    customer = fields.Many2one("customers.action")
    customer_crm = fields.Many2one("res.partner")
    price = fields.Integer()
    chassis_number = fields.Integer()
    department = fields.Many2many("traffic.department")
    brand = fields.Many2one("certificate.brand")
    car_model = fields.Selection(
        selection=[(str(date.today().year - i), str(date.today().year - i)) for i in range(21)])
    my_seq = fields.Char('Serial Number')

    @api.model
    def create(self, vals):
        vals['my_seq'] = self.env['ir.sequence'].next_by_code('code')
        return super(VehicleCertificate, self).create(vals)

    @api.constrains("serial_number")
    def _validate_serial_number(self):
        # regex = r'\b[TD][0-9]\b'
        regex = r'^TD[0-9]{5}$'
        if not re.fullmatch(regex, self.serial_number):
            raise ValidationError("Wrong Serial Number")

    _sql_constraints = [('duplicate_serial_number', 'UNIQUE(serial_number)', 'Serial Number already exists')]


class Brand(models.Model):
    _name = "certificate.brand"
    brand = fields.One2many("vehicle.certificate", "brand")
