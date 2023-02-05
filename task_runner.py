'''
Preet Kaur 

Task Runner 
Bighat Biosciences Take-Home Assignment
Pseudocode: 
https://docs.google.com/document/d/1I88jOjG27xrhnC2wE7hiqMaAuDfoqB4tS8WPLgrdMV4/edit?usp=sharing

How to run: 

python task_runner.py 'path to file'
'''
from collections import defaultdict
import json
import sys
import time


class TaskRunner:
    def __init__(self, adj_list, root):
        '''
        Insert comments here
        '''
        self.adj_list = adj_list
        self.num_vertices = len(adj_list.keys())
        self.start = root

    def check_acylic_sort(self):
        ''' 
        Determine whether there are cycles in the DAG using a BFS traversal approach and populate/sort a dictioanary 
        with the nodes and the order and time in which they will be printed. I would consider this pre-processing.
        '''
        num_incoming_vert = defaultdict(int) #create a dictionary to track the number of dependencies of each task 
        visited = defaultdict(bool) #create dictionary to ensure all vertices are visited
        for vertex in self.adj_list.keys():
            num_incoming_vert[vertex] #populate the dict
            visited[vertex]

        for vertex in self.adj_list.keys():
            for inc_edge in self.adj_list[vertex]: #iterate through the dependents of a task
                if inc_edge != None:
                    num_incoming_vert[inc_edge[0]] += 1 #if a dependent shows up in the adjacency, increment it's number of dependencies by 1
                else: 
                    pass

        queue = []
        queue.append(self.start) #build queue and append the start node. 
        time_for_node = defaultdict(int) #record time for each node
        time_for_node[self.start]

        #populate the queue with any other tasks that dont have any dependences 
        for node in num_incoming_vert: 
            if num_incoming_vert[node] == 0 and not self.start:
                queue.append(node)

        #start working through the queue to determine if there are any cycles 

        num_visited = 0 #initialize counter to ensure all vertices are visited 

        while(queue):
            current_node = queue.pop(0) #FIFO approach 

            #if all vertices in queue have been visited and if the vertex doesn't have any dependents, pop it from the queue
            if self.adj_list[current_node] == [None] and num_incoming_vert[current_node] == 0:
                visited[current_node] = True
            elif visited[current_node] == False: #if the vert has dependents, cycle through all of them and update the number of incoming verts by 1 bc they have now been visited
                for vert,weight in self.adj_list[current_node]:
                    for node, in vert: 
                        num_incoming_vert[node[0]] -= 1
                        time_for_node[node[0]] = time_for_node[current_node] + weight #populate the dict with the time a node will be printed
                    if num_incoming_vert[node[0]] == 0: 
                        queue.append(node[0])

                    visited[current_node] = True

        check = len(set(visited.values())) == True

        if check == False: #the number of visited vertices has to be equal to the number of vertices in the task runner for it to be acyclic. 
            return False
        else: 
            sorted_by_time = sorted(time_for_node.items(), key = lambda x:x[1]) #sort the time dict in ASC
            return sorted_by_time

    def run_tasks(self, sorted_tasks):
        ''' 
        Print/Execute the tasks in the described order and time from the input. 
        '''
        start_time = time.time() #Time starts now!! 

        for node in sorted_tasks: 
            if round(time.time() - start_time, 1) >= node[1]: #check if the time elapsed is equal to the time of the given node
                print(node[0])
            elif round(time.time() - start_time, 1) < node[1]: #if the right amount of time has not been elapsed, wait 
                time.sleep(node[1] - round(time.time() - start_time, 1))
                print(node[0])
            else: #if no waiting is required or if the window has been missed, print the node immediately.
                print(node[0])
            


def make_adjacency_list(input_dag):
    '''
    Make a weighted adjacency list with the dict converted from the json input.
    '''
    adj_list = defaultdict(list)
    start_node = ''

    for key in input_dag:
        if len(input_dag[key]) == 2: #with the assumption that there is only one start node specified, the length of that key will be 2
            start_node = key 
        
        if input_dag[key]['edges'] != {}: #for verices that have children/dependent tasks
            for nested_key, nested_value in input_dag[key]['edges'].items():
                adj_list[key].append((nested_key, nested_value)) #add weights and edges of the children in the form of a tuple 
        else: 
            adj_list[key].append(None) #if there are no children, assign the edges NoneType


    return adj_list, start_node


def main():
    path = sys.argv[1]

    with open(path, "r") as dag_file: 
        try: 
            dag_dict = json.loads(dag_file.read()) #make sure the input it properly formated in JSON
            adj_list, root = make_adjacency_list(dag_dict) #make an adjacency list with the input file

            tasks = TaskRunner(adj_list, root)
            checked_sorted_tasks = tasks.check_acylic_sort() #check if graph is acyclic and make sorted list of tasks

            if checked_sorted_tasks == False:
                print("Task runner can not execute a list of tasks that has circular dependencies.")
            else: 
                tasks.run_tasks(checked_sorted_tasks) #print out the tasks in the appropriate order and time differential

        except ValueError as e: 
            print(f"JSON file is invalid. Please check input. Error: {e}")

    

if __name__ == "__main__":
    main()
