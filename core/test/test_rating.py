from core.models import *
from django.core import management
from django.test import TestCase
import io

class TestCSV(TestCase):
    def setUp(self):
        print("setUp method called")
        #Channels
        TvShows = Channel.objects.create(title='TV Shows',language='TR',picture='channels/im1.png')
        Games = Channel.objects.create(title='Games',language='TR',picture='channels/games_JEZwDcJ.png')
        Music = Channel.objects.create(title='Music',language='EN',picture='channels/music.jpg')
        Multiplayer = Channel.objects.create(title='Multiplayer',language='EN',picture='channels/Multiplayer_4B98qeb.jpg',parent_channel=Games)
        Singleplayer = Channel.objects.create(title='Single player',language='EN',picture='channels/images.jpeg',parent_channel=Games)
        Rockmusic = Channel.objects.create(title='Rock Music',language='TR',picture='channels/rock.png',parent_channel=Music)
        Popmusic = Channel.objects.create(title='Pop Music',language='TR',picture='channels/pop.png',parent_channel=Music)
        #Contents
        cont1 = Content.objects.create(title='Vikings', metadata='{"Author": "EL Sercan","Duration": "26","Year": "2011"}',channel=TvShows , text='description', rating = 6)
        cont1.save()
        cont1 = Content.objects.create(title='Peaky Blinders', metadata='{"Author": "Steven Knight","Duration": "40","Year": "2017"}',channel=TvShows , text='description', rating = 9)
        cont1.save()
        cont1 = Content.objects.create(title='Cyberpunk 2077', metadata='{"Producer": "Adam Badowski","Release": "2020","Genre": "Action"}',channel=Singleplayer , text='description', rating = 5)
        cont1.save()
        cont1 = Content.objects.create(title='Final Fantasy 7', metadata='{"Producer": "Firato Ldowski","Release": "2010","Genre": "Action"}',channel=Multiplayer , text='description', rating = 4)
        cont1.save()
        cont1 = Content.objects.create(title='Bu son olsun', metadata='{"Singer": "Cem Karaca","Release": "2001"}',channel=Rockmusic , text='description', rating = 3)
        cont1.save()
        cont1 = Content.objects.create(title='Yolla', metadata='{"Singer": "Tarkan","Release": "2001"}',channel=Popmusic , text='description', rating = 8)
        cont1.save()

    def test_rating_algorithm(self):
        """
        Python supports file like objects, that don't write to the disk but stay in the memory.
        """
        inmemoryfile  = io.StringIO()
        management.call_command("exportCSV", stdout=inmemoryfile)

        self.assertIn("Pop Music: 8.0",inmemoryfile.getvalue())
        self.assertIn("TV Shows: 7.5",inmemoryfile.getvalue())
        self.assertIn("Music: 5.5",inmemoryfile.getvalue())
        self.assertIn("Single player: 5.0",inmemoryfile.getvalue())
        self.assertIn("Games: 4.5",inmemoryfile.getvalue())
        self.assertIn("Multiplayer: 4.0",inmemoryfile.getvalue())
        self.assertIn("Rock Music: 3.0",inmemoryfile.getvalue())

        inmemoryfile.close()
    
    def tearDown(self):    
        print('tearDown method called')

