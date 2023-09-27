from django.test import TestCase, Client
dummy_user_login = {
    'username': 'Budi',
    'password': 'Haha1234567890',
  }

dummy_user_register = {
    'username': 'Budi',
    'password1': 'Haha1234567890',
    'password2': 'Haha1234567890',
  }
class RegisterTest(TestCase):
  def test_register_url_is_exist(self):
    response = Client().get('/register/')
    self.assertEqual(response.status_code, 200)

  def test_register_using_register_template(self):
    response = Client().get('/register/')
    self.assertTemplateUsed(response, 'register.html')

  def test_register_success(self):
    response = Client().post('/register/',dummy_user_register)
    self.assertEqual(response.status_code, 302) # got redirected

  def test_register_failed(self):
    response = Client().post('/register/', {})
    self.assertEqual(response.status_code, 200)

class LoginTest(TestCase):
  def setUp(self):
    Client().post('/register/', dummy_user_register)

  def test_login_url_is_exist(self):
    response = Client().get('/login/')
    self.assertEqual(response.status_code, 200)

  def test_login_using_login_template(self):
    response = Client().get('/login/')
    self.assertTemplateUsed(response, 'login.html')

  def test_login_success(self):
    response = Client().post('/login/', dummy_user_login)
    self.assertEqual(response.status_code, 302) # got redirected

  def test_login_failed(self):
    response = Client().post('/login/', {})
    self.assertEqual(response.status_code, 200)

# create test cases for logout
class LogoutTest(TestCase):
  def setUp(self):
    response = Client().post('/login/', dummy_user_login)

  def test_logout_success(self):
    response = Client().get('/logout/')
    self.assertEqual(response.status_code, 302) # got redirected