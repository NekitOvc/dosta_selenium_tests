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

    def category_salads(self):
        salads = self.find_element(Locators.category_salads)
        salads.click()
        return salads

    def category_soups(self):
        soups = self.find_element(Locators.category_soups)
        soups.click()
        return soups

    def category_desserts(self):
        desserts = self.find_element(Locators.category_desserts)
        desserts.click()
        return desserts

    def category_drinks(self):
        drinks = self.find_element(Locators.category_drinks)
        drinks.click()
        return drinks

    def category_sauces(self):
        sauces = self.find_element(Locators.category_sauces)
        sauces.click()
        return sauces


class Compilations(BasePage):

    def compilations_new(self):
        new = self.find_element(Locators.compilations_new)
        new.click()
        return new

    def compilations_fastfood(self):
        fastfood = self.find_element(Locators.compilations_fastfood)
        fastfood.click()
        return fastfood

    def compilations_pan_asian(self):
        pan_asian = self.find_element(Locators.compilations_pan_asian)
        pan_asian.click()
        return pan_asian

    def compilations_lunch(self):
        lunch = self.find_element(Locators.compilations_lunch)
        lunch.click()
        return lunch

    def compilations_hearty(self):
        hearty = self.find_element(Locators.compilations_hearty)
        hearty.click()
        return hearty

    def compilations_light(self):
        light = self.find_element(Locators.compilations_light)
        light.click()
        return light

    def compilations_shrimps(self):
        shrimps = self.find_element(Locators.compilations_shrimps)
        shrimps.click()
        return shrimps

    def compilations_salmon(self):
        salmon = self.find_element(Locators.compilations_salmon)
        salmon.click()
        return salmon

    def compilations_vegetarian_menu(self):
        vegetarian_menu = self.find_element(Locators.compilations_vegetarian_menu)
        vegetarian_menu.click()
        return vegetarian_menu

    def compilations_for_kids(self):
        for_kids = self.find_element(Locators.compilations_for_kids)
        for_kids.click()
        return for_kids

    def compilations_sweet(self):
        sweet = self.find_element(Locators.compilations_sweet)
        sweet.click()
        return sweet
