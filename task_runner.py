'''
Preet Kaur 

Task Runner 
Bighat Biosciences Take-Home Assignment

How to run:
'''

import json
from collections import defaultdict

def change_empty_edges(dag_dict):
    '''
    Chance empty edge values to None type. This will make it easier down the line when I populate the adjacency list for the graph.
    '''
    if isinstance(dag_dict, dict): #check if DAG passed in is of type "dict"
        for key in dag_dict: 
            if dag_dict[key] == {}:
                dag_dict[key] = None    #after iterating through the keys and checking if the values are empty, change them to None type
            else:
                change_empty_edges(dag_dict[key]) #recursively iterate through each dictionary -- since there is a nested dict in the inital DAG file

    return dag_dict

def main() :
    file_path = input("Enter path to JSON file or file name:")
    with open(file_path, "r") as dag_file: 
        dag_dict = json.loads(dag_file.read())

    updated_dag = change_empty_edges(dag_dict)
    

if __name__ == "__main__":
    main()