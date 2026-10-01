from django.test import TestCase
from django.urls import reverse
from .models import Note  # Replace with your actual model name

class NoteModelTest(TestCase):
    def setUp(self):
        # Create a sample note for testing
        Note.objects.create(
            title='Test Sticky Note',
            content='This is the content of the sticky note.'
        )

    def test_note_has_title(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Sticky Note')

    def test_note_has_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is the content of the sticky note.')

    def test_str_representation(self):
        note = Note.objects.get(id=1)
        self.assertEqual(str(note), 'Test Sticky Note')


class NoteViewTest(TestCase):
    def setUp(self):
        Note.objects.create(
            title='View Test Note',
            content='Testing view responses.'
        )

    def test_note_list_view(self):
        # Replace 'note_list' with your actual URL route name
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Note')

    def test_note_detail_view(self):
        note = Note.objects.get(id=1)
        # Replace 'note_detail' with your actual detail route name
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Note')
        self.assertContains(response, 'Testing view responses.')
        