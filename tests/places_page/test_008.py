import pytest
from locators.places_locators import PlacesPageLocators
from screens.MoviesPage import MoviesPage
from screens.PlacesPage import PlacesPage
from locators.common_locators import CommonLocators


@pytest.mark.usefixtures('driver')
class TestPlacesPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.places_locators = PlacesPageLocators()

    def test_places_tab_are_opened(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.common_locators.tab_places)
        self.places_page = PlacesPage(driver)
        self.places_page.set_custom_wait(20)
        self.places_page.pass_popup()
        self.places_page.find_element(*self.places_locators.place_name)
        self.places_page.find_element(*self.places_locators.place_address)

    def test_close_geo_popup(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.common_locators.tab_places)
        self.places_page = PlacesPage(driver)
        self.places_page.set_custom_wait(20)
        self.places_page.click(*self.places_locators.close_allow_geo_location)
        self.places_page.not_displayed(*self.places_locators.allow_geo_location_button)

    def test_geo_popup_is_available(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.common_locators.tab_places)
        self.places_page = PlacesPage(driver)
        self.places_page.set_custom_wait(20)
        self.places_page.find_element(*self.places_locators.allow_geo_location_button)
        self.places_page.find_element(*self.places_locators.close_allow_geo_location)

    def test_tab_places_is_selected(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.common_locators.tab_places)
        self.places_page = PlacesPage(driver)
        self.places_page.set_custom_wait(20)
        self.places_page.find_element(*self.places_locators.input)
        self.places_page.find_element(*self.places_locators.events_carousel)
        self.places_page.find_element(*self.places_locators.event_img)
        self.places_page.find_element(*self.places_locators.option_name)

    def test_tab_movies_is_selected_by_default(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.common_locators.tab_places)
        self.places_page = PlacesPage(driver)
        self.places_page.set_custom_wait(20)
        self.places_page.check_state_tabs()
