from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from accounts.forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import get_user_model
from django.http import HttpRequest


User=get_user_model()

class UpdateProfileTest(TestCase):
    def setUp(self):
        self.url = reverse('update_user_profile')
        self.template_name='accounts/updateprofile.html'
        self.username = 'testuser'
        self.email='testuser@app.com'
        self.password='testpassword'

        User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

    def test_profile_update_page_exists(self):
        self.client.login(username=self.username,password=self.password)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,self.template_name)

        profile_form= response.context.get('profile_form',None)
        user_form= response.context.get('user_form',None)

        self.assertIsInstance(profile_form,ProfileUpdateForm)
        self.assertIsInstance(user_form,UserUpdateForm)


    def test_profile_and_user_update_forms_update_users(self):
        
        request = HttpRequest()

        request.user = User.objects.get(id=1)

        request.POST={
            'bio':'sample bio text',
            'address':'123 django avenue',
            'first_name':"updated",
            'last_name':'user',
            'username':'testuser'
        }

        profile_form = ProfileUpdateForm(instance=request.user.profile,data={
            'bio':request.POST.get('bio',None),
            'address':request.POST.get('address',None)
        })
        user_form = UserUpdateForm(instance=request.user,data={
            'first_name':request.POST.get('first_name',None),
            'last_name':request.POST.get('last_name',None),
            'username':request.POST.get('username',None),
        })

        self.assertTrue(profile_form.is_valid())
        self.assertTrue(user_form.is_valid())

        profile_form.save()
        user_form.save()

        self.assertEqual(request.user.username,request.POST.get('username',None))
        self.assertEqual(request.user.profile.bio,request.POST.get('bio',None))
