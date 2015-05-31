from django.core.management.base import BaseCommand, CommandError
from apps.polls.models import Poll

class Command(BaseCommand):
    help = 'Mudando o status das votações'

    def handle(self, *args, **options):
        
        now = datetime.date.today()
        ranking_polls = Poll.objects.filter(ranking_date=now)
        close_polls = Poll.objects.filter(final_date=now)        

        for poll in ranking_polls:
            poll.status = 'ranqueamento'
            poll.save()
        
        for poll in close_polls:
            poll.status = 'fechada'
            poll.save()

        self.stdout.write('O status das votações foram alterados')