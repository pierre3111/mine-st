from faker import Faker
from .models import Conference

fake = Faker()

def create_dummy_conferences(num=10):
    for _ in range(num):
        name = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
        category = fake.word()
        date = fake.date_between(start_date='today', end_date='+1y')
        venue = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        theme = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)

        Conference.objects.create(name=name, category=category, date=date, venue=venue, theme=theme)
