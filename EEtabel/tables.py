import django_tables2 as tables
from .models import Summoners
import itertools

class PersonTable(tables.Table):

    row_number = tables.Column(empty_values=(), verbose_name= 'Koht')
    Summoner_name = tables.Column(verbose_name= 'Nimi' )
    League = tables.Column(verbose_name= 'Liiga' )
    League_points = tables.Column(verbose_name= 'Punktid' )
    TotalLP = tables.Column(verbose_name= 'Liigapunktid kokku' )

    def __init__(self, *args, **kwargs):
        super(PersonTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return '%d' % next(self.counter)

    class Meta:
        #orderable = False
        model = Summoners
        fields = ('row_number', 'Summoner_name', 'League', 'Division', 'League_points', 'TotalLP')


