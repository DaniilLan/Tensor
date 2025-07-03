import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from core.utils.data_generators import get_region


class Locators:
    CONTACTS_OFFICES = (By.XPATH, '//ul[@class="sbisru-Header__menu ws-flexbox ws-align-items-center"]//div[text()="Контакты"]')
    LINK_ALL_OFFICES = (By.XPATH, '//div[@class="sbisru-Header-ContactsMenu__items sbisru-Header-ContactsMenu__items-visible"]//a[@href="/contacts"]')
    LOGO_TENSOR = (By.XPATH, '//div[@class="sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm pl-20 pv-12 pl-xm-0 mt-xm-12"]//img[@alt="Разработчик системы Saby — компания «Тензор»"]')
    TITLE_POWER_IS_IN_PEOPLE = (By.XPATH, '//p[text()="Сила в людях"]')
    LINK_DETAIL_POWER_IS_IN_PEOPLE = (By.XPATH, '//div[@class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"]//a')
    TITLE_SECTION_WORKING = (By.XPATH, '//h2[text()="Работаем"]')
    PHOTO_IN_SECTION_WORKING = (By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')
    LINK_REGION_HEADER = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    LIST_BRANCHES_PARTNERS = (By.XPATH, '//div[@class="sbisru-Contacts-List__col-1"]')
    QUANTITY_BRANCHES = (By.XPATH, '//div[@class="sbisru-Contacts-City__item-count sbisru-Contacts__text--md ws-flex-shrink-0"]')
    WINDOW_ALL_REGIONS = (By.XPATH, '//div[@name="dialog"]')

class SabyPage(BasePage):

    def go_to_contact_offices(self):
        self.click(Locators.CONTACTS_OFFICES)
        self.click(Locators.LINK_ALL_OFFICES)

    def click_logo_tensor(self):
        self.click(Locators.LOGO_TENSOR)
        self.switch_focus_last_tab()

    def expect_visible_title_power_is_in_people(self):
        self.expect_visible_element(Locators.TITLE_POWER_IS_IN_PEOPLE)

    def click_on_detail_block_power_is_in_people(self):
        self.click(Locators.LINK_DETAIL_POWER_IS_IN_PEOPLE)
        assert self.get_url() == 'https://tensor.ru/about'

    def check_size_photo_chronology_working(self):
        self.scroll_to_element(Locators.TITLE_SECTION_WORKING)
        self.check_images_equal_size(Locators.PHOTO_IN_SECTION_WORKING)

    def check_region(self):
        region_on_page = self.get_text(Locators.LINK_REGION_HEADER)
        region_current = get_region()
        assert region_on_page == region_current, (f'Текущий регион не соответствует сайту.\n'
                                                  f'На сайт: {region_on_page}\n'
                                                  f'Текущий: {region_current}')

    def check_partners_region(self):
        sum_region = 0
        for quantity_element in self.driver.find_elements(*Locators.QUANTITY_BRANCHES):
            quantity_text = quantity_element.text
            try:
                quantity_in_region = int(quantity_text)
                sum_region += quantity_in_region
            except ValueError:
                print(f"Не удалось преобразовать '{quantity_text}' в число")
        len_list = self.quantity_elements(Locators.LIST_BRANCHES_PARTNERS)
        assert len_list == sum_region, (f'Количество филиалов не соответствует количеству в списке.\n'
                                                  f'Сумма: {sum_region}\n'
                                                  f'Сумма в списке: {len_list}')

    def open_all_regions(self):
        self.click(Locators.LINK_REGION_HEADER)
        self.expect_visible_element(Locators.WINDOW_ALL_REGIONS)

    def selected_region(self, region: str):
        time.sleep(0.5) # Увы так и не смог локализовать проблему с кликом по региону из списка:(
        self.click((By.XPATH, f'//span[@title="{region}"]/span'))

    # Для первого и второго кейса
    # def check_data_by_region(self):
    # Нужен dict с данными по региону и с него сверять информацию по текущему региону страницы







