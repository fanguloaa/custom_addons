# -*- coding: utf-8 -*-
# Copyright 2018 Tecnativa - David Vidal
# Copyright 2019 Pudu Technology - Felipe Angulo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    product_brand_id = fields.Many2one(
        'product.manufacturer',
        string='Manufacturer',
    )

    def _select(self):
        select_str = super(SaleReport, self)._select()
        select_str += """
            , t.product_manufacturer_id
            """
        return select_str

    def _group_by(self):
        group_by_str = super(SaleReport, self)._group_by()
        group_by_str += ", t.product_manufacturer_id"
        return group_by_str
