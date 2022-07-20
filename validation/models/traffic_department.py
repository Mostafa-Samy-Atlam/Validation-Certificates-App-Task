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


class TrafficDepartment(models.Model):
    _name = "traffic.department"
    _description = "menus to view/create traffic departments"
    name = fields.Char(required=True)

