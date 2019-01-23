# -*- coding: utf-8 -*-
# © 2009 NetAndCo (<http://www.netandco.net>).
# © 2011 Akretion Benoît Guillot <benoit.guillot@akretion.com>
# © 2014 prisnet.ch Seraphine Lantible <s.lantible@gmail.com>
# © 2016 Serpent Consulting Services Pvt. Ltd.
# © 2018 Daniel Campos <danielcampos@avanzosc.es>
# © 2019 Felipe Angulo <felipe@pudutechnology.cl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class ProductManufacturer(models.Model):
    _name = 'product.manufacturer'
    _order = 'name'

    name = fields.Char('Manufacturer Name', required=True)
    description = fields.Text('Description', translate=True)
    country_id = fields.Many2one(
        'res.country',
         string='Country',
         help='Select a country for this manufacturer',
         ondelete='restrict'
    )
    logo = fields.Binary('Logo File')
    product_ids = fields.One2many(
        'product.template',
        'product_manufacturer_id',
        string='Manufacturer Products',
    )
    products_count = fields.Integer(
        string='Number of products',
        compute='_get_products_count',
    )

    @api.multi
    @api.depends('product_ids')
    def _get_products_count(self):
        for manufacturer in self:
            manufacturer.products_count = len(manufacturer.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_manufacturer_id = fields.Many2one(
        'product.manufacturer',
        string='Manufacturer',
        help='Select a manufacturer for this product'
    )
