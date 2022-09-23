from django.test import TestCase, Client


def test_open_homepage_should_be_success(self):  # expected success
    c = Client()
    response = c.get("http://127.0.0.1:8000/")
    assert "Hello world!" in str(response.content)
    assert response.status_code == 200


def test_post_homepage_should_return_405(self):  # expected fail
    c = Client()
    response = c.post("http://127.0.0.1:8000/")
    assert response.status_code == 405, f"{response.status_code} should be 405"