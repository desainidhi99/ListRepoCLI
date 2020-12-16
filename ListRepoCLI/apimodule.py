import  requests, json, time, traceback
import pandas as pd
from .popularity import sort_data_key
from operator import itemgetter



GIT_API_URL_Repos = "https://api.github.com/repos/"
GIT_API_URL_Organization = 'https://api.github.com/orgs/'
USER = 'desainidhi99'
API_TOKEN = 'bbb8b1d43c6c3320762744217910809c550d9c79'


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' 'application/vnd.github.mercy-preview+json',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

def get_api(organizationName, noOfRecords):
    
    try:
            
        requestUrl = GIT_API_URL_Organization + organizationName + '/' + 'repos'
        jsonData = getResponse(requestUrl)
        print(jsonData)
        
        results = []
        
        for item in jsonData:
        
            forks_count = item['forks_count']
            star_count = item['stargazers_count']
            full_name = item['full_name']
            name_repository = item['name']
                                    
            requestevent = GIT_API_URL_Repos + full_name + '/pulls'           
            jsonEventData = getResponse(requestevent)
            
            pr_count = 0
            contribution_Percentage = 0
            pr_count = (len(jsonEventData))
            contribution_Percentage = round(((pr_count/forks_count) * 100),3)

                       
            data = {
            
               'name' : name_repository, 
               'forks_count' : forks_count,
               'stargazers_count' : star_count,
               'no_pullrequests' : pr_count,
               'contribution_percentage' : contribution_Percentage                 
            
            }
            
            results.append(data)
            
        with open('result_info.json', 'w') as f:
            json.dump(results,f,indent=2)
            
        
        
        s_fork = sort_data_key('forks_count',noOfRecords)
        
        s_star = sort_data_key('stargazers_count',noOfRecords)
        
        s_pr = sort_data_key('no_pullrequests',noOfRecords)
        
        s_contri_percentage = sort_data_key('contribution_percentage',noOfRecords)
        
    
    except:
        print ('failed to get api')
        traceback.print_exc() 
        
    
def getResponse(requestUrl) :
      
        morePagesAvailable = True
        currentPage = 0
        data= []
                
        '''
        /*Request gives back only first 30 records , Uncomment these code (and comment out 'morepages' code) for fewer API requests*/
        
        response = requests.get(requestUrl+'?page{0}'.format(str(currentPage)), auth=(USER, {API_TOKEN}), headers = hdr)
            
        result = response.json()
        data +=result

        '''
        while morePagesAvailable :

            requestUrlforpage = (requestUrl+'?page{0}'.format(str(currentPage)))
            response = requests.get(requestUrl+'?page{0}'.format(str(currentPage)), auth=(USER, {API_TOKEN}), headers = hdr)
            currentPage = currentPage+1
            result = response.json()

            if response.links.get('next') == None:
                morePagesAvailable = False
                       
            data+= result
        
        return data


       

   