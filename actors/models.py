from django.db import models

NATIONALITY_CHOICES = (
    ('US', 'Estados Unidos'), # ('value', 'display') o value é o que será salvo no banco de dados e o display é o que será exibido no formulário
    ('UK', 'Reino Unido'),
    ('FR', 'França'),
    ('DE', 'Alemanha'),
    ('IT', 'Itália'),
    ('JP', 'Japão'),
    ('KR', 'Coreia do Sul'),
    ('CN', 'China'),
    ('RU', 'Russia'),
    ('IN', 'India'),
    ('BR', 'Brasil'),
    ('AU', 'Australia'),
    ('CA', 'Canada'),
    ('MX', 'Mexico'),
    ('ES', 'Espanha'),
    ('AR', 'Argentina'),
    ('CO', 'Colombia'),
    ('PE', 'Peru'),
    ('CL', 'Chile'),
    ('VE', 'Venezuela'),
    ('EC', 'Equador'),
    ('BO', 'Bolivia'),
    ('PY', 'Paraguay'),
    ('UY', 'Uruguay'),
    ('CR', 'Costa Rica'),
    ('PA', 'Panama'),
    ('CU', 'Cuba'),
    ('DO', 'Dominican Republic'),
    ('GT', 'Guatemala'),
    ('HN', 'Honduras'),
    ('SV', 'El Salvador'),
    ('NI', 'Nicaragua'),
    ('PR', 'Puerto Rico'),
    ('JM', 'Jamaica'),
    ('BS', 'Bahamas'),
    ('HT', 'Haiti'),
    ('BB', 'Barbados'),
    ('TT', 'Trinidad and Tobago'),
    ('AG', 'Antigua and Barbuda'),
    ('DM', 'Dominica'),
    ('VC', 'Saint Vincent and the Grenadines'),
    ('GD', 'Grenada'),
    ('KN', 'Saint Kitts and Nevis'),
    ('LC', 'Saint Lucia'),
    ('SR', 'Suriname'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, null=True, blank=True)
    biography = models.TextField(max_length= 300, null=True, blank=True)

    def __str__(self):
        return self.name