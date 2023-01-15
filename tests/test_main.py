import requests

api_url = 'http://localhost:8000'

def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200

class testShops():
    def test_get_blank_shops():
        response = requests.get(f'{api_url}/v1/shops')
        assert response.status_code == 200
        assert len(response.json()) == 0
    
    def test_add_shops():
        body = {"name": "ShopName", "location": "City", "productnum": 5 }
        response = requests.post(f'{api_url}/v1/shops', json = body)
        assert response.status_code == 200
        assert response.json().get('name') == 'ShopName'
        assert response.json().get('location') == 'City'
        assert response.json().get('productnum') == 5
        assert response.json().get('id') == 0

    def test_get_shop_id():
        response = requests.post(f'{api_url}/v1/shops/0')
        assert response.status_code == 200
        assert response.json().get('name') == 'ShopName'
        assert response.json().get('location') == 'City'
        assert response.json().get('productnum') == 5
        assert response.json().get('id') == 0

    def test_get_shops():
        response = requests.get(f'{api_url}/v1/shops')
        assert response.status_code == 200
        assert len(response.json()) == 1
    

