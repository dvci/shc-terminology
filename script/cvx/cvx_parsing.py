import json
import re
import requests
import os
from collections import OrderedDict


def retrieve_new_cvx():
    '''
    use requests.get to retrieve latest flat file from CDC
    saves the file as newest_cvx_file for posterity and returns file for reading
    '''
    CVX = 'https://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/cvx.txt'

    # retrieve flat file data
    response = requests.get(CVX)

    response.encoding = 'utf-8'

    with open('cvx_cdc.txt', 'w') as outfile:
        outfile.write(response.text)

    with open('cvx_cdc.txt', 'r') as readfile:
        lines = readfile.readlines()
        cvx_dict = {}
        for line in lines:
            sub_dict = {}
            split_list = line.split('|')
            cvx_dict[split_list[0].strip()] = sub_dict
            sub_dict['short-description'] = split_list[1]
            sub_dict['full-vaccine-name'] = split_list[2]
            sub_dict['vaccine-status'] = split_list[4]
            sub_dict['last-update-date'] = split_list[6]
            sub_dict['notes'] = split_list[3]

    # # convert keys to integers for ordering
    # cvx_dict = {int(key): value for key, value in cvx_dict.items()}

    # # reorder dictionary by increasing value of keys
    # cvx_dict = OrderedDict(sorted(cvx_dict.items()))

    return cvx_dict


def retrieve_new_name():
    '''
    use requests.get to retrieve latest trade name flat file from CDC
    saves the file and returns for reading
    '''
    PRODUCT = 'https://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/TRADENAME.txt'

    # retrieve flat file data
    response = requests.get(PRODUCT)
    
    # extract content and write to a file
    with open('name_cdc.txt', 'w') as outfile:
        outfile.write(response.text)

    # open file to read for processing
    with open('name_cdc.txt', 'r') as readfile:
        lines = readfile.readlines()
        name_dict = {}
        for line in lines[1:]:
            sub_dict = {}
            split_list = line.split('|')
            name_dict[split_list[2].strip()] = sub_dict
            sub_dict['prod_name'] = split_list[0]
            sub_dict['Description'] = split_list[1]

    return name_dict


def retrieve_old_cvx():
    '''
    retrieves saved updated cvx file from same folder for comparison
    returns most up-to-date dictionary of codes
    '''
    with open ('cvx_updated.json', 'r', encoding='utf-8') as json_file:
        data_dict = json.load(json_file)

    return data_dict


def find_diffs(old_cvx, new_cvx):

    old_set = set(old_cvx)
    new_set = set(new_cvx)

    difference = new_set - old_set

    if len(difference) == 0:
        return None
    else:
        return difference


def update_cvx(old_cvx, new_cvx, name_dict):
    '''
    compares the old and new cvx files 
    updates information for matching keys in the old file
    retains old codes and adds new one's
    '''
    old_cvx.update(new_cvx)

    for k, v in name_dict.items():
        if k in old_cvx:
            old_cvx[k].update(v)

    with open('updated_cvx.txt', 'w') as file:
        file.write(json.dumps(old_cvx))

    return old_cvx


def covid_dict(updated_dict):
    '''
    filters the updated dictionary to just
    key, value pairs that are COVID-19 vaccines
    returns the filtered COVID-19 dictionary
    '''
    covid_dict = {}
    
    for key, value in updated_dict.items():
        for k, v in value.items():
            if 'COVID-19' in v:
                covid_dict[key] = value

    return covid_dict


def update_value_set(covid_dict, target_dir):
    '''
    update the covid-cvx.json vocab file with all
    COVID-19 vaccines
    '''

    json_valuset = open(target_dir+'/input/vocabulary/covid-cvx.json', 'r')

    vs = json.load(json_valuset)

    # default designation dictionary that is sub-dictionary in 
    # in the vocab file
    designation_dict = [
      {
        "language": "en-US",
        "use": {
          "system": "https://terminology.smarthealth.cards/CodeSystem/designation-use",
          "use": "consumer-friendly"
          },
          "value": ""
          }
    ] 

    # check that all the cvx codes are integers
    for code in vs['compose']['include'][0]['concept']:
        code['code'] = int(code['code'])
    
    # access the list of code dictionaries within value set file
    code_subdict = vs['compose']['include'][0]['concept']
    current_cvx_codes = []

    # make reference list of cvx codes that are already in the vocab file
    for code in code_subdict:
        current_cvx_codes.append(code['code'])

    # iterate through the covid dictionary
    for key, value in covid_dict.items():
        # if the key is already present, pass
        if int(key) in current_cvx_codes:
            pass
        # otherwise, build a new dictionary for the new cvx code in the format of the vocab file
        else:
            one_code = {}
            one_code['code'] = int(key)
            one_code['display'] = value['short-description']
            # it's possible the cvx file won't have a prod_name so if else statement to check if it exists
            if 'prod_name' in value.keys():
                designation_dict[0]['value'] = value['prod_name']
            else:
                designation_dict[0]['value'] = ""
            one_code['designation'] = designation_dict
            vs['compose']['include'][0]['concept'].append(one_code)
    
    # order the list of dictionaries by increasing cvx value 
    ordered_vs = sorted(vs['compose']['include'][0]['concept'], key=lambda d: d['code'])

    # insert sorted value set back into json value set
    vs['compose']['include'][0]['concept'] = ordered_vs

    return vs


def main():

    # retrieve newest CVX file from CDC
    new_cvx = retrieve_new_cvx()

    # retrieve newest Manufacturer name file from CDC
    new_name = retrieve_new_name()

    # retrieve old CVX file from previous run
    old = retrieve_old_cvx()

    # update the CVX dictionary
    updated_dict = update_cvx(old, new_cvx, new_name)

    # save the updated file for reuse in next update
    with open('cvx_updated.json','w') as outfile:
            json.dump(updated_dict, outfile, indent=4)

    covid = covid_dict(updated_dict)

    # get current file path    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # move two levels up in directory to get value set file
    target_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2])

    # update the value set
    updated_vs = update_value_set(covid, target_dir)

    # save the updated file for reuse in next update
    with open(target_dir+'/input/vocabulary/covid-cvx.json','w') as outfile:
            json.dump(updated_vs, outfile, indent=4)


if __name__=="__main__":
    main()