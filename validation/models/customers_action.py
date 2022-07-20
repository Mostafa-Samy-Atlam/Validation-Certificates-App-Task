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


class CustomerAction(models.Model):
    _name = "customers.action"
    _description = "menus to view/create certificate types"
    name = fields.Char(required=True)
    phone = fields.Char(required=True)
    certificate_id = fields.One2many("vehicle.certificate", "customer")
    department = fields.Many2many("traffic.department")

    @api.constrains("phone")
    def _validate_phone_number(self):
        reg = r'^01[0125][0-9]{8}$'
        if not re.fullmatch(reg, self.phone):
            raise ValidationError("Wrong Phone Number")

    _sql_constraints = [('duplicate_phone', 'UNIQUE(phone)', 'Phone Number already exists')]

