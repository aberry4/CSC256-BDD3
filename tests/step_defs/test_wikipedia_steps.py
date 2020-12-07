import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver


@scenario('../features/wikipedia.feature', 'Search Wikipedia for Wake Tech')
def test_search():
    pass


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


@given("the Wikipedia home page is displayed")
def go_to_wikipedia(driver):
    driver.get('https://en.wikipedia.org/')


@when("the user types in 'wake tech' to the search bar")
def input_search(driver):
    search = driver.find_element_by_id('searchInput')
    search.send_keys('wake tech')
    driver.find_element_by_id('searchButton').click()


@then("the Wake Tech page is displayed")
def get_page(driver):
    title = driver.find_element_by_id('firstHeading').text
    assert title == 'Wake Technical Community College'
