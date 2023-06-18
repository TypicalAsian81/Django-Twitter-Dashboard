# tweets/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Schedule

class TweetTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='specialpwd'
        )

        self.tweet = Schedule.objects.create(
            body='Nice tweet!',
            user=self.user,
        )

    def test_tweet_string(self):
        tweet = Schedule(body='A sample tweet')
        self.assertEqual(str(tweet), tweet.body)

    def test_tweet_content(self):
        self.assertEqual(f'{self.tweet.user}', 'testuser')
        self.assertEqual(f'{self.tweet.body}', 'Nice tweet!')

    def test_tweet_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice tweet!')
        self.assertTemplateUsed(response, 'home.html')

    def test_tweet_create_view(self):
        response = self.client.post(reverse('schedule_new'), {
            'body': 'New tweet',
            'user': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New tweet')






# # tweets/tests.py
# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from .models import Schedule

# class ScheduleTests(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             email='test@email.com',
#             password='specialpwd'
#         )

#         self.tweet = Schedule.objects.create(
#             body='Nice tweet!',
#             user=self.user,
#         )

#     def test_schedule_string(self):
#         schedule = Schedule(body='A sample tweet')
#         self.assertEqual(str(schedule), schedule.body)

#     def test_schedule_content(self):
#         self.assertEqual(f'{self.tweet.user}', 'testuser')
#         self.assertEqual(f'{self.tweet.body}', 'Nice tweet!')

#     def test_schedule_list_view(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Nice tweet!')
#         self.assertTemplateUsed(response, 'home.html')

#     def test_schedule_create_view(self):
#         response = self.client.post(reverse('schedule_new'), {
#             'body': 'New tweet',
#             'user': self.user,
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New tweet')