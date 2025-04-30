from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Параметры
url = 'https://example.com'
expected_title = 'Example'
expected_redirect_url = 'https://www.iana.org/help/example-domains'
timeout = 10

# Инициализация браузера
driver = webdriver.Chrome()

try:
    # 1. Открытие страницы
    driver.get(url)
    print("Страница открыта:", url)

    # 2. Проверка заголовка страницы
    title = driver.title
    assert expected_title in title, f"Заголовок '{title}' не содержит '{expected_title}'"
    print(f"Заголовок содержит '{expected_title}'")

    # 3. Поиск и клик по ссылке с текстом "More information"
    try:
        link = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "More information")]'))
        )
        print(f"Найден элемент с текстом: '{link.text}'")
        link.click()
        print("Клик по ссылке выполнен")
    except TimeoutException:
        raise RuntimeError("Не найдена ссылка с текстом 'More information'")

    # 4. Проверка URL после перехода
    WebDriverWait(driver, timeout).until(lambda d: d.current_url != url)
    current_url = driver.current_url
    assert current_url == expected_redirect_url, f"Ожидался URL '{expected_redirect_url}', но получен '{current_url}'"
    print(f"Переход на '{expected_redirect_url}' выполнен успешно")

finally:
    # Завершение работы браузера
    driver.quit()
    print("Браузер закрыт")
