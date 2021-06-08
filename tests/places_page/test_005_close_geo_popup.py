import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.PlacesPage import PlacesPage
from locators.common_locators import CommonLocators
from locators.places_locators import PlacesPageLocators


# @pytest.mark.usefixtures('driver')
# class TestPlacesPage:
#     def test_close_geo_popup(self, driver):
#         '''В табе Места закрываем попап о геолокации'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*CommonLocators.tab_places)
#         self.places_page = PlacesPage(driver)
#         self.places_page.set_custom_wait(10)
#         self.places_page.click(*PlacesPageLocators.close_allow_geo_location)
#         self.places_page.not_displayed(*PlacesPageLocators.allow_geo_location_button)