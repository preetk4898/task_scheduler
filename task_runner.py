'''
Preet Kaur 

Task Runner 
Bighat Biosciences Take-Home Assignment

How to run:
'''

import json



class TaskRunner:
    def __init__(self, updated_dag, root):
        self.dag = updated_dag
        self.num_vertices = len(updated_dag.keys())
        self.start = root


def change_empty_edges(dag_dict):
    '''
    Change empty edge values to None type. This will make it easier down the line when I populate the adjacency list for the graph.
    '''
    if isinstance(dag_dict, dict):  # check if DAG passed in is of type "dict"
        for key in dag_dict:
            if dag_dict[key] == {}:
                # after iterating through the keys and checking if the values are empty, change them to None type
                dag_dict[key] = None
            else:
                # recursively iterate through each dictionary -- since there is a nested dict in the inital DAG file
                change_empty_edges(dag_dict[key])

    return dag_dict

def make_adjacency_list(dag_dict):
    '''
    Remove the start key/value pair from the dictionary of edges and vertices to have a final adjacency list to be used in the graph.
    '''
    root = '' #store the start vertex

    for key in dag_dict:
        if len(dag_dict[key]) == 2: #iterate through the dictionary and find a key that has more then key in it's nested dictionary -- we can assume that all other vertices will only have an "edges" key
            root = key
            dag_dict[key].pop('start', None) #remove the start key/value pair so now the start node can behave the same as all downstream 

    return dag_dict, root


def main():
    file_path = input("Enter path to JSON file or file name:")
    with open(file_path, "r") as dag_file:
        dag_dict = json.loads(dag_file.read())

    updated_dag, root = change_empty_edges(dag_dict)
    adj_list, root = make_adjacency_list(updated_dag)


if __name__ == "__main__":
    main()
