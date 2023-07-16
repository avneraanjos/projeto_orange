import time

#Done
def test_CT001_inclusao_usuario(fixture):
  pim=fixture
  pim.employee_name('Maria')
  pim.click_search_button()
  time.sleep(1)

  assert pim.table_size() == 0
  pim.visit(pim._url_pim_add_user)
  pim.add('Maria', 'Jose', 'Silva','9999')
  pim.click_save_button()
  pim.visit(pim._url_pim)
  pim.employee_name('Maria')
  pim.click_search_button()
  time.sleep(1)
  assert pim.table_size() == 1

#Done
def test_CT002_busca_usuario(fixture):
  pim=fixture
  pim.employee_id('9999')
  pim.click_search_button()
  time.sleep(1)
  assert pim.table_size() == 1
  id,name,last_name,contract = pim.get_table_data()
  assert id == '9999'
  assert name == 'Maria Jose'
  assert last_name == 'Silva'

def test_CT003_filtro_usuario(fixture):
  pim=fixture
  pim.filter_employment_status('Full-Time Contract')
  pim.click_search_button()
  id,name,last_name,contract = pim.get_table_data()
  assert contract == 'Full-Time Contract'

def test_CT004_ordena_lista(fixture):
  pim=fixture
  lista = pim.get_table_user_id()
  lista_ordenada = sorted(lista)
  assert lista != lista_ordenada

  pim.order_list_by_id()
  time.sleep(2)
  lista = pim.get_table_user_id()
  lista_ordenada = sorted(lista)
  assert lista == lista_ordenada

#Done
def test_CT005_reset_button(fixture):
  pim=fixture
  init_table_size = pim.table_size()
  pim.employee_id('x') #invalid id to force 'No Records Found'
  pim.click_search_button()
  assert pim.table_size() == 0
  pim.click_reset_button()
  assert pim.table_size() == init_table_size

#Done
def test_CT006_exclusao_usuario(fixture):
  pim=fixture
  pim.employee_id('9999')
  pim.click_search_button()
  time.sleep(3)
  assert pim.table_size() == 1
  pim.delete_employee()
  pim.visit(pim._url_pim)
  pim.employee_id('9999')
  pim.click_search_button()
  time.sleep(3)
  assert pim.table_size() == 0
