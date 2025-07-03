# 1) Перейти на https://saby.ru в раздел "Контакты"
# 2) Проверить, что определился ваш регион (в нашем примере
# Ярославская обл.) и есть список партнеров.
# 3) Изменить регион на Камчатский край
# 4) Проверить, что подставился выбранный регион, список партнеров
# изменился, url и title содержат информацию выбранного региона
import time


class TestSaby:

    def test_first_scenario(self, page_saby):
        page_saby.go_to_contact_offices()
        page_saby.click_logo_tensor()
        page_saby.expect_visible_title_power_is_in_people()
        page_saby.click_on_detail_block_power_is_in_people()
        page_saby.check_size_photo_chronology_working()

    def test_second_scenario(self, page_saby):
        page_saby.go_to_contact_offices()
        page_saby.check_region()
        page_saby.check_partners_region()
        page_saby.open_all_regions()
        test_region = "Камчатский край"
        page_saby.selected_region(test_region)
        page_saby.check_new_region_and_partners()
        time.sleep(3)