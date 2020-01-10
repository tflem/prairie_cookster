recipe_list = []


def get_last_id():
    if recipe_list:
        last_recipe = recipe_list[-1]
    else:
        return 1

    return last_recipe.id + 1


class Recipe:
    def __init__(self,
                 name,
                 description,
                 number_of_servings,
                 cooking_time,
                 directions):

        self.id = get_last_id()
        self.name = name
        self.description = description
        self.number_of_servings = number_of_servings
        self.cooking_time = cooking_time
        self.directions = directions
        self.is_published = False

        # Return data as dictionary object
        @property
        def data():
            return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'number_of_servings': self.number_of_servings,
                'cooking_time': self.cooking_time,
                'directions': self.directions
            }

