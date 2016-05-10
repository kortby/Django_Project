import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import Author, Book

class AuthorFactory(factory.django.DjangoModelFactory):
	"""
	Creating an author
	"""
	class Meta:
		model = Author

	name = factory.Faker('name')

class UserFactory(factory.django.DjangoModelFactory):
	"""Create standard Users"""
	class Meta:
		model = User

	first_name = factory.Faker('first_name')
	last_name = factory.Faker('last_name')
	username = first_name
	password = make_password('test')
		
class BookFactory(factory.django.DjangoModelFactory):
	"""
	Create a book without a review
	"""
	class Meta:
		model = Book

	title = factory.Faker('word')

	@factory.post_generation
	def authors(self, create, extracted, **kwargs):
		if not create:
			return
		if extracted:
			for authors in extracted:
				self.authors.add(authors)

class ReviewFactory(BookFactory):
	"""creates a book with review"""
	
	review = factory.Faker('text', max_nb_chars=400)
	date_reviewed = now()
	reviewed_by = factory.SubFactory(UserFactory)


		