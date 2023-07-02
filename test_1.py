
class Testlogin:

    def test_login(self, open_login_page):
        login_page = open_login_page
        login_page.login()


class TestsPIM:
    def test_CT001_inclusao_usuario(self, open_pmi_page):
        pmi = open_pmi_page
        pmi.open_PMI()
        pmi.add('Maria', 'José', 'Silva')

    def test_CT002_busca_usuario(self, open_pmi_page):
        pmi = open_pmi_page
        pmi.open_PMI()
        pmi.search('Maria José')
        pmi.validate_search('Maria José')

    def test_CT003_filtro_employment(self, open_pmi_page):
        pmi = open_pmi_page
        pmi.open_PMI()
        pmi.filter_employment_status('Full-Time Contract')