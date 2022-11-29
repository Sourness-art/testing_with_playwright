import os

from playwright.sync_api import Page

from Locators.file_downloading_uploading_locators import *


class FileDownloadingUploading:

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_upload_file_page(self):
        self.page.get_by_role("link", name="File Upload Example Page").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/file-upload-test.html")

    def navigate_to_download_file_page(self):
        self.page.get_by_role("link", name="File Downloads").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/download/download.html")

    def open_file_selector(self):
        self.page.locator(FILE_SELECTOR).click()

    def select_file_for_uploading_txt(self):
        self.page.locator(FILE_SELECTOR).set_input_files(os.getcwd() + TXT_FILE_IN_FOLDER)

    def select_file_for_uploading_jpg(self):
        self.page.locator(FILE_SELECTOR).set_input_files(os.getcwd() + JPG_FILE_IN_FOLDER)

    def select_file_type_txt(self):
        self.page.get_by_label(GENERAL_FILE_TYPE).check()

    def select_file_type_jpg(self):
        self.page.get_by_label(IMAGE_FILE_TYPE).check()

    def upload_file(self):
        self.page.locator(UPLOAD_BUTTON).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/uploads/fileprocessor")

    def get_file_name_from_page(self):
        return self.page.locator(UPLOADED_FILE_NAME).inner_text()

    def change_selected_file(self):
        self.page.locator(UPLOAD_ANOTHER_BUTTON).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/file-upload-test.html")

    def download_file(self):
        with self.page.expect_download() as download_info:
            self.page.locator(DOWNLOAD_FILE_BUTTON).click()
        download = download_info.value
        download.save_as(os.getcwd() + DOWNLOAD_FILE_DESTINATION)

    @staticmethod
    def check_file_is_downloaded():
        return os.path.exists(os.getcwd() + DOWNLOAD_FILE_DESTINATION)

    @staticmethod
    def delete_unused_file():
        os.remove(os.getcwd() + FILE_TO_DELETE)

    @staticmethod
    def get_txt_file_name_from_folder():
        return os.path.basename(os.getcwd() + TXT_FILE_IN_FOLDER)

    @staticmethod
    def get_jpg_file_name_from_folder():
        return os.path.basename(os.getcwd() + JPG_FILE_IN_FOLDER)
