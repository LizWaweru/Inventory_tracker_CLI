from db.tools import Session
from db.category import Category

class CategoryMenu:
    def __init__(self):
        self.session = Session()

    def add_category(self, name, description):
        category = Category(name = name, description = description)

        try:
            self.session.add(category)
            self.session.commit()
            print("Category added successfully.")
            return category
        except Exception as e:
            self.session.rollback()
            print(f"Error adding category: {str(e)}")
            return None
        
    def find_category_by_id(self, id):
        category = self.session.query(Category).get(id)
        return category
    
    def get_all_category(self):
        categories = self.session.query(Category)
        return [category for category in categories]
    
    def update_category (self, id, name,description):
        category = self.find_category_by_id(id)
        if category:
            try:
                category.name = name
                category.description = description
                self.session.commit()
                print("Category updated successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error updating category: {str(e)}")

    def delete_category(self, id):
        category = self.find_category_by_id(id)
        if category:
            try:
                self.session.delete(category)
                self.session.commit()
                print("Category deleted successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error deleting category: {str(e)}")

    
    def close_session(self):
        self.session.close()


    
