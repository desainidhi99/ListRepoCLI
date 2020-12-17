import sys
import argparse
from .apimodule import get_api


def main():

    parser = argparse.ArgumentParser(description ='Sorting the repos of organization by popularity in Github')
    parser.add_argument('organization', type= str,  help='Name of organization')
    parser.add_argument('noOfRecords', type= int,  help='No Of Repositories')
    parser.add_argument('AccessToken', type= str,  help='Personal Access Token')
    args = parser.parse_args()        

    
    get_api(args.organization,args.noOfRecords,args.AccessToken)



if __name__ == '__main__':
    main()