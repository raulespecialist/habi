from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from api.models import Property

def test_get_request(self):
    client = APIClient()
    response = client.get('/api/v1/properties/')
    result = json.loads(response.content)
    assert response.status_code, status.HTTP_200_OK


def test_get_request_query_params_in_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8080/api/v1/properties/?city=bogota')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        expected = {
            'method': 'GET',
            'query_params': {'city': 'bogota'}
        }
        assert response.status_code, status.HTTP_200_OK