import pytest

class TestSaby:

    def test_first_scenario(self, page_saby):
        page_saby.go_to_contact_offices()
        page_saby.click_logo_tensor()
        page_saby.expect_visible_title_power_is_in_people()
        page_saby.click_on_detail_block_power_is_in_people()
        page_saby.check_size_photo_chronology_working()

    @pytest.mark.parametrize('region', ['Камчатский край'])  # И другие возможные регионы
    def test_second_scenario(self, page_saby, region):
        page_saby.go_to_contact_offices()
        page_saby.check_region()
        page_saby.check_partners_region()
        page_saby.open_all_regions()
        test_region = region
        page_saby.selected_region(test_region)
        page_saby.check_region(test_region)
        page_saby.check_name_partners(test_region)
        page_saby.check_cities_partners(test_region)

    # 1) Перейти на https://saby.ru
    # 2) В Footer'e найти и перейти "Скачать локальные версии"
    # 3) Скачать СБИС Плагин для вашей для windows, веб-установщик в
    # папку с данным тестом
    # 4) Убедиться, что плагин скачался
    # 5) Сравнить размер скачанного файла в мегабайтах. Он должен
    # совпадать с указанным на сайте (в примере 3.64 МБ).

    def test_third_scenario(self, download_page):
        download_page.open_page_download_local_app()
        download_page.download_web_installer_in_test_dir()








