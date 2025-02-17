from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_search():
    browser.open('/')
    s('.header-search-button').should(be.visible).click()

    s("#query-builder-test").should(be.visible).send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").should(be.visible).submit()
    s(by.link_text("eroshenkoam/allure-example")).should(be.visible).click()
    s("#issues-tab").should(be.visible).click()
    s(by.partial_text("Another test issue")).should(be.present)