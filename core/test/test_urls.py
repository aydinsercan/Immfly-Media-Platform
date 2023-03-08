
from django.test import TestCase

class TestUrls(TestCase):

    def test_channels_list_status_code(self):
        response = self.client.get('/channels/')
        self.assertEquals(response.status_code,200)
    
    def test_channels_status_code(self):
        response = self.client.get('/channels/', {'channel_id':'2'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'base.html','channels.html')
    
    def test_content_status_code(self):
        response = self.client.get('/channels/',{'channel_id':'1'}, '/content')
        self.assertEquals(response.status_code,200)


      



    

    