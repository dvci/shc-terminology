import requests
import secret
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
client_id = secret.CLIENT_ID
client_secret = secret.CLIENT_SECRET
scope = 'icdapi_access'
grant_type = 'client_credentials'


# get the OAUTH2 token

# set data to post
payload = {'client_id': client_id, 
	   	   'client_secret': client_secret, 
           'scope': scope, 
           'grant_type': grant_type}
           
# make request
r = requests.post(token_endpoint, data=payload, verify=False).json()
token = r['access_token']


# access ICD API

uri = 'https://id.who.int/icd/entity/894585096'


# HTTP header fields to set
headers = {'Authorization':  'Bearer '+token, 
           'Accept': 'application/json', 
           'Accept-Language': 'en',
	       'API-Version': 'v2'}
           
# # make request           
# r = requests.get(uri, headers=headers, verify=False)

# r_json = json.loads(r.text)

# print the result
# print (r.text)	
# print(json.dumps(r_json, indent=4))



def call_api(uri):
    '''
    takes uri that calls for COVID-related vaccine
    returns API JSON results with COVID-realted vaccine gorups
    '''
    r = requests.get(uri, headers=headers, verify=False)
    r_json = json.loads(r.text)

    return r_json

def obtain_vax_codes(api_json):
    '''
    takes the top-level list of vaccine types
    returns the child vaccines for the vaccine type
    '''
    vaccine_group_list = api_json['child']
    return vaccine_group_list


def call_vaccines(vaccine_group_list):
    '''
    takes a list list of they types of vaccines
    returns a nested dictionary with the type of vaccine as a key, 
    and the name of the respective vaccines are they values
    '''
    icd_dict = {}    
    vacc_dict = {}
    for vaccine in vaccine_group_list:
        vacc = call_api(vaccine)
        title = vacc['title']['@value']
        # try and except statement for determining if there's child vaccines or not
        try:
            vacc_names = obtain_vax_codes(vacc)
        except KeyError:
            vacc_names = []
        vacc_name_list = []
        vacc_dict = {}
        for name in vacc_names:
            one_vacc = call_api(name)
            vacc_name_list.append(one_vacc['title']['@value'])
        vacc_dict[title] = vacc_name_list
        icd_dict.update(vacc_dict)
    return icd_dict


def main():

    # call API for vaccine groups
    parent_results = call_api(uri)

    # pull child vaccines from vaccine groups
    group_results = obtain_vax_codes(parent_results)

    # iterate through vaccine groups and return all child vaccines for the group
    individ_vaccines = call_vaccines(group_results) 

    # save the updated file for reuse in next update
    with open('icd_updated.json','w') as outfile:
        json.dump(individ_vaccines, outfile, indent=4)

if __name__=="__main__":
    main()