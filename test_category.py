import unittest
import uuid # std lib - ja vem instalada com o python

from category import Category
from uuid import UUID

class TestCategory(unittest.TestCase):

    def test_name_is_required(self):
        with self.assertRaises(TypeError):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category("a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        self.assertEquals(type(category.id), UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        self.assertEquals(category.name, "Filme")
        self.assertEquals(category.description, "")
        self.assertEquals(category.is_active, True)

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        self.assertEquals(category.is_active, True)

    def test_category_is_created_with_provided_values(self):
        new_id = uuid.uuid4()
        category = Category(
            id=new_id,
            name="Filme",
            description="Filmes em geral",
            is_active=False
        )
        self.assertEquals(category.id, new_id)
        self.assertEquals(category.name, "Filme")
        self.assertEquals(category.description, "Filmes em geral")
        self.assertEquals(category.is_active, False)

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