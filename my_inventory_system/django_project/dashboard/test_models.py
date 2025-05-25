import pytest
from .models import Product
from django.core.exceptions import ValidationError
@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(name="Test Mahsulot", quantity=10)
    assert product.name == "Test Mahsulot"
    assert product.quantity == 10

@pytest.mark.django_db
def test_product_name_cannot_be_blank():
    product = Product(name="", quantity=5)
    with pytest.raises(ValidationError):
        product.full_clean()

@pytest.mark.django_db
def test_product_quantity_cannot_be_negative():
    product = Product(name="Salqin ichimlik", quantity=-3)
    with pytest.raises(ValidationError):
        product.full_clean()
