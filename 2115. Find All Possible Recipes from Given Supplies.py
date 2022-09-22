import copy


class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        output = []
        recipe_set = set()
        recipe_memo = {}
        supply_set = set()
        r_to_i = {}
        for i in range(len(recipes)):
            recipe_set.add(recipes[i])
            r_to_i.update({recipes[i]: set(ingredients[i])})

        for supply in supplies:
            supply_set.add(supply)

        for i in range(len(recipes)):
            if self.checkRecipe(recipes[i], recipe_set, ingredients, supply_set, r_to_i, recipe_memo):
                output.append(recipes[i])

        return output

    def checkRecipe(self, recipe, recipe_set, ingredients, supply_set, r_to_i, memo, path_set=set()):
        if recipe in memo:
            return memo.get(recipe)

        if recipe in path_set:
            memo[recipe] = False
            return False

        path_copy = copy.copy(path_set)
        path_copy.add(recipe)

        if recipe in supply_set:
            memo[recipe] = True
            return True

        elif recipe in recipe_set:
            ing_list = r_to_i.get(recipe)
            for ing in ing_list:
                if not self.checkRecipe(ing, recipe_set, ingredients, supply_set, r_to_i, memo, path_copy):
                    memo[recipe] = False
                    return False

            memo[recipe] = True
            return True

        memo[recipe] = False
        return False
