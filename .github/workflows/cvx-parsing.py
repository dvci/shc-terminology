import json

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
    old_cvx_file = open('cvx_0.txt','r')
    new_cvx_file = open('cvx_1.txt','r')
    old = parse_cvx_file(old_cvx_file)
    new = parse_cvx_file(new_cvx_file)
    update_cvx(old, new)

if __name__=="__main__":
    main()