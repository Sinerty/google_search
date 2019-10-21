from project.base_elements.base_test import BaseTest
from project.pages.main_page import MainPage
from project.pages.search_page import SearchPage


class TestSearchDomain(BaseTest):

    def test_find_domain(self):
        MainPage().search_bar.search_for(search_word="automation")
        result = SearchPage().search_domain_in_pages('testautomationday.com', 5)
        assert result, "Результат пошуку не містить пошукового слова"
