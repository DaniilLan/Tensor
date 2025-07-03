import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    CONTACTS_OFFICES = (By.XPATH, '//ul[@class="sbisru-Header__menu ws-flexbox ws-align-items-center"]//div[text()="Контакты"]')
    LINK_ALL_OFFICES = (By.XPATH, '//div[@class="sbisru-Header-ContactsMenu__items sbisru-Header-ContactsMenu__items-visible"]//a[@href="/contacts"]')
    LOGO_TENSOR = (By.XPATH, '//div[@class="sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm pl-20 pv-12 pl-xm-0 mt-xm-12"]//img[@alt="Разработчик системы Saby — компания «Тензор»"]')
    TITLE_POWER_IS_IN_PEOPLE = (By.XPATH, '//p[text()="Сила в людях"]')
    LINK_DETAIL_POWER_IS_IN_PEOPLE = (By.XPATH, '//div[@class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"]//a')
    PHOTO_IN_SECTION_WORKING = (By.XPATH, '//div[@class="tensor_ru-About__block3-image-filter"]')


class SabyPage(BasePage):

    def go_to_contact_offices(self):
        self.click(Locators.CONTACTS_OFFICES)
        self.click(Locators.LINK_ALL_OFFICES)

    def click_logo_tensor(self):
        self.click(Locators.LOGO_TENSOR)
        current_window = self.driver.current_window_handle
        self.wait.until(lambda d: len(d.window_handles) > 1)
        all_windows = self.driver.window_handles
        new_window = [window for window in all_windows if window != current_window][0]
        self.driver.switch_to.window(new_window)

    def expect_visible_title_power_is_in_people(self):
        self.expect_visible_element(Locators.TITLE_POWER_IS_IN_PEOPLE)

    def click_on_detail_block_power_is_in_people(self):
        self.click(Locators.LINK_DETAIL_POWER_IS_IN_PEOPLE)
        assert self.get_url() == 'https://tensor.ru/about'

    def check_size_photo_chronology_working(self):
        self.check_images_equal_size(Locators.PHOTO_IN_SECTION_WORKING)


