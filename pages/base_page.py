from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def expect_visible_element(self, locator: tuple[str, str]):
        """Поиск элемента страницы по локатору."""
        return self.wait.until(
            EC.visibility_of_element_located(locator), message=f"Не удалось найти элемент {locator}"
        )

    def expect_presence_element(self, locator: tuple[str, str]):
        """Поиск элемента в DOM по локатору."""
        return self.wait.until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент {locator}"
        )

    def expect_clickable_element(self, locator: tuple[str, str]):
        """Проверка на кликабельность элемента по локатору"""
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Локатор '{locator}' не стал кликабельным"
        )

    def expect_visible_elements(self, locator: tuple[str, str]):
        """Поиск элемента страницы по локатору"""
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator), message=f"Не удалось найти элемент {locator}"
        )

    def open(self, uri: str):
        """Открыть страницу"""
        self.driver.get(uri)

    def get_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def click(self, locator: tuple[str, str]):
        """Клик по элементу"""
        self.expect_visible_element(locator).click()

    def fill_text(self, locator: tuple[str, str], value: str):
        """Ввод текста в поле"""
        element = self.expect_visible_element(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator: tuple[str, str]):
        """Получить текст элемента"""
        element = self.expect_visible_element(locator)
        return element.text

    def get_text_by_hidden_element(self, locator: tuple[str, str]):
        """Получить текст скрытого элемента"""
        element = self.expect_presence_element(locator)
        return element.get_attribute("textContent")

    def get_text_all_elements(self, locator: tuple[str, str]):
        """Получить список текстов всех элементов, соответствующих локатору"""
        elements = self.expect_visible_elements(locator)
        return [element.text for element in elements if element.text]

    def expect_text(self, locator: tuple[str, str], expected_text: str):
        """Проверка соответствия текста"""
        element = self.expect_visible_element(locator)
        actual_text = element.text
        assert actual_text == expected_text, f"Текст не совпадает.\nОжидалось: '{expected_text}', получено: '{actual_text}'"

    def check_images_equal_size(self, locator: tuple[str, str]):
        """Проверяет, что все изображения по локатору имеют одинаковый размер"""
        images = self.wait.until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Не найдено изображения по локатору {locator}"
        )
        sizes = []
        for img in images:
            width = img.get_attribute("width")
            height = img.get_attribute("height")
            if width is None or height is None:
                width = img.size['width']
                height = img.size['height']

            sizes.append((int(width), int(height)))
        first_size = sizes[0]
        number = 0
        for size in sizes[1:]:
            number += 1
            assert size == first_size, (f"Размеры изображений не совпадают.\n"
                                        f"Первое изображение: {first_size}, текущее {number}: {size}")

    def switch_focus_last_tab(self):
        """Переключение на последнюю открытую вкладку"""
        self.wait.until(lambda d: len(d.window_handles) > 1)
        all_windows = self.driver.window_handles
        new_window = all_windows[-1]
        self.driver.switch_to.window(new_window)

    def scroll_to_element(self, locator: tuple[str, str]):
        """Скроллить страницу к элементу"""
        element = self.expect_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def quantity_elements(self, locator: tuple[str, str]):
        """Получить количество элементов по локатору"""
        return len(self.driver.find_elements(*locator))

    def get_list_elements(self, locator: tuple[str, str]):
        """Получить список из элементов по локатору"""
        return self.driver.find_elements(*locator)
