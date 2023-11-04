import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_model_creation(self):
        """Test if a BaseModel instance is
        created with the correct attributes."""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_model_update(self):
        """Test if the BaseModel instance updates
        the 'updated_at' attribute upon saving."""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected
        dictionary format."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()

        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['__class__'], "BaseModel")
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json['id'], str)
        self.assertIsInstance(my_model_json['created_at'], str)

    def test_str_representation(self):
        """Test if the __str__ method returns the expected
        string representation."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        expected_str = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)


if __name__ == '__main__':
    unittest.main()
