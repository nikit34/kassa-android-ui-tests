import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.PlacesPage import PlacesPage
from locators.common_locators import CommonLocators


# @pytest.mark.usefixtures('driver')
# class TestPlacesPage:
#     def test_tab_movies_is_selected_by_default(self, driver):
#         '''Таб кино выбран по дефолту'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*CommonLocators.tab_places)
#         self.places_page = PlacesPage(driver)
#         self.places_page.set_custom_wait(10)
#         self.places_page.check_state_tabs()
