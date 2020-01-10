from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipe_list


class RecipeListResource(Resource):
    def get_recipes(self):
        data = []

        for recipe in recipe_list:
            if recipe.is_published is True:
                data.append(recipe.data)
        return {'data': data}, HTTPStatus.OK

    def post_recipes(self):
        data = request.get_json()

        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        number_of_servings=data['number_of_servings'],
                        cooking_time=data['cooking_time'],
                        directions=data['directions'])

        recipe_list.append(recipe)
        return recipe.data, HTTPStatus.CREATED
