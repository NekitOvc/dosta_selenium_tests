from baseapp import BasePage
from locators import Locators
from selenium.webdriver.common.by import By


class CategoryMenu(BasePage):
    def category_georgia(self):
        georgia = self.find_element(Locators.category_georgia)
        georgia.click()
        return georgia

    def category_main_dishes(self):
        main_dishes = self.find_element(Locators.category_main_dishes)
        main_dishes.click()
        return main_dishes

    def category_breakfast(self):
        breakfast = self.find_element(Locators.category_breakfast)
        breakfast.click()
        return breakfast

    def category_pizza(self):
        pizza = self.find_element(Locators.category_pizza)
        pizza.click()
        return pizza

    def category_pies(self):
        pies = self.find_element(Locators.category_pies)
        pies.click()
        return pies

    def category_sets_sushi_rolls(self):
        sets_sushi_rolls = self.find_element(Locators.category_sets_sushi_rolls)
        sets_sushi_rolls.click()
        return sets_sushi_rolls

    def category_onigiri(self):
        onigiri = self.find_element(Locators.category_onigiri)
        onigiri.click()
        return onigiri

    def category_combo_sets(self):
        combo_sets = self.find_element(Locators.category_combo_sets)
        combo_sets.click()
        return combo_sets

    def category_burgers(self):
        burgers = self.find_element(Locators.category_burgers)
        burgers.click()
        return burgers

    def category_streetfood(self):
        streetfood = self.find_element(Locators.category_streetfood)
        streetfood.click()
        return streetfood

    def category_snacks(self):
        snacks = self.find_element(Locators.category_snacks)
        snacks.click()
        return snacks

    def category_bowls(self):
        bowls = self.find_element(Locators.category_bowls)
        bowls.click()
        return bowls

    def category_woks(self):
        woks = self.find_element(Locators.category_woks)
        woks.click()
        return woks