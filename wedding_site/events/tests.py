from django.test import TestCase
from .models import Event

class EventModelTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(
            name="Test Wedding",
            date="2023-10-10",
            location="Test Venue"
        )

    def test_event_creation(self):
        self.assertEqual(self.event.name, "Test Wedding")
        self.assertEqual(str(self.event.date), "2023-10-10")
        self.assertEqual(self.event.location, "Test Venue")

    def test_event_str(self):
        self.assertEqual(str(self.event), "Test Wedding")  # Assuming __str__ method returns the event name

class EventViewTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(
            name="Test Wedding",
            date="2023-10-10",
            location="Test Venue"
        )

    def test_event_list_view(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Wedding")

    def test_event_detail_view(self):
        response = self.client.get(f'/events/{self.event.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Wedding")

    def test_event_create_view(self):
        response = self.client.post('/events/create/', {
            'name': 'New Wedding',
            'date': '2023-11-11',
            'location': 'New Venue'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Event.objects.filter(name='New Wedding').exists())

    def test_event_update_view(self):
        response = self.client.post(f'/events/{self.event.id}/edit/', {
            'name': 'Updated Wedding',
            'date': '2023-12-12',
            'location': 'Updated Venue'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, 'Updated Wedding')

    def test_event_delete_view(self):
        response = self.client.post(f'/events/{self.event.id}/delete/')
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())