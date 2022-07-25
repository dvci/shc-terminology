import json
import re
import requests

URL = 'https://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/cvx.txt'

def retrieve_new_cvx(URL):
    '''
    use requests.get to retrieve latest flat file from CDC
    saves the file as newest_cvx_file for posterity and returns file for reading
    '''
    # retrieve flat file data
    cvx_from_cdc = requests.get(URL)
    
    # extract content and write to a file
    open('latest_cdc_file.txt', 'wb').write(cvx_from_cdc.content)

    # open file to read for processing
    return open('latest_cdc_file.txt', 'r')


def retrieve_old_cvx():
    '''
    retrieves saved updated cvx file from same folder for comparison
    returns most up-to-date dictionary of codes
    '''
    with open ('.github/workflows/cvx_updated.json') as json_file:
        data_dict = json.load(json_file)

    return data_dict


def parse_cvx_file(cvx_file):
    '''
    takes a CVX flat file and converts it to a nested dictionary
    dictionary key is the CVX code
    '''
    lines = cvx_file.readlines()
    cvx_dict = {}
    for line in lines:
        sub_dict = {}
        split_list = line.split('|')
        cvx_dict[split_list[0].strip()] = sub_dict
        sub_dict['short-description'] = split_list[1]
        sub_dict['full-vaccine-name'] = split_list[2]
        sub_dict['vaccine-status'] = split_list[4]
        sub_dict['last-update-date'] = split_list[5]
        sub_dict['notes'] = split_list[6]
    return cvx_dict

def find_diffs(old_cvx, new_cvx):

    old_set = set(old_cvx)
    new_set = set(new_cvx)

    difference = new_set - old_set

    if len(difference) == 0:
        return None
    else:
        return difference


def update_cvx(old_cvx, new_cvx):
    '''
    compares the old and new cvx files 
    updates information for matching keys in the old file
    retains old codes and adds new one's
    '''
    old_cvx.update(new_cvx)
    with open('updated_cvx.txt', 'w') as file:
        file.write(json.dumps(old_cvx))
    return old_cvx


def main():

    new_cvx_file = retrieve_new_cvx(URL)

    old = retrieve_old_cvx()
    new = parse_cvx_file(new_cvx_file)

    if find_diffs(old, new) != None:

        update_cvx(old, new)

    # save the updated file for reuse in next update
    with open('.github/workflows/cvx_updated.json','w') as outfile:
            json.dump(old, outfile, indent=4)

if __name__=="__main__":
    main()