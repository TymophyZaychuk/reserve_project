from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test-user',
            password='correct-password',
        )

    def test_get_renders_login_form(self):
        response = self.client.get('/login/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn('form', response.context)

    def test_invalid_post_renders_login_form(self):
        response = self.client.post('/login/', {
            'username': self.user.username,
            'password': 'wrong-password',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertTrue(response.context['form'].errors)

    def test_valid_post_logs_in_and_redirects_home(self):
        response = self.client.post('/login/', {
            'username': self.user.username,
            'password': 'correct-password',
        })

        self.assertRedirects(response, '/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)


class AccountViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='account-user',
            email='account@example.com',
            password='correct-password',
        )

    def test_guest_is_redirected_to_login_form(self):
        response = self.client.get(reverse('account'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('login'))
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Вхід в акаунт')
        self.assertContains(response, 'name="username"')

    def test_authenticated_user_sees_account_details_and_logout(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('account'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)
        self.assertContains(response, reverse('logout'))

    def test_logout_logs_user_out_and_redirects_to_login(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('login'))
        self.assertNotIn('_auth_user_id', self.client.session)
