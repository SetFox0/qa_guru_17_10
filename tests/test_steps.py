import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_steps(open_browser):
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        s('.header-search-button').should(be.visible).click()

        s("#query-builder-test").should(be.visible).send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").should(be.visible).submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).should(be.visible).click()

    with allure.step("Открываем Issues"):
        s("#issues-tab").should(be.visible).click()

    with allure.step("Проверяем наличие Issue с наименованием 'Another test issue'"):
        s(by.partial_text("Another test issue")).should(be.present)
