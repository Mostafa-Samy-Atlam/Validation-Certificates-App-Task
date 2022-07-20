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


class CertificateType(models.Model):
    _name = "certificate.type"
    _description = "menus to view/create certificate types"
    name = fields.Char(required=True)
    certificate_id = fields.One2many("vehicle.certificate", "certificate_type")
