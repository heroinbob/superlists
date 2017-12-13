from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

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

        # The user types "Buy a T-Rex"
        text_input.send_keys('Buy a T-Rex')

        # When the user presses "enter" they see the new todo item saved
        # 1: "Buy a T-Rex"
        text_input.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertTrue(
            any(row.text == '1: Buy a T-Rex' for row in rows)
        )

        # The user can still add items, and enters "Take over the world"
        self.fail('Finish The Test!')

        # The page now shows both items

        # The url for the site has a unique identifier and an explanation as to
        # what it is for, this list!

        # The user uses the unique URL and sees the list


if __name__ == '__main__':
    unittest.main()
