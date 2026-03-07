import os
from unittest.mock import patch

from django.test import RequestFactory, SimpleTestCase

from drf_crud.views import health, home


class ProjectRoutesTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_redirects_to_grocery_api_by_default(self):
        request = self.factory.get("/")
        with patch.dict(os.environ, {"FRONTEND_URL": ""}):
            response = home(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/api/grocery/")

    def test_home_redirects_to_frontend_when_configured(self):
        request = self.factory.get("/")
        frontend_url = "https://grocery-bud-frontend.onrender.com"
        with patch.dict(os.environ, {"FRONTEND_URL": frontend_url}):
            response = home(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], frontend_url)

    def test_health_endpoint_returns_ok_payload(self):
        request = self.factory.get("/api/health/")
        response = health(request)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})
