# -*- coding: utf-8 -*-
# © 2009 NetAndCo (<http://www.netandco.net>).
# © 2011 Akretion Benoît Guillot <benoit.guillot@akretion.com>
# © 2014 prisnet.ch Seraphine Lantible <s.lantible@gmail.com>
# © 2016 Serpent Consulting Services Pvt. Ltd.
# © 2018 Daniel Campos <danielcampos@avanzosc.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class ProductModel(models.Model):
    _name = 'product.model'
    _order = 'name'

    name = fields.Char('Model Name', required=True)
    description = fields.Text('Description', translate=True)
    brand_id = fields.Many2one(
        'product.brand',
         string='Brand',
         help='Select a brand for this brand if any.',
         ondelete='restrict'
    )
    logo = fields.Binary('Logo File')
    product_ids = fields.One2many(
        'product.template',
        'product_model_id',
        string='Model Products',
    )
    products_count = fields.Integer(
        string='Number of products',
        compute='_get_products_count',
    )

    @api.multi
    @api.depends('product_ids')
    def _get_products_count(self):
        for model in self:
            model.products_count = len(model.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_model_id = fields.Many2one(
        'product.model',
        string='Model',
        help='Select a model for this product'
    )
