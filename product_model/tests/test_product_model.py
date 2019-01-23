# Copyright (c) 2018 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests import common


class TestProductModel(common.TransactionCase):

    def setUp(self):
        super(TestProductModel, self).setUp()
        self.product = self.env.ref('product.product_product_4')
        self.supplier = self.ref('base.res_partner_2')
        self.product_model_obj = self.env['product.model']
        self.product_model = self.product_model_obj.create(
            {'name': 'Test Model',
             'description': 'Test model description',
             'partner_id': self.supplier
             })

    def test_products_count(self):
        self.assertEqual(self.product_model.products_count, 0,
                         'Error product count does not match')
        self.product.product_model_id = self.product_model.id
        self.assertEqual(self.product_model.products_count, 1,
                         'Error product count does not match')
