import ast
import json

from playwright.sync_api import APIRequestContext, expect

endpoint = 'character'


def test_get_data_about_character(gh_context: APIRequestContext) -> None:
    c_response = gh_context.get(endpoint)
    expect(c_response).to_be_ok()
    data = str(c_response.json())
    json_string = json.dumps(ast.literal_eval(data))
    jsonFile = open("../api-testing/data-from-playwright-test.json", "w")
    jsonFile.write(json_string)
    jsonFile.close()
