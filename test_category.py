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
        with pytest.raises(ValueError, match="name cannot be longer than 255"):
            Category("a" * 256)
    
    def test_category_name_cannot_be_created_empty(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")

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

        assert output == f"{category.name} - {category.description} ({category.is_active})"

    def test_category_when_repr_is_calling(self):
        category = Category(name="Filme")

        output = repr(category)
        print("teste repr ", output)

        assert output == f"<Category {category.name} ({category.id})>"


class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="Filme", description="Filmes em geral")

        category.update_category(name="Série", description="Séries em geral")

        assert category.name == "Série"
        assert category.description == "Séries em geral"

    def test_update_category_with_invalid_name_raises_exception(self):
        category = Category(name="Filme", description="Filmes em geral")

        with pytest.raises(ValueError, match="name cannot be longer than 255"):
            category.update_category(name="a" * 256, description="Séries em geral")

    def test_update_category_name_with_empty_name_raises_exception(self):
        category = Category(name="Filme", description="Filmes em geral")

        with pytest.raises(ValueError, match="name cannot be empty"):
            category.update_category(name="", description="Séries em geral")

class TestActivate:
    def test_activate_inactive_category(self):
        category = Category(name="Filme", description="Filmes em geral", is_active=False)

        category.activate()

        assert category.is_active is True

    def test_activate_active_category(self):
        category = Category(name="Filme", description="Fiomes em geral", is_active=True)

        category.activate()

        assert category.is_active is True

    def test_deactivate_active_category(self):
        category = Category(name="Filme", description="Fiomes em geral", is_active=True)

        category.deactivate()

        assert category.is_active is False

class TestEquality:
    def test_when_categories_have_same_id_they_are_equal(self):
        id = uuid.uuid4()

        category_1 = Category(id=id, name="Filme")
        category_2 = Category(id=id, name="Filme")

        assert category_1 == category_2
    
    def test_equality_different_classes(self):
        class Dummy:
            pass

        id = uuid.uuid4()
        category = Category(id=id, name="Filme")

        dummy = Dummy()
        dummy.id = id

        assert category != dummy