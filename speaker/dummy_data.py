from faker import Faker
from .models import Speaker

fake = Faker()

def create_dummy_speakers(num=10):
    for _ in range(num):
        name = fake.name()
        bio = fake.paragraph(nb_sentences=3)
        contact_info = fake.email()
        profile_picture = None  # You can add a default profile picture path here if needed
        areas_of_expertise = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)

        Speaker.objects.create(name=name, bio=bio, contact_info=contact_info,
                               profile_picture=profile_picture, areas_of_expertise=areas_of_expertise)
