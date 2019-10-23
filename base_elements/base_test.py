from driver.driver import Driver


class BaseTest:

    def setup(self):
        self.driver = Driver().get_instance()   # створення інстансу драйверу
        self.driver.maximize_window()           # розгортання вікна для firefox

    def teardown(self):
        Driver().close()    # закриття вкладки
        Driver().quit()     # закриття драйверу та присвоєння змінній значення за замовчуванням
