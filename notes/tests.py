from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm  # Ensure NoteForm is imported from your forms.py


class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title='Test Sticky Note',
            content='This is the content of the sticky note.'
        )

    def test_note_has_title(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, 'Test Sticky Note')

    def test_note_has_content(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.content, 'This is the content of the sticky note.')

    def test_str_representation(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(str(note), 'Test Sticky Note')


class NoteFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'title': 'Form Test Note',
            'content': 'Testing form validation with valid data.'
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_title(self):
        form_data = {
            'title': '',  # Required field left blank
            'content': 'Content without a title.'
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title='View Test Note',
            content='Testing view responses.'
        )

    # --- List View Tests ---
    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Note')

    def test_note_list_view_empty(self):
        Note.objects.all().delete()
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    # --- Detail View Tests ---
    def test_note_detail_view_success(self):
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Note')
        self.assertContains(response, 'Testing view responses.')

    def test_note_detail_view_404_missing(self):
        response = self.client.get(reverse('note_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    # --- Create View Tests ---
    def test_note_create_view_post_success(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'Created via Test',
            'content': 'Newly created content.'
        })
        self.assertEqual(response.status_code, 302)  # Expect redirect after creation
        self.assertTrue(Note.objects.filter(title='Created via Test').exists())

    def test_note_create_view_post_invalid(self):
        response = self.client.post(reverse('note_create'), {
            'title': '',  # Blank title to trigger invalid form
            'content': 'Missing title'
        })
        self.assertEqual(response.status_code, 200)  # Should remain on form page with error
        self.assertFormError(response, 'form', 'title', 'This field is required.')

    # --- Update View Tests ---
    def test_note_update_view_post_success(self):
        response = self.client.post(reverse('note_update', args=[self.note.id]), {
            'title': 'Updated Title',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')
        self.assertEqual(self.note.content, 'Updated Content')

    def test_note_update_view_404_missing(self):
        response = self.client.post(reverse('note_update', args=[9999]), {
            'title': 'Updated Title',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 404)

    # --- Delete View Tests ---
    def test_note_delete_view_post_success(self):
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())

    def test_note_delete_view_404_missing(self):
        response = self.client.post(reverse('note_delete', args=[9999]))
        self.assertEqual(response.status_code, 404)