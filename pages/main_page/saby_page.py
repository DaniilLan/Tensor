import os
import time

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from core.utils.data_generators import get_region
from config.base_cofig import DataRegion


class Locators:
    CONTACTS_OFFICES = (By.XPATH, '//ul[@class="sbisru-Header__menu ws-flexbox ws-align-items-center"]//div[text()="Контакты"]')
    LINK_ALL_OFFICES = (By.XPATH, '//div[@class="sbisru-Header-ContactsMenu__items sbisru-Header-ContactsMenu__items-visible"]//a[@href="/contacts"]')
    LOGO_TENSOR = (By.XPATH, '//div[@class="sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm pl-20 pv-12 pl-xm-0 mt-xm-12"]//img[@alt="Разработчик системы Saby — компания «Тензор»"]')
    TITLE_POWER_IS_IN_PEOPLE = (By.XPATH, '//p[text()="Сила в людях"]')
    LINK_DETAIL_POWER_IS_IN_PEOPLE = (By.XPATH, '//div[@class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"]//a')
    TITLE_SECTION_WORKING = (By.XPATH, '//h2[text()="Работаем"]')
    PHOTO_IN_SECTION_WORKING = (By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')
    LINK_REGION_HEADER = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    LIST_PARTNERS = (By.XPATH, '//div[@class="sbisru-Contacts-List__col-1"]')
    QUANTITY_PARTNERS = (By.XPATH, '//div[@class="sbisru-Contacts-City__item-count sbisru-Contacts__text--md ws-flex-shrink-0"]')
    WINDOW_ALL_REGIONS = (By.XPATH, '//div[@name="dialog"]')
    CITIES_REGION = (By.XPATH, '//div[contains(@id, "city-id-")]')
    NAME_PARTNERS = (By.XPATH, '//div[@class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32"]')
    LINK_PAGE_DOWNLOAD_LOCAL_APP = (By.XPATH, '//a[text()="Скачать локальные версии"]')
    LINK_DOWNLOAD_WEB_INSTALLER = (By.XPATH, "//h3[text()='Веб-установщик ']/ancestor::div[contains(@class, 'sbis_ru-DownloadNew-block')]//a[contains(@class, 'js-link')]")


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
        fact_url = self.get_url()
        expected = 'https://tensor.ru/about'
        assert fact_url == expected, ('Фактический URL страницы не соответствует ожиданию\n'
                                                                               f'Ожидаемый URL: {expected}\n'
                                                                               f'Фактический: {fact_url}')

    def check_size_photo_chronology_working(self):
        self.scroll_to_element(Locators.TITLE_SECTION_WORKING)
        self.check_images_equal_size(Locators.PHOTO_IN_SECTION_WORKING)

    def check_region(self, region: str = None):
        region_on_page = self.get_text(Locators.LINK_REGION_HEADER)
        if region is not None:
            region_current = region
        else:
            region_current = get_region()
            if region_current not in DataRegion.regions:
                region_current = 'г. Москва'
        assert region_on_page == region_current, (f'Текущий регион не соответствует сайту.\n'
                                                  f'На сайт: {region_on_page}\n'
                                                  f'Текущий: {region_current}')

    def check_partners_region(self):
        sum_region = 0
        region = self.get_text(Locators.LINK_REGION_HEADER)
        if region in ["г. Москва", "г. Санкт-Петербург"]:
            sum_region = int(self.get_text_by_hidden_element(Locators.QUANTITY_PARTNERS))
        else:
            for quantity_element in self.driver.find_elements(*Locators.QUANTITY_PARTNERS):
                quantity_text = quantity_element.text
                quantity_in_region = int(quantity_text)
                sum_region += quantity_in_region
        len_list = self.quantity_elements(Locators.LIST_PARTNERS)
        assert len_list == sum_region, (f'Количество филиалов не соответствует количеству в списке.\n'
                                        f'Сумма: {sum_region}\n'
                                        f'Сумма в списке: {len_list}')

    def open_all_regions(self):
        self.click(Locators.LINK_REGION_HEADER)
        self.expect_visible_element(Locators.WINDOW_ALL_REGIONS)

    def selected_region(self, region: str):
        time.sleep(1)
        self.click((By.XPATH, f'//span[@title="{region}"]/span'))
        self.expect_visible_element((By.XPATH, f'//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/span[text()="{region}"]'))

    # Пример двух проверок для второго сценария проверки
    def check_name_partners(self, region: str):
        dr = DataRegion()
        name_partners = self.get_text_all_elements(Locators.NAME_PARTNERS)
        db_name_partners = dr.data_region[f"{region}"]['all_name_partners']
        assert name_partners == db_name_partners, (f'Данные имен филиалов не соответствуют БД\n'
                                                   f'Сайт: {name_partners}\n'
                                                   f'Бд: {db_name_partners}')

    def check_cities_partners(self, region: str):
        dr = DataRegion()
        name_partners = self.get_text_all_elements(Locators.CITIES_REGION)
        db_name_partners = dr.data_region[f"{region}"]['city']
        assert name_partners == db_name_partners, (f'Данные имен филиалов не соответствуют БД\n'
                                                   f'Сайт: {name_partners}\n'
                                                   f'Бд: {db_name_partners}')

    def open_page_download_local_app(self):
        self.click(Locators.LINK_PAGE_DOWNLOAD_LOCAL_APP)
        assert self.get_url() == 'https://saby.ru/download'

    def download_web_installer_in_test_dir(self):
        link_download = Locators.LINK_DOWNLOAD_WEB_INSTALLER
        self.click(link_download)

        size_text = self.get_text(link_download)
        expected_size_mb = float(size_text.split()[-2])
        download_path = os.path.join(os.getcwd(), "test_downloads")

        max_wait_time = 60
        waited_time = 0
        file_found = False
        downloaded_file = None

        while not file_found and waited_time < max_wait_time:
            time.sleep(1)
            waited_time += 1
            files = os.listdir(download_path)
            for file in files:
                if file.endswith('.exe'):
                    downloaded_file = os.path.join(download_path, file)
                    file_found = True
                    break
        assert file_found, f"Файл не был скачан в течение {max_wait_time} секунд"

        file_size_bytes = os.path.getsize(downloaded_file)
        actual_size_mb = file_size_bytes / (1024 * 1024)
        assert abs(actual_size_mb - expected_size_mb) < 0.1, (f"Размер файла не совпадает.\n"
                                                        f"Ожидалось: {expected_size_mb} МБ\n"
                                                        f"Фактически: {actual_size_mb:.2f} МБ")
        try:
            if downloaded_file and os.path.exists(downloaded_file):
                os.remove(downloaded_file)
                print(f"Файл {downloaded_file} удален")
        except Exception as e:
            print(f"Ошибка при удалении файла {downloaded_file}: {str(e)}")







