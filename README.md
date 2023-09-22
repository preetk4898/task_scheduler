See task_runner.pdf for detailed specs for the project. 

To run: 

python task_runner.py path_to_json_file.json

Input Requirements: 
1. Input must be in JSON format as desribed in the specs: 
    {
        "A": {"start": true, "edges": {"B": 5, "C": 7}},
        "B": {"edges": {}},
        "C": {"edges": {}}
    }
2. There must be at least one JSON entry that specifies the starting task.
3. Tasks with dependences can not require the re-execution. i.e. If Task A must be completed before Task B then Task B can not have Task A as a dependent task. 
4. All tasks with dependents must have weights for each edge. 

Test cases included: 
1. test_1.json: This test case does not have any tasks that need to be executed/printed at the same time. 
    Expected Output: 
        A 
        D
        C
        B
        E
        F
        G
2. test_2.json: This test case is an incorrectly formatted JSON. 
    Expected Output: 
        JSON file is invalid. Please check input. Error: 'description of error'
3. test_3.json: This test case is a JSON input of a Directed Cyclic Graph. 
    Expected Output: 
        Task runner can not execute a list of tasks that have circular dependencies.
4. test_4.json: This test case exhibits Tasks that need to be printed at the exact same time.
    Expected Output: BCD and FG: will be printed at about the same time but on new lines
        A 
        B 
        C
        D
        E
        F
        G

The algorithm that I used as inspiration for this project was Kahn's Algorithm (Topoligical Sort with BFS). If this algorithm is applied naively -- without taking into consideration the weights of the edges in the input DAG -- there could be numerous outcomes. The most challenging portion of this coding challenge was the use of the weights and properly sorting them. I was unable to truly capture the request in the challenge (where vertices are processed in parallel). I have some ideas on the parallelization of the tasks to be executed, and they include multiple threading and async functions, however I am not too familiar with these methods in Python so they would have to be explored during a longer time-line for a project like this. 




