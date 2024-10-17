class Recipe():
    def __init__(self, id, title, average_cooking_time, rating):
        self.id = id
        self.title = title
        self.average_cooking_time = average_cooking_time
        self.rating = rating
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.title}, {self.average_cooking_time} minutes, {self.rating} stars)"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__