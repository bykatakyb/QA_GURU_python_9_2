from selene import browser
from selene.support.conditions import be, have


def test_google_search_1_good():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_2_bad():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('12sq1092874jmm;;[qpk').press_enter()
    browser.element('#appbar').should(have.text('Результатов: примерно 0'))


