from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish The Test!')

        # The user is able to enter a new item directly

        # The user types "Buy a real dinosaur fossil"

        # When the user presses "enter" they see the new todo item saved
        # 1: "Buy a real dinosaur fossil"

        # The user can still add items, and enters "Take over the world"

        # The page now shows both items

        # The url for the site has a unique identifier and an explanation as to
        # what it is for, this list!

        # The user uses the unique URL and sees the list


if __name__ == '__main__':
    unittest.main()
