from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_todo_item(self, todo_text):
        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(todo_text, [row.text for row in rows])

    def create_todo_item(self, todo_text):
        text_input = self.browser.find_element_by_id('new_item')
        text_input.send_keys(todo_text)
        text_input.send_keys(Keys.ENTER)

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # The page and the browser show the to do text
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # The user is able to enter a new item directly
        text_input = self.browser.find_element_by_id('new_item')
        self.assertEqual(
            text_input.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Create a couple of Todos
        first_todo_text = 'Buy a T-Rex'
        second_todo_text = 'Take over the world'

        self.create_todo_item(first_todo_text)
        self.create_todo_item(second_todo_text)

        self.check_for_todo_item(first_todo_text)
        self.check_for_todo_item(second_todo_text)

        # The page now shows both items

        # The url for the site has a unique identifier and an explanation as to
        # what it is for, this list!

        # The user uses the unique URL and sees the list


if __name__ == '__main__':
    unittest.main()
