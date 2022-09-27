def test_basic_web_page_example(base_class):
    base_class.basic_web_page_example.check_main_page()
    base_class.basic_web_page_example.check_basic_page()
    base_class.basic_web_page_example.return_to_main_page()


def test_element_attributes_examples(base_class):
    base_class.element_attributes_examples.navigate_to_attr_page()
    origin_title = base_class.element_attributes_examples.get_original_title()
    assert origin_title == 'This used to be the title'
    title = base_class.element_attributes_examples.get_title()
    assert title == 'a paragraph to test attributes on'
    custom_attr = base_class.element_attributes_examples.get_custom_attrib()
    assert custom_attr == 'attrib in source at load'

    nexid = base_class.element_attributes_examples.get_nextid_attr()
    base_class.element_attributes_examples.click_add_attribute_button()
    newid = base_class.element_attributes_examples.get_nextid_attr()
    assert nexid < newid


def test_table_test_page(base_class):
    base_class.table_test_page.navigate_table_page()
    amount = base_class.table_test_page.get_table_row_amount()
    assert amount != 0
    print(base_class.table_test_page.get_values())
    assert 'Douglas' in base_class.table_test_page.get_values()


def test_dynamic_test_table_test_page(base_class):
    base_class.dynamic_table_test_page.navigate_to_dynamic_table_page()
    base_class.dynamic_table_test_page.add_value_in_a_row()
    print(base_class.dynamic_table_test_page.get_value_in_table())
    assert 'John' in base_class.dynamic_table_test_page.get_value_in_table()

