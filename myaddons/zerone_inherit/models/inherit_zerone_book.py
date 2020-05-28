# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Author:       ZERONE
# Date:         2020/2/11 下午12:36
# Description:  

# -------------------------------------------------------------------------------

from odoo import api, fields, models, _

import base64
import binascii
import codecs
import collections
import unicodedata

import chardet
import datetime
import io
import itertools
import logging
import psycopg2
import operator
import os
import re
import requests
import math
from PIL import Image

from odoo import api, fields, models
from odoo.exceptions import AccessError
from odoo.tools.translate import _
from odoo.tools.mimetypes import guess_mimetype
from odoo.tools import config, DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, pycompat

FIELDS_RECURSION_LIMIT = 2
ERROR_PREVIEW_BYTES = 200
DEFAULT_IMAGE_TIMEOUT = 3
DEFAULT_IMAGE_MAXBYTES = 10 * 1024 * 1024
DEFAULT_IMAGE_REGEX = r"^(?:http|https)://"
DEFAULT_IMAGE_CHUNK_SIZE = 32768
IMAGE_FIELDS = ["icon", "image", "logo", "picture"]
_logger = logging.getLogger(__name__)
BOM_MAP = {
    'utf-16le': codecs.BOM_UTF16_LE,
    'utf-16be': codecs.BOM_UTF16_BE,
    'utf-32le': codecs.BOM_UTF32_LE,
    'utf-32be': codecs.BOM_UTF32_BE,
}

try:
    import xlrd

    try:
        from xlrd import xlsx
    except ImportError:
        xlsx = None
except ImportError:
    xlrd = xlsx = None

try:
    from . import odf_ods_reader
except ImportError:
    odf_ods_reader = None

FILE_TYPE_DICT = {
    'text/csv': ('csv', True, None),
    'application/vnd.ms-excel': ('xls', xlrd, 'xlrd'),
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ('xlsx', xlsx, 'xlrd >= 1.0.0'),
    'application/vnd.oasis.opendocument.spreadsheet': ('ods', odf_ods_reader, 'odfpy')
}
EXTENSIONS = {
    '.' + ext: handler
    for mime, (ext, handler, req) in FILE_TYPE_DICT.items()
}


class ZeroneBook(models.Model):
    _inherit = "zerone.book"

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('zerone.book.sequence') or '/'
        res = super(ZeroneBook, self).create(vals)
        return res


class Import(models.TransientModel):
    _inherit = 'base_import.import'

    special_model = ['zerone.book']
    special_key = ['定价']

    def float_ceil(self, model_name):
        if model_name in self.special_model:
            return True
        else:
            return False

    def _read_xls_book(self, book):
        should_float = self.float_ceil(self.res_model)
        sheet = book.sheet_by_index(0)
        # emulate Sheet.get_rows for pre-0.9.4
        special_key_index = []
        for rowx, row in enumerate(map(sheet.row, range(sheet.nrows)), 1):
            if rowx == 1:
                col_info = [[int(colx), str(cell)] for colx, cell in enumerate(row, 1)]
                for item1 in self.special_key:
                    for item2 in col_info:
                        if item1 in item2[1]:
                            special_key_index.append(item2[0])
                            break

            values = []
            for colx, cell in enumerate(row, 1):
                if cell.ctype is xlrd.XL_CELL_NUMBER:
                    is_float = cell.value % 1 != 0.0
                    if should_float:
                        values.append(
                            str(math.ceil(cell.value)) if is_float else str(int(cell.value))
                        )
                    else:
                        values.append(
                            str(cell.value) if is_float else str(int(cell.value))
                        )
                elif cell.ctype is xlrd.XL_CELL_DATE:
                    is_datetime = cell.value % 1 != 0.0
                    # emulate xldate_as_datetime for pre-0.9.3
                    dt = datetime.datetime(*xlrd.xldate.xldate_as_tuple(cell.value, book.datemode))
                    values.append(
                        dt.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
                        if is_datetime
                        else dt.strftime(DEFAULT_SERVER_DATE_FORMAT)
                    )
                elif cell.ctype is xlrd.XL_CELL_BOOLEAN:
                    values.append(u'True' if cell.value else u'False')
                elif cell.ctype is xlrd.XL_CELL_ERROR:
                    raise ValueError(
                        _("Invalid cell value at row %(row)s, column %(col)s: %(cell_value)s") % {
                            'row': rowx,
                            'col': colx,
                            'cell_value': xlrd.error_text_from_code.get(cell.value,
                                                                        _("unknown error code %s") % cell.value)
                        }
                    )
                else:
                    values.append(cell.value)
            if any(x for x in values if x.strip()):
                yield values
