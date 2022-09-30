import time


def test_basic_web_page_example(base_class):
    base_class.basic_web_page_example.check_main_page()
    base_class.basic_web_page_example.navigate_to_basic_page()
    base_class.basic_web_page_example.check_basic_page()
    base_class.basic_web_page_example.return_to_main_page()


def test_element_attributes_examples_get_attr(base_class):
    base_class.element_attributes_examples.navigate_to_attr_page()
    origin_title = base_class.element_attributes_examples.get_original_title()
    assert origin_title == 'This used to be the title'
    title = base_class.element_attributes_examples.get_title()
    assert title == 'a paragraph to test attributes on'
    custom_attr = base_class.element_attributes_examples.get_custom_attrib()
    assert custom_attr == 'attrib in source at load'


def test_element_attributes_examples_add_attr(base_class):
    base_class.element_attributes_examples.navigate_to_attr_page()
    nexid = base_class.element_attributes_examples.get_nextid_attr()
    base_class.element_attributes_examples.click_add_attribute_button()
    newid = base_class.element_attributes_examples.get_nextid_attr()
    assert nexid < newid


def test_table_page(base_class):
    base_class.table_test_page.navigate_table_page()
    amount = base_class.table_test_page.get_table_row_amount()
    assert amount != 0
    assert 'Douglas' in base_class.table_test_page.get_values()


def test_dynamic_table_page_add_new_value(base_class):
    base_class.dynamic_table_test_page.navigate_to_dynamic_table_page()
    base_class.dynamic_table_test_page.open_table_data()
    base_class.dynamic_table_test_page.add_value_in_a_row("[{\"name\" : \"John\", \"age\" : 22}]")
    base_class.dynamic_table_test_page.refresh_table()
    assert 'John' in base_class.dynamic_table_test_page.get_value_in_table()


def test_dynamic_table_page_delete_value(base_class):
    base_class.dynamic_table_test_page.navigate_to_dynamic_table_page()
    base_class.dynamic_table_test_page.open_table_data()
    base_class.dynamic_table_test_page.add_value_in_a_row("[]")
    base_class.dynamic_table_test_page.refresh_table()
    assert '' in base_class.dynamic_table_test_page.get_empty_table()


def test_dynamic_table_page_change_name(base_class):
    base_class.dynamic_table_test_page.navigate_to_dynamic_table_page()
    base_class.dynamic_table_test_page.open_table_data()
    base_class.dynamic_table_test_page.get_table_name()
    before = base_class.dynamic_table_test_page.get_table_name()
    base_class.dynamic_table_test_page.change_table_name()
    base_class.dynamic_table_test_page.refresh_table()
    after = base_class.dynamic_table_test_page.get_table_name()
    assert before != after


def test_dynamic_table_page_change_id(base_class):
    base_class.dynamic_table_test_page.navigate_to_dynamic_table_page()
    base_class.dynamic_table_test_page.open_table_data()
    base_class.dynamic_table_test_page.get_table_id()
    before = base_class.dynamic_table_test_page.get_table_id()
    base_class.dynamic_table_test_page.change_table_id()
    base_class.dynamic_table_test_page.refresh_table()
    after = base_class.dynamic_table_test_page.get_table_id()
    assert before != after


def test_alert_box_page_alert_box(base_class):
    base_class.alert_box_page.navigate_alert_page()
    base_class.alert_box_page.usual_alert_box()


def test_alert_box_page_confirm_box(base_class):
    base_class.alert_box_page.navigate_alert_page()
    base_class.alert_box_page.confirm_alert_box()
    confirm_message = base_class.alert_box_page.get_confirm_result()
    base_class.alert_box_page.dismiss_alert_box()
    dismiss_message = base_class.alert_box_page.get_confirm_result()
    assert confirm_message != dismiss_message


def test_alert_box_page_prompt_box(base_class):
    base_class.alert_box_page.navigate_alert_page()
    base_class.alert_box_page.prompt_alert_box("test text")
    assert 'test text' in base_class.alert_box_page.get_prompt_text()


def test_fake_alert_box(base_class):
    base_class.fake_alert_page.navigate_to_fake_alert_page()
    base_class.fake_alert_page.open_fake_alert_box()
    assert base_class.fake_alert_page.check_alert_box_is_visible() is True
    base_class.fake_alert_page.accept_fake_alert()
    assert base_class.fake_alert_page.check_alert_box_is_visible() is False


def test_fake_accept_modal_box(base_class):
    base_class.fake_alert_page.navigate_to_fake_alert_page()
    base_class.fake_alert_page.open_modal_box()
    assert base_class.fake_alert_page.check_alert_box_is_visible() is True
    base_class.fake_alert_page.accept_modal_box()
    assert base_class.fake_alert_page.check_alert_box_is_visible() is False


def test_fake_exit_modal_box(base_class):
    base_class.fake_alert_page.navigate_to_fake_alert_page()
    base_class.fake_alert_page.open_modal_box()
    assert base_class.fake_alert_page.check_alert_box_is_visible() is True
    base_class.fake_alert_page.exit_modal_box()
    # assert base_class.fake_alert_page.check_alert_box_is_visible() is False
