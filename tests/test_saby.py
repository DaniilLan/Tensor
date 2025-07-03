# 1) Перейти на https://saby.ru в раздел "Контакты" (Ещё <> офисов в регионе).
# 2) Найти баннер Тензор, кликнуть по нему
# 3) Перейти на https://tensor.ru/
# 4) Проверить, что есть блок "Сила в людях"
# 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
# https://tensor.ru/about
# 6) Находим раздел Работаем и проверяем, что у всех фотографии
# хронологии одинаковые высота (height) и ширина (width)


class TestSaby:

    def test_first_scenarios(self, page_saby):
        page_saby.go_to_contact_offices()
        page_saby.click_logo_tensor()
        page_saby.expect_visible_title_power_is_in_people()
        page_saby.click_on_detail_block_power_is_in_people()
        page_saby.check_size_photo_chronology_working()