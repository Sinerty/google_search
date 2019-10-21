from components.navigation_bar import NavigationBar
from components.search_results import SearchResults


class SearchPage:

    search_results = SearchResults()
    navigation_bar = NavigationBar()

    def search_domain_in_pages(self, domain_name, number_of_pages):
        for page in range(1, number_of_pages):
            self.navigation_bar.navigate_to_page(page)
            if domain_name in self.search_results.domains():
                return True
            else:
                return False