from django.core.management.base import BaseCommand
import requests
from members. models import competition

class command(BaseCommand):
    help='fetch and store football competitions from API'
    
    def handle(self, *args,**options,):
        url= 'http://api.football-data.org/v4/competitions/'
        headers={'X-AUTH-Token':'YOUR-API-KEY'}
        response=requests.get(url,headers=headers)
        data=response.json()
         
        for competition_data in data['competitions']:
                competition.objects.get_or_create(
                    id=competition_data['id'],
                    name=competition_data['name'],
                    code=competition_data['code'],
                )
                
            
                
                self.stdout.write(self.style.SUCCESS('successfully fetched and stored competitions'))
                
                
        for competition_data in data['competitions']:
                competition.objects.get_or_create(
                    id=competition_data['id'],
                    defaults={
                    'name':competition_data['name'],
                    'code':competition_data['code'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('successfully fetched and stored  football competitions'))
        
        
        
        
                
        
