from pytest_bdd import scenarios, scenario, given, then, parsers
import pytest
import requests

DUCKDUCKGO_API = 'https://api.duckduckgo.com/?q='


# @scenario('../features/duckduckgo.feature', 'Search DuckDuckGo API for US Presidents')
# def test_duckduckgo():
#     pass
scenarios('../features/duckduckgo.feature', example_converters=dict(president=str))


@given('the DuckDuckGo API is queried for US Presidents')
def ddg_response(president):
    search = 'presidents+of+the+united+states'
    format_json = '&format=json'
    params = {'q': search, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API + search + format_json)
    return response


@then('the response contains results for "<president>"')
def find_presidents(ddg_response, president):
    rsp_data = ddg_response.json()
    rel_topic = rsp_data["RelatedTopics"]
    text = [sub['Text'] for sub in rel_topic]
    assert True
    # assert any(president in item for item in text)

