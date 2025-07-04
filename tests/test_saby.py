import pytest
import allure

@allure.epic("Тесты сайта Saby")
@allure.feature("Основные сценарии тех. задания")
class TestSaby:

    @allure.story("Первый сценарий")
    @allure.severity(allure.severity_level.NORMAL)
    def test_first_scenario(self, page_saby):
        with allure.step("Переход в раздел контактов"):
            page_saby.go_to_contact_offices()
        with allure.step("Клик по логотипу Tensor"):
            page_saby.click_logo_tensor()
        with allure.step("Проверка видимости заголовка 'Сила в людях'"):
            page_saby.expect_visible_title_power_is_in_people()
        with allure.step("Клик по описанию блока 'Сила в людях'"):
            page_saby.click_on_detail_block_power_is_in_people()
        with allure.step("Проверка размеров фотографий в хронологии работы"):
            page_saby.check_size_photo_chronology_working()

    @allure.story("Второй сценарий")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('region', ['Камчатский край'], ids=lambda reg: f"Регион: {reg}")
    def test_second_scenario(self, page_saby, region):
        with allure.step("Переход в раздел контактов"):
            page_saby.go_to_contact_offices()
        with allure.step("Проверка текущего региона"):
            page_saby.check_region()
        with allure.step("Проверка партнёров в регионе"):
            page_saby.check_partners_region()
        with allure.step("Открытие списка всех регионов"):
            page_saby.open_all_regions()
        test_region = region
        with allure.step(f"Выбор региона {test_region}"):
            page_saby.selected_region(test_region)
        with allure.step(f"Проверка региона {test_region}"):
            page_saby.check_region(test_region)
        with allure.step(f"Проверка имён партнёров в регионе {test_region}"):
            page_saby.check_name_partners(test_region)
        with allure.step(f"Проверка городов партнёров в регионе {test_region}"):
            page_saby.check_cities_partners(test_region)

    @allure.story("Третий сценарий")
    @allure.severity(allure.severity_level.NORMAL)
    def test_third_scenario(self, download_page):
        with allure.step("Открытие страницы загрузки локальных версий продукта"):
            download_page.open_page_download_local_app()
        with allure.step("Загрузка веб-установщика и проверка размера скаченного файла"):
            download_page.download_web_installer_in_test_dir()