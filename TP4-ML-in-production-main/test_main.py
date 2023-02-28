import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_name(self):
        response = self.app.get('/api/hello/ben')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'hello': 'ben'})

    def test_model(self):
        response = self.app.get('/classify/[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,78,136,167,184,181,177,168,149,135,136,140,136,141,170,168,172,162,140,81,0,0,0,0,1,4,0,52,255,221,199,238,192,199,228,196,247,196,238,210,216,243,192,239,188,219,232,224,255,70,0,0,0,0,0,216,203,215,210,218,212,224,229,197,224,205,227,221,212,215,209,238,217,228,218,213,227,212,2,0,0,0,21,196,224,216,213,216,217,217,150,101,255,242,176,205,255,165,101,220,229,220,222,235,216,241,87,0,0,2,232,208,188,227,231,234,254,184,214,157,239,72,133,65,184,209,179,200,234,246,240,233,225,217,255,0,0,43,218,207,213,217,212,193,187,146,101,203,236,94,115,74,202,233,156,100,224,185,226,210,225,230,188,0,0,83,208,204,181,225,202,110,63,211,173,200,220,253,119,223,248,207,171,210,143,64,163,190,231,228,236,25,0,72,173,212,198,214,238,203,166,224,119,187,190,147,248,203,130,206,138,179,207,170,239,240,222,217,207,34,0,49,125,210,186,222,246,223,142,151,202,204,191,199,254,231,171,203,203,170,137,192,255,229,225,237,199,31,0,31,159,210,193,228,145,245,255,140,208,174,226,143,240,141,201,198,202,150,211,255,131,211,228,208,228,42,0,27,171,209,209,245,165,110,163,206,182,196,191,168,253,194,155,203,182,197,197,99,139,247,229,234,244,22,0,74,209,212,179,228,255,132,110,240,165,186,253,226,165,201,253,227,158,203,211,51,234,241,224,200,243,3,31,43,167,232,221,236,233,235,247,242,230,248,192,124,216,123,156,218,242,229,243,246,233,231,229,238,234,0,0,0,160,222,214,242,242,244,239,241,238,246,204,209,255,225,195,220,231,223,222,223,222,226,213,210,207,0,77,180,197,238,217,157,214,236,225,229,228,222,236,224,220,222,225,222,216,219,212,220,214,208,237,241,126,0,151,238,223,225,252,255,255,255,255,255,255,255,255,246,255,255,255,255,254,255,245,255,255,246,174,130,115,0,0,11,42,60,94,101,104,101,102,110,75,14,0,7,16,9,10,11,9,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"label":"Bag","prediction":8})
if __name__ == '__main__':
    unittest.main()