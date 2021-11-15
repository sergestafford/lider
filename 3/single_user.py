import requests
from unittest import TestCase, main
 
class TestEndpoint(TestCase):
    def test_get(self):
        response = requests.get('https://reqres.in/api/single_user')
        self.assertEqual(200, response.status_code, "Code is not 200!")
        response_name = response.json()
        self.assertIn("first_name", response_name, "Key first_name not found!")
        self.assertEqual(response_name["first_name"], "Janet", "Key first_name not equal Janet")
        print(response.text)
 
if __name__ == '__main__':
    main()







