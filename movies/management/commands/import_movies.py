from genres.models import Genre
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from movies.models import Movie
from actors.models import Actor


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com filmes e atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row_number, row in enumerate(reader, start=1):
                    try:
                        actor_name = row['actor_name']
                        birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                        nationality = row['nationality']
                        title = row['title']
                        release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
                        resume = row['resume']
                        genre_name = row['genre']

                        # Criar ou obter o ator
                        actor, created = Actor.objects.get_or_create(
                            name=actor_name,
                            defaults={
                                'birthday': birthday,
                                'nationality': nationality
                            }
                        )
                        if created:
                            self.stdout.write(self.style.NOTICE(f"Linha {row_number}: Ator '{actor_name}' criado com sucesso"))

                        # Criar ou obter o gênero
                        genre, _ = Genre.objects.get_or_create(name=genre_name)

                        # Criar ou obter o filme
                        movie, created = Movie.objects.get_or_create(
                            title=title,
                            defaults={
                                'release_date': release_date,
                                'resume': resume,
                                'genre': genre
                            }
                        )
                        if created:
                            self.stdout.write(self.style.NOTICE(f"Linha {row_number}: Filme '{title}' criado com sucesso"))

                        # Adicionar relação ator-filme
                        movie.actors.add(actor)

                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(f"Linha {row_number}: Coluna ausente no CSV ({e})"))
                        continue
                    except ValueError as e:
                        self.stdout.write(self.style.ERROR(f"Linha {row_number}: Erro de formatação nos dados ({e})"))
                        continue

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Arquivo '{file_name}' não encontrado."))
            return

        self.stdout.write(self.style.SUCCESS('Filmes e atores importados com sucesso!'))
