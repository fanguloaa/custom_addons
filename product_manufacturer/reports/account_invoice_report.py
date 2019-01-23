# -*- coding: utf-8 -*-
# Copyright 2018 Tecnativa - David Vidal
# Copyright 2019 Pudu Technology - Felipe Angulo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    product_manufacturer_id = fields.Many2one(
        'product.manufacturer',
        string='Manufacturer',
    )

    def _select(self):
        select_str = super(AccountInvoiceReport, self)._select()
        select_str += """
            , sub.product_manufacturer_id as product_manufacturer_id
            """
        return select_str

    def _sub_select(self):
        select_str = super(AccountInvoiceReport, self)._sub_select()
        select_str += """
            , pt.product_manufacturer_id
            """
        return select_str

    def _group_by(self):
        group_by_str = super(AccountInvoiceReport, self)._group_by()
        group_by_str += ", pt.product_manufacturer_id"
        return group_by_str
