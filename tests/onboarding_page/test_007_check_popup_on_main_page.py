import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.OnboardingPage import OnboardingPage


#
# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     def test_geo_popup_is_come(self, driver):
#         '''Видим popup после onboarding'''
#         self.onboarding_page = OnboardingPage(driver)
#         self.onboarding_page.set_custom_wait(15)
#         self.onboarding_page.skip_onboarding()
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.check_popup()
#         self.movie_page.pass_popup()
