import pytest
from locators.places_locators import PlacesPageLocators
from screens.FeaturerMoviesPage import MoviesPage
from screens.PlacesPage import PlacesPage
from locators.common_locators import CommonLocators


# @pytest.mark.usefixtures('driver')
# class TestPlacesPage:
#     def test_places_tab_are_opened(self, driver):
#         '''Открыта вкладка Билеты'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*CommonLocators.tab_places)
#         self.places_page = PlacesPage(driver)
#         self.places_page.set_custom_wait(10)
#         self.places_page.pass_popup()
#         self.places_page.find_element(*PlacesPageLocators.place_name)
#         self.places_page.find_element(*PlacesPageLocators.place_address)
