import os
import unittest
import json
import random
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import setup_db, App_User, Ad_Category_Area, Ad_Area, Ad_Category_Area, App_Group, app_user_group, db, Ad_Category


''' Please change before test '''

bearer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpLNExvWVllVmFSWFE0Zm9rUkZXZCJ9.eyJpc3MiOiJodHRwczovL3dlYmNvZmZlZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMmNlNDgzOGFhOWIwYmU3NWRmZjhlIiwiYXVkIjoiU1BTTVMtQVBJLURFViIsImlhdCI6MTU5MDk1NDM0NywiZXhwIjoxNTkxMDQwNzQ3LCJhenAiOiIxNnpCVVhXVjNiTzlxZGxRalJpS0VndERSbTBLRmd5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFyZWEiLCJnZXQ6Y2F0ZWdvcnkiLCJnZXQ6Z3JvdXAiLCJnZXQ6c2FsZXMiLCJnZXQ6dXNlciIsInBvc3Q6YXJlYSIsInBvc3Q6Y2F0ZWdvcnkiLCJwb3N0Omdyb3VwIiwicG9zdDpzYWxlcyIsInBvc3Q6dXNlciJdfQ.CauGXcVvFhIt4bHmd-FPPtdyM6weCEnispquUPCE90yRS3ZDbukQZIksx_FmFiErWCs0bWkhSDz-s0uxf77EYoHymuTW-Zb2SVJpSzYmxElVlHsNgwPP29cnpPeD-LR9o3piC33KIst34Uf0R5pUkLHVC-2l1bKFx_U5gz1Jnf9qqpHtZ4PxD2Yaxy57zs4mR81DiGDOA2H5dqPhhcXhxPeyjxuBW2X17D-SNTaTcTwMFfAr-Jz8D3hxlk6C7DmIOJqhvnesF6WEt_v5GBXckrnnr8duPmIwT8AiTR-wop2OwkDKX2LwIvvoGJNbbDR0_Y0sV43fOaxMsP_NXxTVNg'
bearer_token_sales = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpLNExvWVllVmFSWFE0Zm9rUkZXZCJ9.eyJpc3MiOiJodHRwczovL3dlYmNvZmZlZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjOGU4Yzc5YzVjYmUwYzFhYzM3ZjIwIiwiYXVkIjoiU1BTTVMtQVBJLURFViIsImlhdCI6MTU5MDk1NDY4MSwiZXhwIjoxNTkxMDQxMDgxLCJhenAiOiIxNnpCVVhXVjNiTzlxZGxRalJpS0VndERSbTBLRmd5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFyZWEiLCJnZXQ6Y2F0ZWdvcnkiLCJnZXQ6c2FsZXMiLCJwb3N0OnNhbGVzIl19.B9S6TWEVhScbcLqkdN1rIs_t2sYL8Wg5m_-pFaCk71WOhQTGD6Xp1HEYWt3kRTcq3ovHsAC5qfRCGEKB-oTo7wS6N53ourtj5p2rU4-P4U2LzRtR25EiwmfE0JZWXYI7wc4Cbc4Sp2_SNIpg_CHgI3aI24EMQotMzQ4aam8gjbUiPVDP3i_hXyDqD5NqqD1T3IhZKFN9x797BKs7THDEe-OAxyn7Yf69WtINTvTUfAXRDJHocGZSc1ya9l66qXlSJRRDILta5eszLo6C46yv23OCm0294fGrTIQJwZgRl2Szossyw8NJjE16uE3lVqHLbLcA-C0lemC6UT73n5UDEw'

''' DO NOT CHANGE THE KEYS BELOW'''
bearer_token_wrong = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6I'
bearer_token_expired = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpLNExvWVllVmFSWFE0Zm9rUkZXZCJ9.eyJpc3MiOiJodHRwczovL3dlYmNvZmZlZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMmNlNDgzOGFhOWIwYmU3NWRmZjhlIiwiYXVkIjoiU1BTTVMtQVBJLURFViIsImlhdCI6MTU5MDQzMTg2NCwiZXhwIjoxNTkwNDM5MDY0LCJhenAiOiIxNnpCVVhXVjNiTzlxZGxRalJpS0VndERSbTBLRmd5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFyZWEiLCJnZXQ6Y2F0ZWdvcnkiLCJnZXQ6Z3JvdXAiLCJnZXQ6c2FsZXMiLCJnZXQ6dXNlciIsInBvc3Q6YXJlYSIsInBvc3Q6Y2F0ZWdvcnkiLCJwb3N0Omdyb3VwIiwicG9zdDpzYWxlcyIsInBvc3Q6dXNlciJdfQ.CqjwTdu-7VynU6RLqttpKMGOvmW66Gy4Ss0-8wjTYex13TS40pDw7WCGNDWqhJ7ozXa7rP58UUSvU5-LOAYxn9WLErnX8scfqSMcILS1nR382ajQevsuv6RlDJrp9s-tmiEyjWG-NLyJuVa1D2HwjK3qp5pVXXcdqzwVDE_n5Qh7Ph1zssdJ6m0RaDV8MdaWvf4RtYUuMLW1-3OV6f8RZ74srGi6xRYYoqrOelMgbLyQB-u4MvlNsz0tjfYZ3ZwZxW0D-uTS0Q29izrcqQ9pwKnFOBUfGCIVY-RPf-NhpfFttz9VDHG23t9qNwoPihhkurwltcIaJniUuxEfgfRwFQ'


