def test_basic_web_page_example(basic_web_page_example):
    basic_web_page_example.check_main_page()
    basic_web_page_example.check_basic_page()
    basic_web_page_example.return_to_main_page()


def test_element_attributes_examples(element_attributes_examples):
    element_attributes_examples.navigate_to_attr_page()
    origin_title = element_attributes_examples.get_original_title()
    assert origin_title == 'This used to be the title'
    title = element_attributes_examples.get_title()
    assert title == 'a paragraph to test attributes on'
    custom_attr = element_attributes_examples.get_custom_attrib()
    assert custom_attr == 'attrib in source at load'

    nexid = element_attributes_examples.get_nextid_attr()
    element_attributes_examples.click_add_attribute_button()
    newid = element_attributes_examples.get_nextid_attr()
    assert nexid < newid


def test_table_test_page(table_test_page):
    table_test_page.navigate_table_page()
    amount = table_test_page.get_table_row_amount()
    assert amount != 0

