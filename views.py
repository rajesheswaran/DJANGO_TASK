from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from members import competition
from.serializers import competitionserializer

class competitionListView(APIView):
    
    def get(self,request,*args,**kwargs):
        url= 'http://api.football-data.org/v4/competitions/'
        headers={'X-Auth-Token':'YOUR_API-KEK'}
        
        response=requests.get(url,headers=headers)
        data=response.json()
        
        competition=[]
        
        for competition_data in data['competitions']:
            competition={
                'id': competition_data['id'],
                'area': {
                    'id': competition_data['area']['id'],
                    'name': competition_data['area']['name'],
                    
                },
                'currentseason':{
                    'id': competition-data['currentseason']['id'],
                    'startdate':competition_data['currentseason']['startdate'],
                    'enddate':competition_data['currentseason']['enddate'],
                    
                },
                'numberfavailableseason':competition_data['numberofavailableseason'],
            }
            competition.append(competition)
            
            serializer=competitionserializer(competition,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)