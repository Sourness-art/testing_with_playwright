def test_basic_web_page_example(t_base):
    t_base.basic_web_page_example.check_main_page()
    t_base.basic_web_page_example.check_basic_page()
    t_base.basic_web_page_example.return_to_main_page()


def test_element_attributes_examples(t_base):
    t_base.element_attributes_examples.navigate_to_attr_page()
    origin_title = t_base.element_attributes_examples.get_original_title()
    assert origin_title == 'This used to be the title'
    title = t_base.element_attributes_examples.get_title()
    assert title == 'a paragraph to test attributes on'
    custom_attr = t_base.element_attributes_examples.get_custom_attrib()
    assert custom_attr == 'attrib in source at load'

    nexid = t_base.element_attributes_examples.get_nextid_attr()
    t_base.element_attributes_examples.click_add_attribute_button()
    newid = t_base.element_attributes_examples.get_nextid_attr()
    assert nexid < newid


def test_table_test_page(t_base):
    t_base.table_test_page.navigate_table_page()
    amount = t_base.table_test_page.get_table_row_amount()
    assert amount != 0
    print(t_base.table_test_page.get_values())
    assert 'Douglas' in t_base.table_test_page.get_values()


def test_dynamic_test_table_test_page(t_base):
    t_base.dynamic_table_test_page.navigate_to_dynamic_table_page()
    t_base.dynamic_table_test_page.add_value_in_a_row()
    print(t_base.dynamic_table_test_page.get_value_in_table())
    assert 'John' in t_base.dynamic_table_test_page.get_value_in_table()

