import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.PlacesPage import PlacesPage
from locators.common_locators import CommonLocators
from locators.places_locators import PlacesPageLocators


# @pytest.mark.usefixtures('driver')
# class TestPlacesPage:
#     def test_geo_popup_is_available(self, driver):
#         '''в табе МЕСТА имеется попап о геолокации'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*CommonLocators.tab_places)
#         self.places_page = PlacesPage(driver)
#         self.places_page.set_custom_wait(10)
#         self.places_page.find_element(*PlacesPageLocators.allow_geo_location_button)
#         self.places_page.find_element(*PlacesPageLocators.close_allow_geo_location)
