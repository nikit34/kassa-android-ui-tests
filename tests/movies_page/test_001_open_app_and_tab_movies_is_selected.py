import pytest

from screens.FeaturerMoviesPage import MoviesPage
from locators.common_locators import CommonLocators



# @pytest.mark.usefixtures('driver')
# class TestMoviePage:
#     def test_tab_movie_is_selected_when_app_opened(self, driver):
#         '''Вкладка КИНО выбрана при открытии приложения'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         tab_trend = self.movie_page.find_element(*CommonLocators.tab_trend)
#         assert tab_trend.is_selected(), f'invalid state: {tab_trend}'
#         tab_search = self.movie_page.find_element(*CommonLocators.tab_search)
#         assert not tab_search.is_selected(), f'invalid state: {tab_search}'
#         tab_ticket = self.movie_page.find_element(*CommonLocators.tab_ticket)
#         assert not tab_ticket.is_selected(), f'invalid state: {tab_ticket}'
#         tab_places = self.movie_page.find_element(*CommonLocators.tab_places)
#         assert not tab_places.is_selected(), f'invalid state: {tab_places}'
#         tab_profile = self.movie_page.find_element(*CommonLocators.tab_profile)
#         assert not tab_profile.is_selected(), f'invalid state: {tab_profile}'
#
#     def test_check_feature_content(self, driver):
#         '''Каждый фильм в fitcher имеет название/описание + время, тег, цену'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.find_element(*MoviesPageLocators.movies_title)
#         movie_base_canvas = self.movie_page.find_element(*MoviesPageLocators.carousel_rv)
#         movie_base_canvas_row = self.movie_page.find_element(*MoviesPageLocators.list_session_view)
#
#         random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
#         while True:
#             current_check = random_num % 4
#
#             if current_check == 0:
#                 movie_base_canvas.find_element(*MoviesPageLocators.event_name)
#             elif current_check == 1:
#                 movie_base_canvas.find_element(*MoviesPageLocators.place_label)
#             elif current_check == 2:
#                 movie_base_canvas_row.find_element(*MoviesPageLocators.session_date)
#             elif current_check == 3:
#                 movie_base_canvas_row.find_element(*MoviesPageLocators.session_price)
#
#             random_num //= 4
#             if random_num == 0:
#                 break
#             self.movie_page.act.swipe(80, 30, 20, 30)
#
#     def test_fastbuy_button_is_working(self, driver):
#         '''Кнопка быстрой покупки открывает расписание'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*MoviesPageLocators.fastbuy_ticket_id)
#         self.shedule_page = ShedulePage(driver)
#         self.shedule_page.set_custom_wait(15)
#         self.shedule_page.find_element(*ShedulePageLocators.event_name)
#
#     def test_hiding_eventstabs_after_swipe_down(self, driver):
#         '''Проверяем, что event tabs пропадает при свайпе вниз'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(2)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         sleep(1)
#         self.movie_page.not_displayed(*MoviesPageLocators.feature_app_bar)
#         self.movie_page.not_displayed(*MoviesPageLocators.tabs_rv)
#
#     def test_top_movies_are_visible(self, driver):
#         '''Топ фильмы отображаются на главном экране'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.find_element(*MoviesPageLocators.event_img)
#
#     def test_top_movie_is_opened_from_featurer(self, driver):
#         '''Открытия фильма из раздела top'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click_random(*MoviesPageLocators.event_img, 3)
#         self.event_detail_page = EventsDetailsPage(driver)
#         self.event_detail_page.set_custom_wait(15)
#         self.event_detail_page.find_element(*EventsDetailsPageLocators.description)
#
#     def test_hide_and_show_up_headers_tabs(self, driver):
#         '''Event navigation бар пропадает при swipe вниз и появляется при swipe вверх'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 20, 50, 80)
#         sleep(1)
#         self.movie_page.find_element(*MoviesPageLocators.feature_app_bar)
#         self.movie_page.find_element(*MoviesPageLocators.tabs_rv)
#
#     def test_popular_movies_are_visible(self, driver):
#         '''Популярные фильмы видны на экране при запуске'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.movie_page.find_element(*MoviesPageLocators.compilation_img)
#         self.movie_page.find_element(*MoviesPageLocators.favorite_container)
#
#     def test_premiers_are_available(self, driver):
#         '''Премьеры присутствуют на экране'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 55, 50, 45)
#         sleep(1)
#         self.movie_page.matching_text(*MoviesPageLocators.movies_title, pattern='Скоро в кино')
#         self.movie_page.find_element(*MoviesPageLocators.carousel_rv)
#
#     def test_flop_into_popular_movie(self, driver):
#         '''Проваливаемся в карусель популярные фильмы по клику'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.movie_page.click(*MoviesPageLocators.compilation_img)
#         self.movie_page.pass_allow_photo_media()
#         self.movie_page.find_element(*EventsDetailsPageLocators.event_trailer)
#
#     def test_closing_schedule_to_event_detail(self, driver):
#         '''Event details показывается после закрытия расписания кнопкой назад'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*MoviesPageLocators.fastbuy_ticket_id)
#         self.shedule_page = ShedulePage(driver)
#         self.shedule_page.set_custom_wait(10)
#         self.shedule_page.pass_allow_photo_media()
#         self.shedule_page.click(*ShedulePageLocators.back_button)
#         self.event_details_page = EventsDetailsPage(driver)
#         self.event_details_page.set_custom_wait(10)
#         self.event_details_page.find_element(*EventsDetailsPageLocators.description)
#
#     def test_popular_movies_are_visible(self, driver):
#         '''Проваливаемся в карусель популярные фильмы по клику на названия блока'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         sleep(1)
#         self.movie_page.click(*MoviesPageLocators.event_title)
#         self.movie_page.find_element(*EventsDetailsPageLocators.event_trailer)
#
#     def test_popular_movies_are_visible(self, driver):
#         '''Проваливаемся в карусель популярные фильмы по клику на стрелку блока'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(2)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.movie_page.click(*MoviesPageLocators.arrow_right)
#         self.movie_page.find_element(*ShedulePageLocators.event_name)
#
#     def test_popular_movies_are_visible(self, driver):
#         '''Проваливаемся в event details из карусели популярных фильмов'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         sleep(1)
#         self.movie_page.click(*MoviesPageLocators.event_title)
#         self.movie_page.find_element(*EventsDetailsPageLocators.description)
#
#     def test_premiers_are_available(self, driver):
#         '''Проваливаемся в премьеры - горизонтальную карусель'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.movie_page.matching_text(*MoviesPageLocators.movies_title, pattern='Скоро в кино')
#         self.movie_page.click(*MoviesPageLocators.movies_title)
#         self.movie_page.find_element(*MoviesPageLocators.event_name)
#
#     def test_from_premier_into_event_details(self, driver):
#         '''Проваливаемся в эвент детейлз из горизонтальной карусели премьер'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.movie_page.click(*MoviesPageLocators.movies_title)
#         self.movie_page.click(*MoviesPageLocators.event_name)
#         self.events_details_page = EventsDetailsPage(driver)
#         self.movie_page.set_custom_wait(10)
#         self.events_details_page.find_element(*EventsDetailsPageLocators.title)
#
#     def test_premiers_are_available(self, driver):
#         ''' Открываем расписание из горизонтальной карусели премьер через кнопку быстрой оплаты'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.movie_page.click(*MoviesPageLocators.arrow_right)
#         self.schedule_page = ShedulePage(driver)
#         self.schedule_page.set_custom_wait(15)
#         self.schedule_page.click(*ShedulePageLocators.fastbuy_ticket_id)
#         self.schedule_page.find_element(*ShedulePageLocators.session_sheet)
#
#     def test_close_premier_schedule_sheet_from_carousel(self, driver):
#         '''Закрываем расписание из карусели премьер и попадаем на эвент детейлз'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         sleep(5)
#         self.movie_page.act.swipe(50, 80, 50, 20)
#         self.movie_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.movie_page.click(*MoviesPageLocators.arrow_right)
#         self.movie_page.click(*MoviesPageLocators.fastbuy_ticket_id)
#         self.schedule_page = ShedulePage(driver)
#         self.schedule_page.set_custom_wait(15)
#         self.schedule_page.click(*ShedulePageLocators.back_bar_button)
#         self.event_details_page = EventsDetailsPage(driver)
#         self.event_details_page.find_element(*EventsDetailsPageLocators.title)
#
#     def test_close_premier_schedule_sheet_from_carousel(self, driver):
#         '''Выходим кнопкой назад из карусели премьер и попадаем на фичер'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*MoviesPageLocators.event_img)
#         self.event_detail_page = EventsDetailsPage(driver)
#         self.event_detail_page.set_custom_wait(15)
#         self.event_detail_page.pass_allow_photo_media()
#         self.event_detail_page.find_element(*EventsDetailsPageLocators.title)
#         self.event_detail_page.click(*EventsDetailsPageLocators.back_button)
#         self.movie_page.find_element(*MoviesPageLocators.list_session_view)