class SpsmsTestCases(unittest.TestCase):
    '''This class represents the test cases for SPSMS App'''

    def setUp(self):
        '''Define test variables and initialize web app'''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

        self.category = {
            "name": "Testing Category",
            "code": "TESTRND202000100123",
            "mm_min": 5,
            "mm_max": 370,
            "column_min": 1,
            "column_max": 7,
            "notes": "Category for Testing - DO NOT USE"
        }

        self.area = {
            "name": "Testing Area - DO NOT USE",
            "code": "TESTAREARND202000100123",
            "gp_mm_price": 7.00,
            "gp_mm_price_text": 4.00,
            "dp_mm_price": 5.00,
            "dp_mm_price_text": 2.50
        }

    def tearDown(self):
        """Executed after reach test"""
        # print('----------------')
        pass

    # ##################################
    # Categories
    # ##################################

    def test_1a_get_categories(self):
        print('##### Check GET categories Endpoint #####')
        res = self.client().get('/categories/',
                                headers=[
                                    ('Content-Type', 'application/json'),
                                    ('Authorization', f'Bearer {bearer_token}')
                                ]
                                )
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def test_1b_get_categories(self):
        print('##### Check BAD GET categories Endpoint #####')
        res = self.client().get('/categories/10000000000000000',
                                headers=[
                                    ('Content-Type', 'application/json'),
                                    ('Authorization', f'Bearer {bearer_token}')
                                ]
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_1c_post_categories(self):
        print('##### Check POST categories Endpoint #####')
        res = self.client().post('/categories/',
                                 json=self.category,
                                 headers=[
                                     ('Content-Type', 'application/json'),
                                     ('Authorization',
                                      f'Bearer {bearer_token}')
                                 ]
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_1d_delete_categories(self):
        print('##### Check DELETE categories Endpoint #####')
        last_entry_id = (Ad_Category.query.with_entities(
            Ad_Category.id).filter(Ad_Category.code == self.category['code']).first())

        res = self.client().delete('/categories/' + str(last_entry_id[0]),
                                   headers=[
                                       ('Content-Type', 'application/json'),
                                       ('Authorization',
                                           f'Bearer {bearer_token}')
        ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_1e_delete_categories(self):
        print('##### Check BAD DELETE categories Endpoint #####')
        last_entry_id = (Ad_Category.query.with_entities(
            Ad_Category.id).filter(Ad_Category.code == 'TESTRND202000100123').first())
        if not last_entry_id:
            last_entry_id = [10000020202020202020]

        res = self.client().delete('/categories/' + str(last_entry_id[0]),
                                   headers=[
                                       ('Content-Type', 'application/json'),
                                       ('Authorization',
                                           f'Bearer {bearer_token}')
        ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    # ##################################
    # Areas
    # ##################################

    def test_2a_get_areas(self):
        print('##### Check GET areas Endpoint #####')
        res = self.client().get('/areas/',
                                headers=[
                                    ('Content-Type', 'application/json'),
                                    ('Authorization', f'Bearer {bearer_token}')
                                ]
                                )
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def test_2b_get_areas(self):
        print('##### Check BAD GET areas Endpoint #####')
        res = self.client().get('/areas/ergtertgertgertg/',
                                headers=[
                                    ('Content-Type', 'application/json'),
                                    ('Authorization', f'Bearer {bearer_token}')
                                ]
                                )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_2c_post_areas(self):
        print('##### Check POST areas Endpoint #####')
        res = self.client().post('/areas/',
                                 json=self.area,
                                 headers=[
                                     ('Content-Type', 'application/json'),
                                     ('Authorization',
                                      f'Bearer {bearer_token}')
                                 ]
                                 )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_2d_delete_areas(self):
        print('##### Check DELETE areas Endpoint #####')
        last_entry_id = (Ad_Area.query.with_entities(
            Ad_Area.id).filter(Ad_Area.code == self.area['code']).first())
        resCode = 200

        if not last_entry_id:
            last_entry_id = [10000020202020202020]
            resCode = 404

        res = self.client().delete('/areas/' + str(last_entry_id[0]),
                                   json=self.area,
                                   headers=[
                                       ('Content-Type', 'application/json'),
                                       ('Authorization',
                                           f'Bearer {bearer_token}')
        ]
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, resCode)

    def test_2e_get_areas_wrong_key(self):
        print('##### Check GET areas Endpoint with expired AUTH #####')
        res = self.client().get('/areas/',
                                headers=[
                                    ('Content-Type', 'application/json'),
                                    ('Authorization',
                                     f'Bearer {bearer_token_expired}')
                                ]
                                )
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code, 401)

    def test_2f_get_areas_without_key(self):
        print('##### Check GET areas Endpoint without AUTH #####')
        res = self.client().get('/areas/',
                                headers=[
                                    ('Content-Type', 'application/json')
                                ]
                                )
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code, 401)

    # ##################################
    # users
    # ##################################
    def test_3a_get_users(self):
        print('##### Check GET users Endpoint #####')
        res = self.client().get('/users/',
                                headers=[
                                    ('Content-Type', 'application/json'),
                                    ('Authorization',
                                     f'Bearer {bearer_token}')
                                ]
                                )
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def test_3b_missing_user_rights(self):
        print('##### Check GET users Endpoint without permission #####')
        res = self.client().get('/users/',
                                headers=[
                                    ('Content-Type', 'application/json'),
                                    ('Authorization',
                                     f'Bearer {bearer_token_sales}')
                                ]
                                )
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
