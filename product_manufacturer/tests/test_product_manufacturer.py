# -*- coding: utf-8 -*-
# Copyright 2018 Tecnativa - David Vidal
# Copyright 2019 Pudu Technology - Felipe Angulo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from odoo.tests import common


class TestProductManufacturer(common.TransactionCase):

    def setUp(self):
        super(TestProductManufacturer, self).setUp()
        self.product = self.env.ref('product.product_product_4')
        self.supplier = self.ref('base.res_partner_2')
        self.product_model_obj = self.env['product.manufacturer']
        self.product_model = self.product_model_obj.create(
            {'name': 'Test manufacturer',
             'description': 'Test manufacturer description',
             'partner_id': self.supplier
             })

    def test_products_count(self):
        self.assertEqual(self.product_manufacturer.products_count, 0,
                         'Error product count does not match')
        self.product.product_model_id = self.product_model.id
        self.assertEqual(self.product_manufacturer.products_count, 1,
                         'Error product count does not match')
