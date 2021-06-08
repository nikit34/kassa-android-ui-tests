import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.PlacesPage import PlacesPage
from locators.common_locators import CommonLocators
from locators.places_locators import PlacesPageLocators


# @pytest.mark.usefixtures('driver')
# class TestPlacesPage:
#     def test_tab_places_is_selected(self, driver):
#         '''таб МЕСТА подсвечивается выбранным'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*CommonLocators.tab_places)
#         self.places_page = PlacesPage(driver)
#         self.places_page.set_custom_wait(10)
#         self.places_page.find_element(*PlacesPageLocators.input)
#         self.places_page.find_element(*PlacesPageLocators.events_carousel)
#         self.places_page.find_element(*PlacesPageLocators.event_img)
#         self.places_page.find_element(*PlacesPageLocators.option_name)

