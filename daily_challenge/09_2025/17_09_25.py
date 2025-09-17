"""
https://leetcode.com/problems/design-a-food-rating-system/?envType=daily-question&envId=2025-09-17
"""
from typing import List
import heapq
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.rated_cuisine = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (rating, cuisine)
            self.rated_cuisine[cuisine].append((-rating, food))
        
        for cuisine in self.rated_cuisine:
            heapq.heapify(self.rated_cuisine[cuisine])


    def changeRating(self, food: str, newRating: int) -> None:
        _, curr_cuisine = self.foods[food]
        self.foods[food] = (newRating, curr_cuisine)
        heapq.heappush(self.rated_cuisine[curr_cuisine], (-newRating, food))


    def highestRated(self, cuisine: str) -> str:
        while self.rated_cuisine[cuisine][0][0] != -self.foods[self.rated_cuisine[cuisine][0][1]][0]:
            heapq.heappop(self.rated_cuisine[cuisine])
        return self.rated_cuisine[cuisine][0][1]

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# Unit tests
import unittest
class TestFoodRatings(unittest.TestCase):

    def test_case_1(self):
        foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
        cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
        ratings = [9, 12, 8, 15, 14, 7]
        food_ratings = FoodRatings(foods, cuisines, ratings)
        
        self.assertEqual(food_ratings.highestRated("korean"), "kimchi")
        self.assertEqual(food_ratings.highestRated("japanese"), "ramen")
        
        food_ratings.changeRating("sushi", 16)
        self.assertEqual(food_ratings.highestRated("japanese"), "sushi")
        
        food_ratings.changeRating("ramen", 16)
        self.assertEqual(food_ratings.highestRated("japanese"), "ramen")

    def test_case_2(self):
        foods = ["a", "b", "c", "d"]
        cuisines = ["x", "x", "y", "y"]
        ratings = [1, 2, 3, 4]
        food_ratings = FoodRatings(foods, cuisines, ratings)
        
        self.assertEqual(food_ratings.highestRated("x"), "b")
        self.assertEqual(food_ratings.highestRated("y"), "d")
        
        food_ratings.changeRating("a", 5)
        self.assertEqual(food_ratings.highestRated("x"), "a")
        
        food_ratings.changeRating("d", 6)
        self.assertEqual(food_ratings.highestRated("y"), "d")

if __name__ == "__main__":
    unittest.main()