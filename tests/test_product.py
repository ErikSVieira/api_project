from fastapi.testclient import TestClient
from src.main import app
from src.schemas.product_schema import ProductsOutputDTO

client = TestClient(app)


product_input_test = {
    "name": "Name Pytest",
    "type": "Type Pytest",
    "size": 40,
    "mark": "Mark Pytest",
    "model": "Adventure Pytest",
    "qty": 500,
    "buy_price": 199.99,
    "sale_price": 399.99,
}

product_id_test = None


def test_create_product():
    response = client.post("/products/", json=product_input_test)
    global product_id_test
    assert response.status_code == 201

    data = response.json()

    product_id_test = data["id"]
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data
    assert data["ative"] is True

    for key in product_input_test:
        assert data[key] == product_input_test[key]

    product = ProductsOutputDTO(**data)
    assert isinstance(product, ProductsOutputDTO)


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    products = [ProductsOutputDTO(**item) for item in response.json()]
    assert isinstance(products[0], ProductsOutputDTO)


def test_get_product():
    global product_id_test
    assert product_id_test is not None

    response = client.get(f"/products/{product_id_test}")
    assert response.status_code == 200
    data = response.json()

    global product_input_test
    assert data["id"] == str(product_id_test)
    assert data["name"] == product_input_test["name"]
    assert data["type"] == product_input_test["type"]
    assert data["mark"] == product_input_test["mark"]
    assert data["model"] == product_input_test["model"]
    assert isinstance(data["id"], str)

    product = ProductsOutputDTO(**data)
    assert isinstance(product, ProductsOutputDTO)


def test_update_product():
    global product_id_test
    assert product_id_test is not None

    update_payload = {
        "name": "Produto Atualizado",
        "type": "Tenis",
        "size": 40,
        "mark": "Mark Test",
        "model": "Adventure X",
        "qty": 600,
        "buy_price": 210.00,
        "sale_price": 410.00,
    }

    response = client.put(
        f"/products/{product_id_test}",
        json=update_payload,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Produto Atualizado"
    assert data["qty"] == 600
    assert data["buy_price"] == 210.00
    assert data["sale_price"] == 410.00


def test_delete_product():
    global product_id_test
    assert product_id_test is not None

    response = client.delete(
        f"/products/{product_id_test}",
    )
    assert response.status_code == 204

    response_check = client.get(f"/products/{product_id_test}")
    assert response_check.status_code == 200
    data = response_check.json()
    assert data["ative"] is False
