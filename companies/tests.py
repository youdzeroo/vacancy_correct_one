from django.test import TestCase, Client


class TestCreateCompany(TestCase):
    def test_should_allow_only_post(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/companies/")
        assert response.status_code == 405
        response = c.put("http://127.0.0.1:8000/companies/")
        assert response.status_code == 405
        response = c.delete("http://127.0.0.1:8000/companies/")
        assert response.status_code == 405
        response = c.patch("http://127.0.0.1:8000/companies/")
        assert response.status_code == 405


