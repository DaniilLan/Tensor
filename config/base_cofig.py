# Представим, что некоторые данные класса ниже мы получаем из БД
class DataRegion:
    data_region = {
        'Самарская область': {
            "city": ['Самара', 'Тольятти', 'Новокуйбышевск', 'Сызрань'],
            "quantity_partners": {
                'Самара': 13,
                'Тольятти': 3,
                'Новокуйбышевск': 1,
                'Сызрань': 1
            },
            "all_name_partners": [
                'Saby - Самара', 'АБТ Сервисы для бизнеса', 'ООО «ЦИФРОВИЗОР»', 'ООО "ГриСофт"',
                'ООО "Электронная отчетность"', 'Инфосистемы', 'Компания «Актив Плюс»', 'Кластер',
                'Поволжский Региональный Центр Интернет Технологий', 'ИП Прядко Д.С.',
                'ООО "ИНТЕРНЕТ ТЕХНОЛОГИИ-АБФ63"',
                'Абф63, ООО', 'ИТ Цех Партнер', 'Saby - Тольятти', 'МЕГА-АРТ', 'ИП Кацин А.М.', 'КСВ',
                'ИП Кононова Алёна Александровна'
            ],
        },
        'Камчатский край': {
            "city": ['Петропавловск-Камчатский'],
            "quantity_partners": {'Петропавловск-Камчатский': 1},
            "all_name_partners": ['Saby - Камчатка'],
        }
    }
