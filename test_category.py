import pytest
import unittest
import uuid # std lib - ja vem instalada com o python

from category import Category
from uuid import UUID

class TestCategory:

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            Category("a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active is True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        new_id = uuid.uuid4()
        category = Category(
            id=new_id,
            name="Filme",
            description="Filmes em geral",
            is_active=False
        )
        assert category.id == new_id
        assert category.name == "Filme"
        assert category.description == "Filmes em geral"
        assert category.is_active is False

    def test_category_when_str_is_calling(self):
        category = Category(name="Filme", description="Filmes em geral", is_active=True)
        output = str(category)
        print("teste str ", output)
        # self.assertEquals(output, f"{category.name} - {category.description} ({category.is_active})")

    def test_category_when_repr_is_calling(self):
        category = Category(name="Filme")
        output = repr(category)
        print("teste repr ", output)
        # self.assertEquals(output, f"<Category {category.name} ({category.id})>")

if __name__ == "__main__":
    unittest.main()