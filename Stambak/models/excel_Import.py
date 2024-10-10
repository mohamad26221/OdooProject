import base64

import pandas as pd

from odoo import models, fields


class ExcelImport(models.Model):
    _name = 'excel.import'
    _description = 'Excel Import'

    file = fields.Binary(string='Excel File', required=True)
    filename = fields.Char(string='Filename')

    def import_data(self):
        if self.file:
            file_data = base64.b64decode(self.file)
            print(file_data)
            df = pd.read_excel(file_data, engine='openpyxl')
            print(df.columns.tolist())

            for index, row in df.iterrows():
                test_name = row['test_name']

                test_record = self.env['tests'].search([('test_name', '=', test_name)], limit=1)

                if not test_record:
                    test_record = self.env['tests'].create({
                        'test_name': test_name,
                        'description': 'test description',
                    })
                age_group = row['age_group'] if pd.notna(row['age_group']) else 0.0
                mean_score = row['mean_score'] if pd.notna(row['mean_score']) else 0.0
                std_deviation = row['std_deviation'] if pd.notna(row['std_deviation']) else 0.0

                self.env['reference'].create({
                    'test_id': test_record.id,
                    'age_group': age_group,
                    'mean_score': mean_score,
                    'std_deviation':std_deviation,
                })
        return True
