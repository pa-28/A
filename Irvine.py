# Simple Reflex Agent

hand pulling system
"""

class Environment:
    def __init__(self, heat_level='High'):
        self.heat_level = heat_level

    def get_percept(self):
        """Return the heat level of the object as the percept."""
        return 'Hot' if self.heat_level == 'High' else 'Cool'


class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        """Determine action based on the percept (heat level)."""
        if percept == 'Hot':
            return 'Pull hand away, you touched the hot object'
        else:
            return 'You have not touched any hot object , No need to pull away'

def run_agent(agent, environment):
    # The agent reacts to the heat stimulus only once
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept}, Action: {action}")


# Create instances of agent and environment
agent = SimpleReflexAgent()
environment = Environment(heat_level='Low')  # Start with a cool object

# Run the agent in the environment (only once)
run_agent(agent, environment)

"""vaccum cleaner"""

class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        else:
            return 'Room is clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()


# Create instances of agent and environment
agent = SimpleReflexAgent()
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)

"""vaccum cleaner maze"""

class SimpleReflexAgent:
    def __init__(self):
        self.position = 0  # Start at position 0 (top-left corner)
        self.environment_model = ['Clean', 'Dirty', 'Clean',
                                  'Clean', 'Dirty', 'Dirty',
                                  'Clean', 'Clean', 'Clean']  # Initial model of the environment

    def act(self, percept):
        # If the current position is dirty, clean it
        if percept == 'Dirty':
            self.environment_model[self.position] = 'Clean'  # Clean the environment model
            return 'Clean the room'
        else:
            return 'Room is clean'

    def move(self):
        # Move to the next position in the grid
        if self.position < 8:
            self.position += 1
        return self.position

    def update_model(self, position, percept):
        # Update the agent's internal model with the percept
        self.environment_model[position] = percept

    def get_model(self):
        return self.environment_model


class Environment:
    def __init__(self):
        # Create the environment with a 3x3 grid, where 'b', 'e', and 'f' are dirty
        self.grid = ['Clean', 'Dirty', 'Clean',
                     'Clean', 'Dirty', 'Dirty',
                     'Clean', 'Clean', 'Clean']

    def get_percept(self, position):
        # Return the state of the current position
        return self.grid[position]

    def clean_room(self, position):
        # Clean the room at the given position
        self.grid[position] = 'Clean'

    def display_grid(self, agent_position):
        # Display the current state of the grid in a 3x3 format
        print("\nCurrent Grid State:")
        grid_with_agent = self.grid[:]  # Copy the grid
        grid_with_agent[agent_position] = "👽"  # Place the agent at the current position
        for i in range(0, 9, 3):
            print(" | ".join(grid_with_agent[i:i + 3]))
        print()  # Extra line for spacing


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.act(percept)
        print(f"Step {step + 1}: Position {agent.position} -> Percept - {percept}, Action - {action}")

        # Update agent's internal model based on percept
        agent.update_model(agent.position, percept)

        # Display the grid state with agent's position
        environment.display_grid(agent.position)

        if percept == 'Dirty':
            environment.clean_room(agent.position)

        agent.move()


# Create instances of agent and environment
agent = SimpleReflexAgent()
environment = Environment()

# Run the agent in the environment for 9 steps (to cover the 3x3 grid)
run_agent(agent, environment, 9)

"""# Model based agent

vaccum cleaner
"""

class ModelBasedAgent:
    def __init__(self):
        self.model = {} #current : dirty / clean

    def update_model(self, percept):
        self.model['current'] = percept
        print(self.model)


    def predict_action(self):
        if self.model['current'] == 'Dirty':
            return 'Clean the room'
        else:
            return 'Room is clean'

    def act(self, percept):
        self.update_model(percept)
        return self.predict_action()


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()


# Create instances of agent and environment
agent = ModelBasedAgent()
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)

"""closing window"""

class Environment:
    def __init__(self, rain='No', windows_open='Open'):
        self.rain = rain
        self.windows_open = windows_open

    def get_percept(self):
        """Returns the current percept (rain status and window status)."""
        return {'rain': self.rain, 'windows_open': self.windows_open}

    def close_windows(self):
        """Closes the windows if they are open."""
        if self.windows_open == 'Open':
            self.windows_open = 'Closed'


class ModelBasedAgent:
    def __init__(self):
        self.model = {'rain': 'No', 'windows_open': 'Open'}

    def act(self, percept):
        """Decides action based on the model and current percept."""
        # Update the model with the current percept
        self.model.update(percept)

        # Check the model to decide action
        if self.model['rain'] == 'Yes' and self.model['windows_open'] == 'Open':
            return 'Close the windows'
        else:
            return 'No action needed'

def run_agent(agent, environment, steps):
    for step in range(steps):
        # Get the current percept from the environment
        percept = environment.get_percept()

        # Agent makes a decision based on the current percept
        action = agent.act(percept)

        # Print the current percept and the agent's action
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")

        # If the agent decided to close the windows, update the environment
        if action == 'Close the windows':
            environment.close_windows()

# Create instances of agent and environment
agent = ModelBasedAgent()
environment = Environment(rain='Yes', windows_open='Open')  # It's raining and windows are open

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)

"""2d grid vaccum"""

class ModelBasedAgent:
    def __init__(self):
        self.position = 0
        self.environment_model = {}  # Stores perceptions

    def act(self, percept):
        if self.environment_model.get(self.position, percept) == 'Dirty':
            self.environment_model[self.position] = 'Clean'
            return 'Clean the room'
        else:
            return 'Room is clean'

    def move(self):
        if self.position < 8:
            self.position += 1

    def update_model(self, position, percept):
        self.environment_model[position] = percept


class Environment:
    def __init__(self):
        self.grid = ['Clean', 'Dirty', 'Clean',
                     'Clean', 'Dirty', 'Dirty',
                     'Clean', 'Clean', 'Clean']

    def get_percept(self, position):
        return self.grid[position]

    def clean_room(self, position):
        self.grid[position] = 'Clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.act(percept)
        print(f"Step {step + 1}: Position {agent.position}, Percept: {percept}, Action: {action}")

        agent.update_model(agent.position, percept)
        if percept == 'Dirty':
            environment.clean_room(agent.position)

        agent.move()


agent = ModelBasedAgent()
environment = Environment()
run_agent(agent, environment, 9)

"""# Goal Based Agent"""

class GoalBasedAgent:
    def __init__(self):
        self.goal = 'Clean'

    def formulate_goal(self, percept):
        if percept == 'Dirty':
            self.goal = 'Clean'
        else:
            self.goal = 'No action needed'

    def act(self, percept):
        self.formulate_goal(percept)
        if self.goal == 'Clean':
            return 'Clean the room'
        else:
            return 'Room is clean'


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()


# Create instances of agent and environment
agent = GoalBasedAgent()
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)

"""2d grid vaccum"""

class GoalBasedAgent:
    def __init__(self):
        self.position = 0

    def act(self, percept, environment):
        if "Dirty" not in environment.grid:
            return "Goal achieved!"
        if percept == "Dirty":
            return "Clean the room"
        else:
            return "Move to next position"

    def move(self):
        if self.position < 8:
            self.position += 1
        return self.position


class Environment:
    def __init__(self):
        self.grid = ["Clean", "Dirty", "Clean",
                     "Clean", "Dirty", "Dirty",
                     "Clean", "Clean", "Clean"]

    def get_percept(self, position):
        return self.grid[position]

    def clean_room(self, position):
        self.grid[position] = "Clean"

    def display_grid(self, agent_position):
        grid_copy = self.grid[:]
        grid_copy[agent_position] = "👽"
        print("\nGrid State:")
        for i in range(0, 9, 3):
            print(" | ".join(grid_copy[i:i + 3]))
        print()


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.act(percept, environment)
        print(f"Step {step + 1}: Position {agent.position} -> Percept: {percept}, Action: {action}")

        environment.display_grid(agent.position)

        if action == "Clean the room":
            environment.clean_room(agent.position)
        elif action == "Goal achieved!":
            print("Stopping agent: Environment is fully clean.")
            break

        agent.move()


# Run the goal-based agent
agent = GoalBasedAgent()
environment = Environment()
run_agent(agent, environment, 9)

"""# Utility Based Agent

vaccum cleaner
"""

class UtilityBasedAgent:
    def __init__(self):
        self.utility = {'Dirty': -10, 'Clean': 10}

    def calculate_utility(self, percept):
        return self.utility[percept]

    def select_action(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        else:
            return 'No action needed'

    def act(self, percept):
        action = self.select_action(percept)
        return action


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    total_utility = 0
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        utility = agent.calculate_utility(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}, Utility - {utility}")
        total_utility += utility
        if percept == 'Dirty':
            environment.clean_room()
    print("Total Utility:", total_utility)


# Create instances of agent and environment
agent = UtilityBasedAgent()
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)

"""movie selection"""

class Environment:
    def __init__(self, movies=None):
        if movies is None:
            movies = {'Movie A': 8, 'Movie B': 6, 'Movie C': 9}
        self.movies = movies

    def get_percept(self):
        """Returns the list of movies and their review scores."""
        return self.movies


class UtilityBasedAgent:
    def __init__(self, mood_factor=0.7):
        self.mood_factor = mood_factor

    def utility(self, review):
        """Compute utility based on review score and mood factor."""
        return review * self.mood_factor

    def act(self, percept):
        """Decides which movie to watch based on utility."""
        best_movie = None
        best_utility = -float('inf')

        for movie, review in percept.items():
            movie_utility = self.utility(review)
            if movie_utility > best_utility:
                best_movie = movie
                best_utility = movie_utility

        return best_movie

def run_agent(agent, environment):
    percept = environment.get_percept()
    best_choice = agent.act(percept)
    print(f"Available Movies: {percept}")
    print(f"Best Movie to Watch: {best_choice}")


# Create instances of agent and environment
agent = UtilityBasedAgent(mood_factor=0.8)
environment = Environment({'Movie A': 7, 'Movie B': 9, 'Movie C': 5})

# Run the agent in the environment
run_agent(agent, environment)

"""2d grid vaccum"""

class UtilityAgent:
    def __init__(self):
        self.position = 0

    def act(self, percept, environment):
        if "Dirty" not in environment.grid:
            return "All clean! Done."
        if percept == "Dirty":
            return "Clean the room"
        else:
            # Move to the dirtiest remaining location
            next_dirty = [i for i, state in enumerate(environment.grid) if state == "Dirty"]
            if next_dirty:
                self.position = next_dirty[0]
            return "Move to a dirtier location"

    def move(self, new_position):
        self.position = new_position


class Environment:
    def __init__(self):
        self.grid = ["Clean", "Dirty", "Clean",
                     "Clean", "Dirty", "Dirty",
                     "Clean", "Clean", "Clean"]

    def get_percept(self, position):
        return self.grid[position]

    def clean_room(self, position):
        self.grid[position] = "Clean"

    def display_grid(self, agent_position):
        grid_copy = self.grid[:]
        grid_copy[agent_position] = "👽"
        print("\nGrid State:")
        for i in range(0, 9, 3):
            print(" | ".join(grid_copy[i:i + 3]))
        print()


def run_agent(agent, environment):
    while "Dirty" in environment.grid:
        percept = environment.get_percept(agent.position)
        action = agent.act(percept, environment)
        print(f"Position {agent.position} -> Percept: {percept}, Action: {action}")

        environment.display_grid(agent.position)

        if action == "Clean the room":
            environment.clean_room(agent.position)
        elif action == "All clean! Done.":
            print("Stopping agent: Environment is fully clean.")
            break


# Run the utility-based agent
agent = UtilityAgent()
environment = Environment()
run_agent(agent, environment)


"""# BFS

tree
"""

# tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# BFS Function
def bfs(graph, start, goal):
    visited = []  # List for visited nodes   []  ... [A]
    queue = []    # Initialize a queue      [] .... [A]
    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)  # Dequeue
        print(node, end=" ")
        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in graph[node]:    # node='A'
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(tree, start_node, goal_node)

#Same example to check Visited and Frontier(Queue)
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# BFS Function with Visited and Queue Tracking
def bfs(graph, start, goal):
    visited = []  # List for visited nodes
    queue = []    # Initialize a queue

    visited.append(start)
    queue.append(start)

    print(f"Initial Queue: {queue}")

    while queue:
        node = queue.pop(0)  # Dequeue
        print(f"Visited: {visited}")
        print(f"Dequeued: {node}")
        print(f"Queue: {queue}")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

        print(f"Updated Queue: {queue}\n")

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(tree, start_node, goal_node)

"""goal based agent bfs"""

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def bfs_search(self, graph, start, goal):
        visited = []  # List for visited nodes
        queue = []    # Initialize a queue

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)  # Dequeue
            print(f"Visiting: {node}")

            if node == goal:  # Stop if goal is found
                return f"Goal {goal} found!"

            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return "Goal not found"

    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return self.bfs_search(graph, percept, self.goal)


class Environment:
    def __init__(self, graph):
        #Initial graph/tree/maze
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)  # Pass graph to agent
    print(action)


# Tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Create instances of agent and environment
agent = GoalBasedAgent(goal_node)
environment = Environment(tree)

# Run the agent
run_agent(agent, environment, start_node)

"""graph representation"""

# Graph Representation
graph = {
    0: [1, 3],
    1: [0, 3],
    2: [4,5],
    3: [0, 1, 6, 4],
    4: [3, 2, 5],
    5: [4, 2, 6],
    6: [3, 5]
}


# BFS Function
def bfs(graph, start, goal):
    visited = []  # List for visited nodes
    queue = []    # Initialize a queue

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)  # Dequeue
        print(node, end=" ")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Define Start and Goal Nodes
start_node =0
goal_node = 5

# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(graph, start_node, goal_node)

"""maze representation"""

# Maze representation as a graph
maze = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

# Directions for movement (right and down)
directions = [(0, 1), (1, 0)]  # (row, col)

# Convert maze to a graph (adjacency list representation)
def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # If it's an open path
                neighbors = []
                for dx, dy in directions:  #[(0,1) .. dx ] , [(1,0)].... dy
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbors.append((nx, ny))
                graph[(i, j)] = neighbors
    return graph

# BFS Function using queue
def bfs(graph, start, goal):
    visited = []  # List for visited nodes
    queue = []    # Initialize queue

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)  # FIFO: Dequeue from front
        print(node, end=" ")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in graph[node]:  # Visit neighbors
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Create graph from maze
graph = create_graph(maze)

# Define Start and Goal nodes
start_node = (0, 0)  # Starting point (0,0)
goal_node = (2, 2)   # Goal point (2,2)

# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(graph, start_node, goal_node)

"""goal based agent maze path finding"""

from collections import deque

# Maze representation as a graph (1 = open path, 0 = wall)
maze = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

# Directions for movement (right and down)
directions = [(0, 1), (1, 0)]  # (row, col)

# Convert maze to a graph (adjacency list representation)
def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # If it's an open path
                neighbors = []
                for dx, dy in directions:  # [(0,1) right], [(1,0) down]
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbors.append((nx, ny))
                graph[(i, j)] = neighbors
    return graph

# Goal-Based Agent using BFS
def goal_based_agent_bfs(graph, start, goal):
    queue = deque([(start, [start])])  # Queue stores (node, path taken)
    visited = set()

    while queue:
        node, path = queue.popleft()  # FIFO: Dequeue from front
        if node in visited:
            continue

        print(f"Agent at: {node}, Path: {path}")

        if node == goal:  # Goal condition
            print("\n✅ Goal Reached! Path:", path)
            return path  # Return the found path

        visited.add(node)

        for neighbor in graph.get(node, []):  # Visit neighbors
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  # Append new path

    print("\n❌ Goal Not Reachable")
    return None

# Create graph from maze
graph = create_graph(maze)

# Define Start and Goal nodes
start_node = (0, 0)  # Starting point (0,0)
goal_node = (2, 2)   # Goal point (2,2)

# Run BFS with Goal-Based Agent
print("\n🧭 Goal-Based Agent using BFS:")
goal_based_agent_bfs(graph, start_node, goal_node)

"""# DFS

tree representation
"""

# tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}


# DFS Function
def dfs(graph, start, goal):
    visited = []  # List for visited nodes
    stack = []    # Initialize stack

    visited.append(start)
    stack.append(start)

    while stack:
        node = stack.pop()  # LIFO: Pop from top
        print(node, end=" ")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in reversed(graph[node]):  # Reverse to maintain correct order
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Run DFS
print("\nFollowing is the Depth-First Search (DFS):")
dfs(graph, start_node, goal_node)

"""goal based agent dfs"""

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def dfs_search(self, graph, start, goal):
        visited = []  # List for visited nodes
        stack = []    # Initialize stack

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()  # LIFO: Pop from top
            print(f"Visiting: {node}")

            if node == goal:  # Stop if goal is found
                return f"Goal {goal} found!"

            for neighbour in reversed(graph.get(node, [])):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)

        return "Goal not found"

    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return self.dfs_search(graph, percept, self.goal)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)  # Pass graph to agent
    print(action)


# Tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Create instances of agent and environment
agent = GoalBasedAgent(goal_node)
environment = Environment(tree)

# Run the agent
run_agent(agent, environment, start_node)


# Maze representation as a graph
maze = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

# Directions for movement (right and down)
directions = [(0, 1), (1, 0)]  # (row, col)

# Convert maze to a graph (adjacency list representation)
def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # If it's an open path
                neighbors = []
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbors.append((nx, ny))
                graph[(i, j)] = neighbors
    return graph

# DFS Function using stack
def dfs(graph, start, goal):
    visited = []  # List for visited nodes
    stack = []    # Initialize stack

    visited.append(start)
    stack.append(start)

    while stack:
        node = stack.pop()  # LIFO: Pop from top
        print(node, end=" ")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in graph[node]:  # Visit neighbors
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

# Create graph from maze
graph = create_graph(maze)

# Define Start and Goal nodes
start_node = (0, 0)  # Starting point (0,0)
goal_node = (2, 2)   # Goal point (2,2)

# Run DFS
print("\nFollowing is the Depth-First Search (DFS):")
dfs(graph, start_node, goal_node)

"""goal agent based maze path finding"""

# Maze representation (1 = open path, 0 = wall)
maze = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

# Directions for movement (right and down)
directions = [(0, 1), (1, 0)]  # (row, col)

# Convert maze to a graph (adjacency list representation)
def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # If it's an open path
                neighbors = []
                for dx, dy in directions:  # Right and Down movements
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbors.append((nx, ny))
                graph[(i, j)] = neighbors
    return graph

# Goal-Based Agent using DFS
def goal_based_agent_dfs(graph, start, goal):
    stack = [(start, [start])]  # Stack stores (node, path taken)
    visited = set()

    while stack:
        node, path = stack.pop()  # LIFO: Pop from top

        if node in visited:
            continue

        print(f"Agent at: {node}, Path: {path}")

        if node == goal:  # Goal condition
            print("\n✅ Goal Reached! Path:", path)
            return path  # Return the found path

        visited.add(node)

        for neighbor in reversed(graph.get(node, [])):  # Reverse for correct order in stack
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))  # Append new path

    print("\n❌ Goal Not Reachable")
    return None

# Create graph from maze
graph = create_graph(maze)

# Define Start and Goal nodes
start_node = (0, 0)  # Starting point (0,0)
goal_node = (2, 2)   # Goal point (2,2)

# Run DFS with Goal-Based Agent
print("\n🧭 Goal-Based Agent using DFS:")
goal_based_agent_dfs(graph, start_node, goal_node)

"""# UCS

graph
"""

# Graph with different edge costs for UCS
graph = {
    'A':{'B': 2, 'C': 1} ,
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# UCS Function with Frontier and Visited
def ucs(graph, start, goal):
    # Initialize the frontier with the start node and cost 0
    frontier = [(start, 0)]  # (node, cost)
    visited = set()  # Set to keep track of visited nodes
    cost_so_far = {start: 0}  # Cost to reach each node
    came_from = {start: None}  # Path reconstruction

    while frontier:
        # Sort frontier by cost, simulate priority queue
        frontier.sort(key=lambda x: x[1])

        # Pop the node with the lowest cost
        current_node, current_cost = frontier.pop(0)

        # If we've already visited this node, skip it
        if current_node in visited:
            continue

        # Mark the current node as visited
        visited.add(current_node)

        # If we reach the goal, reconstruct the path and return
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with UCS. Path: {path}, Total Cost: {current_cost}")
            return

        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))  # Add to frontier

    print("Goal not found")

# Run UCS with updated costs, using frontier and visited
ucs(graph, 'A', 'I')

"""goal based agent  UCS """

import heapq

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return environment.ucs_search(percept, self.goal)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def ucs_search(self, start, goal):
        frontier = [(0, start)]  # Priority queue (cost, node)
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}

        while frontier:
            current_cost, current_node = heapq.heappop(frontier)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                return f"Goal {goal} found with UCS. Path: {path}, Total Cost: {current_cost}"

            for neighbor, cost in self.graph.get(current_node, {}).items():
                new_cost = current_cost + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    heapq.heappush(frontier, (new_cost, neighbor))

        return "Goal not found"


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)


# Graph Representation with Costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Create instances of agent and environment
agent = GoalBasedAgent(goal_node)
environment = Environment(graph)

# Run the agent
run_agent(agent, environment, start_node)

"""maze UCS"""

import heapq

class Maze:
    def __init__(self):
        self.grid = [
            ['S', ' ', 'X'],
            [' ', 'X', ' '],
            [' ', ' ', 'G']
        ]
        self.goal = (2, 2)  # Goal position
        self.start = (0, 0)  # Start position

    def get_neighbors(self, position):
        x, y = position
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        neighbors = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3 and self.grid[nx][ny] != 'X':  # Avoid obstacles
                neighbors.append(((nx, ny), 1))  # Each move costs 1
        return neighbors


def uniform_cost_search(maze):
    start, goal = maze.start, maze.goal
    priority_queue = [(0, start, [])]  # (cost, position, path)
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue
        visited.add(node)

        new_path = path + [node]
        if node == goal:
            return new_path, cost  # Goal reached

        for neighbor, step_cost in maze.get_neighbors(node):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + step_cost, neighbor, new_path))

    return None, float('inf')  # No solution found


def run_ucs_maze():
    maze = Maze()
    path, cost = uniform_cost_search(maze)

    if path:
        print("Path found:", path)
        print("Total cost:", cost)
    else:
        print("No path found")


# Run UCS on the maze
run_ucs_maze()

"""tree UCS"""

import heapq

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # (child_node, cost)

    def add_child(self, child_node, cost):
        self.children.append((child_node, cost))


def uniform_cost_search_tree(root, goal):
    priority_queue = [(0, root, [])]  # (cost, node, path)
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node.value in visited:
            continue
        visited.add(node.value)

        new_path = path + [node.value]
        if node.value == goal:
            return new_path, cost  # Goal reached

        for child, step_cost in node.children:
            if child.value not in visited:
                heapq.heappush(priority_queue, (cost + step_cost, child, new_path))

    return None, float('inf')  # No solution found


def build_sample_tree():
    root = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    D = TreeNode('D')
    E = TreeNode('E')
    F = TreeNode('F')
    G = TreeNode('G')

    root.add_child(B, 2)
    root.add_child(C, 3)
    B.add_child(D, 5)
    B.add_child(E, 1)
    C.add_child(F, 4)
    C.add_child(G, 2)

    return root


def run_ucs_tree():
    root = build_sample_tree()
    goal = 'G'  # Target node to find

    path, cost = uniform_cost_search_tree(root, goal)

    if path:
        print("Path found:", path)
        print("Total cost:", cost)
    else:
        print("No path found")


# Run UCS on the tree
run_ucs_tree()

"""UCS Implementation for a Goal-Based Agent in a Maze"""

import heapq

# Maze representation (1 = open path, 0 = wall)
maze = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

# Directions for movement (right, down, left, up)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (row, col)

# Convert maze to a weighted graph
def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # If it's an open path
                neighbors = {}
                for dx, dy in directions:  # Right, Down, Left, Up
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbors[(nx, ny)] = 1  # Uniform cost (1 for each step)
                graph[(i, j)] = neighbors
    return graph

# UCS Function using priority queue
def uniform_cost_search(graph, start, goal):
    pq = []  # Priority queue (min heap)
    heapq.heappush(pq, (0, start, []))  # (Cost, Node, Path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]  # Add node to path

        print(f"Exploring: {node}, Cost: {cost}, Path: {path}")

        if node == goal:
            print("\n✅ Goal Reached! Path:", path, "Total Cost:", cost)
            return path, cost

        for neighbor, step_cost in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + step_cost, neighbor, path))

    print("\n❌ Goal Not Reachable")
    return None, float('inf')

# Create graph from maze
graph = create_graph(maze)

# Define Start and Goal nodes
start_node = (0, 0)  # Starting point
goal_node = (3, 3)   # Goal point

# Run UCS
print("\n🧭 Goal-Based Agent using Uniform Cost Search:")
uniform_cost_search(graph, start_node, goal_node)

"""# BEST FIRST SEARCH using priority queue"""

from queue import PriorityQueue

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 5), ('C', 8)],
    'B': [('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 7)],
    'E': [('F', 2)],
    'F': []
}
def best_first_search(graph, start, goal):

    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))  # priority queue with priority as the heuristic value

    while not pq.empty():
        cost, node = pq.get()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            if node == goal:
                print("\nGoal reached!")
                return True

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    pq.put((weight, neighbor))

    print("\nGoal not reachable!")
    return False

# Example usage:
print("Best-First Search Path:")
best_first_search(graph, 'A', 'F')

"""# Best-First Search Algorithm with Manhattan Distance Heuristic for Maze Pathfinding"""

from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # cost from start node to current node
        self.h = 0  # heuristic estimate of the cost from current node to end node
        self.f = 0  # total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current_pos, end_pos):
    # Manhattan distance heuristic
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def best_first_search(maze, start, end):

    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    end_node = Node(end)
    frontier = PriorityQueue()
    frontier.put(start_node)
    visited = set()

    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position

        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to start from the start position

        visited.add(current_pos)

        # Generate adjacent nodes
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                new_node = Node(new_pos, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, end)
                new_node.f = new_node.h  # Best-First Search: f(n) = h(n)
                frontier.put(new_node)
                visited.add(new_pos)

    return None  # No path found

# Example maze
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

path = best_first_search(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")

"""# Implementation of Greedy Best-First Search (GBFS) Algorithm for Graph Traversal with Heuristic Guidance"""

# Graph with different edge costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Heuristic function (estimated cost to reach goal 'I')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 7,
    'F': 3,
    'G': 6,
    'H': 2,
    'I': 0  # Goal node
}

# Greedy Best-First Search Function (without heapq)
def greedy_bfs(graph, start, goal):
    frontier = [(start, heuristic[start])]  # List-based priority queue (sorted manually)
    visited = set()  # Set to keep track of visited nodes
    came_from = {start: None}  # Path reconstruction

    while frontier:
        # Sort frontier manually by heuristic value (ascending order)
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)  # Get node with best heuristic

        if current_node in visited:
            continue

        print(current_node, end=" ")  # Print visited node
        visited.add(current_node)

        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")
            return

        # Expand neighbors based on heuristic
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic[neighbor]))

    print("\nGoal not found")

# Run Greedy Best-First Search
print("\nFollowing is the Greedy Best-First Search (GBFS):")
greedy_bfs(graph, 'A', 'I')

"""Implementation of greedy Best-First Search Algorithm with Manhattan Distance Heuristic for Maze Pathfinding"""

import heapq

# Manhattan Distance heuristic function
def heuristic(a, b):
    """Calculates the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Function to generate valid neighbors
def generate_neighbors(position, maze):
    """Generates all possible neighbors in a grid while avoiding obstacles."""
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    neighbors = []

    for move in moves:
        new_pos = (position[0] + move[0], position[1] + move[1])
        # Check boundaries and avoid walls
        if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and maze[new_pos[0]][new_pos[1]] == 0:
            neighbors.append(new_pos)

    return neighbors

# Greedy Best-First Search Algorithm
def greedy_best_first_search(maze, start, goal):
    """Finds a path from start to goal in a maze using GBFS."""
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, goal), start))  # Push start node

    came_from = {start: None}  # Track the path

    while priority_queue:
        _, current = heapq.heappop(priority_queue)  # Get node with lowest heuristic

        if current == goal:
            break  # Stop when reaching the goal

        for neighbor in generate_neighbors(current, maze):
            if neighbor not in came_from:  # Avoid revisiting nodes
                came_from[neighbor] = current
                heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor))

    # Reconstruct path
    path = []
    step = goal
    while step is not None:
        path.append(step)
        step = came_from.get(step)
    path.reverse()

    return path if path[0] == start else []  # Return empty list if no path found

# Main function to run the search
def main():
    maze = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]  # 0 = open path, 1 = wall/obstacle

    start = (0, 0)
    goal = (4, 4)

    path = greedy_best_first_search(maze, start, goal)

    # Display the path found
    if path:
        print("Shortest Path:", path)
        print("Total Steps:", len(path) - 1)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()

"""# Implementation of A* Search Algorithm for Graph Traversal with Heuristic and Path Cost Optimization"""

# Graph with different edge costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Heuristic function (estimated cost to reach goal 'I')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 7,
    'F': 3,
    'G': 6,
    'H': 2,
    'I': 0  # Goal node
}

# A* Search Function
def a_star(graph, start, goal):
    frontier = [(start, 0 + heuristic[start])]  # List-based priority queue (sorted manually)
    visited = set()  # Set to keep track of visited nodes
    g_costs = {start: 0}  # Cost to reach each node from start
    came_from = {start: None}  # Path reconstruction

    while frontier:
        # Sort frontier by f(n) = g(n) + h(n)
        frontier.sort(key=lambda x: x[1])
        print(f'\nsorted Frontier: {frontier}')
        current_node, current_f = frontier.pop(0)  # Get node with lowest f(n)

        if current_node in visited:
            continue

        print(current_node, end=" ")  # Print visited node
        visited.add(current_node)

        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return




        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost  # Path cost from start to neighbor
            print(f'\nNew Cost = {new_g_cost}')
            f_cost = new_g_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
            print(f'\nf_Cost = {f_cost}')

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                print(f'\nUpdated G Cost: {g_costs} with Neigbhour: {neighbor}')
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))
                print(f'\nFrontier Loop: {frontier}')

    print("\nGoal not found")

# Run A* Search
print("\nFollowing is the A* Search:")
a_star(graph, 'A', 'I')

"""# Implementation of A* Search Algorithm using Priority Queue for Graph Traversal with Heuristic and Edge Costs"""

from queue import PriorityQueue


# Example graph represented as an adjacency list with heuristic values included
graph = {
    'A': [('B', 5, 9), ('C', 8, 5)],  # (neighbor, cost, heuristic)
    'B': [('D', 10, 4)],              # (neighbor, cost, heuristic)
    'C': [('E', 3, 7)],               # (neighbor, cost, heuristic)
    'D': [('F', 7, 5)],               # (neighbor, cost, heuristic)
    'E': [('F', 2, 1)],               # (neighbor, cost, heuristic)
    'F': []                           # (neighbor, cost, heuristic)
}


def astar_search(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    pq = PriorityQueue()  # Priority queue to prioritize nodes based on f-value (cost + heuristic)
    pq.put((0, start))  # Enqueue the start node with priority 0
    while not pq.empty():
        cost, node = pq.get()  # Dequeue the node with the lowest priority
        if node not in visited:
            print(node, end=' ')  # Print the current node
            visited.add(node)  # Mark the current node as visited
            if node == goal:  # Check if the goal node is reached
                print("\nGoal reached!")
                return True
            for neighbor, edge_cost, heuristic in graph[node]:  # Explore neighbors of the current node
                if neighbor not in visited:
                    # Calculate f-value for the neighbor (cost + heuristic)
                    f_value = cost + edge_cost + heuristic
                    pq.put((f_value, neighbor))  # Enqueue neighbor with priority based on f-value
    print("\nGoal not reachable!")
    return False


# Example usage:
print("A* Search Path:")
astar_search(graph, 'A', 'F')

"""Implementation of A* Algorithm with Manhattan Distance Heuristic for Maze Pathfinding"""

import heapq

class Node:
    def __init__(self, parent, position):
        self.parent = parent  # Parent node
        self.position = position  # Position (x, y)
        self.g = 0  # Cost from start to the current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost (f = g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def astar(maze, start, goal):
    open_list = []
    closed_list = set()
    start_node = Node(None, start)
    goal_node = Node(None, goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # If we reach the goal, reconstruct the path
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path (start to goal)

        # Generate neighbors (adjacent nodes)
        neighbors = [
            (0, 1),  # Up
            (1, 0),  # Right
            (0, -1),  # Down
            (-1, 0),  # Left
        ]

        for next_position in neighbors:
            neighbor_pos = (current_node.position[0] + next_position[0], current_node.position[1] + next_position[1])

            # Check if the neighbor is within the bounds of the maze
            if (0 <= neighbor_pos[0] < len(maze)) and (0 <= neighbor_pos[1] < len(maze[0])):

                # Check if the neighbor is walkable (not a wall)
                if maze[neighbor_pos[0]][neighbor_pos[1]] == 1:
                    continue

                # Create a neighbor node
                neighbor_node = Node(current_node, neighbor_pos)

                # If the neighbor is already in the closed list, skip it
                if neighbor_node.position in closed_list:
                    continue

                # Calculate the costs (g, h, f)
                neighbor_node.g = current_node.g + 1  # Assume cost between nodes is 1
                neighbor_node.h = abs(neighbor_node.position[0] - goal_node.position[0]) + abs(neighbor_node.position[1] - goal_node.position[1])
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Check if the neighbor is already in the open list with a higher f value
                if not any(neighbor_node.position == node.position and neighbor_node.f >= node.f for node in open_list):
                    heapq.heappush(open_list, neighbor_node)

    return None  # No path found


# Example maze (1 represents walkable cells, 0 represents walls)
maze = [
    [1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

start = (0, 0)  # Starting point (top-left corner)
goal = (4, 6)   # Goal point (bottom-right corner)

path = astar(maze, start, goal)
print("Path from start to goal:", path)

"""A* Algorithm (without Manhattan Distance)"""

import heapq
import math

class Node:
    def __init__(self, parent, position):
        self.parent = parent  # Parent node
        self.position = position  # Position (x, y)
        self.g = 0  # Cost from start to the current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost (f = g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def euclidean_distance(start, end):
    """Calculate the Euclidean distance heuristic (straight-line distance)"""
    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)


def astar(maze, start, goal):
    open_list = []
    closed_list = set()
    start_node = Node(None, start)
    goal_node = Node(None, goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # If we reach the goal, reconstruct the path
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path (start to goal)

        # Generate neighbors (adjacent nodes)
        neighbors = [
            (0, 1),  # Up
            (1, 0),  # Right
            (0, -1),  # Down
            (-1, 0),  # Left
        ]

        for next_position in neighbors:
            neighbor_pos = (current_node.position[0] + next_position[0], current_node.position[1] + next_position[1])

            # Check if the neighbor is within the bounds of the maze
            if (0 <= neighbor_pos[0] < len(maze)) and (0 <= neighbor_pos[1] < len(maze[0])):

                # Check if the neighbor is walkable (not a wall)
                if maze[neighbor_pos[0]][neighbor_pos[1]] == 0:
                    continue

                # Create a neighbor node
                neighbor_node = Node(current_node, neighbor_pos)

                # If the neighbor is already in the closed list, skip it
                if neighbor_node.position in closed_list:
                    continue

                # Calculate the costs (g, h, f)
                neighbor_node.g = current_node.g + 1  # Assume cost between nodes is 1
                neighbor_node.h = euclidean_distance(neighbor_node.position, goal_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Check if the neighbor is already in the open list with a higher f value
                if not any(neighbor_node.position == node.position and neighbor_node.f >= node.f for node in open_list):
                    heapq.heappush(open_list, neighbor_node)

    return None  # No path found


# Example maze (1 represents walkable cells, 0 represents walls)
maze = [
    [1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

start = (0, 0)  # Starting point (top-left corner)
goal = (4, 6)   # Goal point (bottom-right corner)

path = astar(maze, start, goal)
print("Path from start to goal:", path)

"""# UCS , Best First search ,and A* (without heapq)"""

graph = {
    'S': {'A': 3, 'B': 6, 'C': 5},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12, 'G': 14},
    'C': {'H': 7},
    'H': {'I': 5, 'J': 6},
    'I': {'K': 1, 'L': 10, 'M': 2},
    'D': {}, 'E': {}, 'F': {}, 'G': {},
    'J': {}, 'K': {}, 'L': {}, 'M': {}
}

heuristic = {
    'S': 10, 'A': 9, 'B': 7, 'C': 5, 'D': 8, 'E': 6, 'F': 4, 'G': 3,
    'H': 3, 'I': 2, 'J': 6, 'K': 2, 'L': 0, 'M': 1
}

def ucs(graph, start, goal):
    frontier = [(start, 0)]  # (node, cost)
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with UCS. Path: {path}, Total Cost: {current_cost}")
            return

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("Goal not found")

def best_first_search(graph, start, goal):
    frontier = [(start, heuristic[start])]
    visited = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with Best First Search. Path: {path}")
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                frontier.append((neighbor, heuristic[neighbor]))
                came_from[neighbor] = current_node

    print("Goal not found")

def a_star_search(graph, start, goal):
    frontier = [(start, 0 + heuristic[start])]
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with A*. Path: {path}, Total Cost: {cost_so_far[goal]}")
            return

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.append((neighbor, new_cost + heuristic[neighbor]))
                came_from[neighbor] = current_node

    print("Goal not found")

# Running all algorithms
ucs(graph, 'S', 'L')
best_first_search(graph, 'S', 'L')
a_star_search(graph, 'S', 'L')

"""for maze"""

import math

# Maze grid (1 = walkable, 0 = wall)
maze = [
    [1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

# Heuristic function: Manhattan distance for maze
def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

# Convert maze to a graph (adjacent nodes are walkable neighbors)
def get_neighbors(position):
    x, y = position
    neighbors = []
    # Check up, down, left, right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1:
            neighbors.append((nx, ny))
    return neighbors

def ucs(maze, start, goal):
    frontier = [(start, 0)]  # (node, cost)
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        # Sort frontier by the cost (UCS uses the cost from start)
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with UCS. Path: {path}, Total Cost: {current_cost}")
            return

        for neighbor in get_neighbors(current_node):
            new_cost = current_cost + 1  # All moves have a cost of 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("Goal not found")

def best_first_search(maze, start, goal):
    frontier = [(start, manhattan_distance(start, goal))]
    visited = set()
    came_from = {start: None}

    while frontier:
        # Sort frontier by heuristic (Best First Search uses only the heuristic)
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with Best First Search. Path: {path}")
            return

        for neighbor in get_neighbors(current_node):
            if neighbor not in visited:
                frontier.append((neighbor, manhattan_distance(neighbor, goal)))
                came_from[neighbor] = current_node

    print("Goal not found")

def a_star_search(maze, start, goal):
    frontier = [(start, 0 + manhattan_distance(start, goal))]
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        # Sort frontier by f = g + h (A* uses both cost and heuristic)
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with A*. Path: {path}, Total Cost: {cost_so_far[goal]}")
            return

        for neighbor in get_neighbors(current_node):
            new_cost = cost_so_far[current_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.append((neighbor, new_cost + manhattan_distance(neighbor, goal)))
                came_from[neighbor] = current_node

    print("Goal not found")

# Running all algorithms
print("Running UCS:")
ucs(maze, (0, 0), (4, 6))

print("\nRunning Best First Search:")
best_first_search(maze, (0, 0), (4, 6))

print("\nRunning A* Search:")
a_star_search(maze, (0, 0), (4, 6))


"""# Genetic Algorithm"""

import random

# Fitness Evaluation (Example: Counting ones in a binary chromosome)
def fitness(chromosome):
    return sum(chromosome)

# Selection (Roulette Wheel Selection)
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected = random.choices(population, probabilities, k=2)  # Select 2 parents
    return selected

# Crossover (Single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation (Bit-flip mutation)
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip the bit
    return chromosome

# Genetic Algorithm
def genetic_algorithm(initial_population, generations, mutation_rate):
    population = initial_population
    for generation in range(generations):
        # Fitness evaluation
        fitness_values = [fitness(chromosome) for chromosome in population]

        # Selection
        parents = roulette_wheel_selection(population, fitness_values)

        # Crossover
        offspring = [crossover(parents[0], parents[1]) for _ in range(len(population) // 2)]
        offspring = [gene for sublist in offspring for gene in sublist]  # Flatten the list

        # Mutation
        mutated_offspring = [mutate(chromosome, mutation_rate) for chromosome in offspring]

        # Replace the old population with the new one
        population = mutated_offspring

    # Return the best chromosome after all generations
    best_chromosome = max(population, key=fitness)
    # print('best_chromosome',best_chromosome)
    return best_chromosome

# Initial population
initial_population = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1]
]

# Genetic Algorithm parameters
generations = 50
mutation_rate = 0.01

# Apply GA
best_solution = genetic_algorithm(initial_population, generations, mutation_rate)
print("Best solution:", best_solution)
print("Fitness:", fitness(best_solution))

"""# N-Queen using GA"""

import random

# Define the number of queens
n = 8

# Fitness function: counts non-attacking pairs of queens
def calculate_fitness(individual):
    non_attacking_pairs = 0
    total_pairs = n * (n - 1) // 2  # Maximum possible non-attacking pairs

    # Check for conflicts
    for i in range(n):
        for j in range(i + 1, n):
            # No same column or diagonal conflict
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1

    # Fitness score is the ratio of non-attacking pairs
    return non_attacking_pairs / total_pairs

# Generate a random individual (chromosome) based on column positions
def create_random_individual():
    return random.sample(range(n), n)  # Ensure unique column positions
# create_random_individual()
# Create an initial population of random individuals
population_size = 10
population = [create_random_individual() for _ in range(population_size)]
population

def print_board(individual):
    n = len(individual)
    for row in range(n):
        line = ["Q" if col == individual[row] else "." for col in range(n)]
        print(" ".join(line))
    print("\n")

# Example
individual = [7, 1, 5, 3, 2, 0, 6, 4]
print_board(individual)


# Evaluate fitness for each individual
fitness_scores = [calculate_fitness(ind) for ind in population]
print("Fitness Scores:", fitness_scores)

# Select parents based on fitness
def select_parents(population, fitness_scores):
    sorted_population = [route for _, route in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population) // 2]

# Select parents
parents = select_parents(population, fitness_scores)
print("Selected Parents:", parents)

# Crossover function: single-point crossover with unique column positions
def crossover(parent1, parent2):
    point = random.randint(1, n - 2)  # Choose a crossover point
    child = parent1[:point] + parent2[point:]

    # Ensure unique column positions
    missing = set(range(n)) - set(child)
    duplicates = [col for col in child if child.count(col) > 1]
    for i in range(len(child)):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()
    return child

# Create new population using crossover
new_population = []
for _ in range(population_size):
    parent1, parent2 = random.sample(parents, 2)
    child = crossover(parent1, parent2)
    new_population.append(child)
print("New Population after Crossover:", new_population)

# Mutation function: swap two column positions
def mutate(individual):
    idx1, idx2 = random.sample(range(n), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Apply mutation with a probability of 0.1
mutation_rate = 0.1
for i in range(len(new_population)):
    if random.random() < mutation_rate:
        new_population[i] = mutate(new_population[i])
print("Population after Mutation:", new_population)

# Genetic Algorithm main function
def genetic_algorithm():
    population = [create_random_individual() for _ in range(population_size)]
    generation = 0
    best_fitness = 0

    while best_fitness < 1.0 and generation < 100:
        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)
        print(f"Generation {generation} Best Fitness: {best_fitness}")

        # Check for optimal solution
        if best_fitness == 1.0:
            break

        # Selection
        parents = select_parents(population, fitness_scores)

        # Crossover
        new_population = [crossover(random.choice(parents), random.choice(parents)) for _ in range(population_size)]

        # Mutation
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])

        population = new_population
        generation += 1

    # Return the best solution
    best_individual = max(population, key=calculate_fitness)
    return best_individual, calculate_fitness(best_individual)

# Run the Genetic Algorithm
solution, fitness = genetic_algorithm()
print("Best Solution:", solution)
print("Best Fitness:", fitness)

"""Different Crossovers"""

import random

# Single-Point Crossover
def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Two-Point Crossover
def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

# Uniform Crossover
def uniform_crossover(parent1, parent2):
    child1, child2 = [], []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1, child2

# Example Usage
p1 = [1, 0, 1, 0, 1, 1]
p2 = [0, 1, 0, 1, 0, 0]

print("Single Point:", single_point_crossover(p1, p2))
print("Two Point:", two_point_crossover(p1, p2))
print("Uniform:", uniform_crossover(p1, p2))

"""different mutations"""

import random

# Bit-Flip Mutation (Original)
def bit_flip_mutation(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip bit
    return chromosome

# Swap Mutation
def swap_mutation(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Scramble Mutation
def scramble_mutation(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = sorted(random.sample(range(len(chromosome)), 2))
        segment = chromosome[idx1:idx2]
        random.shuffle(segment)
        chromosome[idx1:idx2] = segment
    return chromosome

# Inversion Mutation
def inversion_mutation(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = sorted(random.sample(range(len(chromosome)), 2))
        chromosome[idx1:idx2] = reversed(chromosome[idx1:idx2])
    return chromosome

# Function to Apply a Specific Mutation Type
def apply_mutation(chromosome, mutation_rate, mutation_type="bit_flip"):
    if mutation_type == "bit_flip":
        return bit_flip_mutation(chromosome, mutation_rate)
    elif mutation_type == "swap":
        return swap_mutation(chromosome, mutation_rate)
    elif mutation_type == "scramble":
        return scramble_mutation(chromosome, mutation_rate)
    elif mutation_type == "inversion":
        return inversion_mutation(chromosome, mutation_rate)
    else:
        raise ValueError("Unknown mutation type!")

# Example Usage
chromosome = [1, 0, 1, 0, 1, 1]
mutation_rate = 0.3

print("Bit-Flip Mutation:", apply_mutation(chromosome[:], mutation_rate, "bit_flip"))
print("Swap Mutation:", apply_mutation(chromosome[:], mutation_rate, "swap"))
print("Scramble Mutation:", apply_mutation(chromosome[:], mutation_rate, "scramble"))
print("Inversion Mutation:", apply_mutation(chromosome[:], mutation_rate, "inversion"))

"""genetic algorithm template"""

import random

# Define the fitness function (Modify this function as per the question)
def fitness(x):
    """Compute fitness value for a given x."""
    return x**2 + x  # Example: f(x) = x^2 + x (Modify as required)

# Convert a binary string to an integer
def binary_to_decimal(binary_str):
    """Convert binary string to decimal integer."""
    return int(binary_str, 2)

# Convert an integer to a fixed-length binary string
def decimal_to_binary(num, bit_length=5):
    """Convert decimal integer to binary string of given bit length."""
    return format(num, f'0{bit_length}b')

# Generate the initial population
def initialize_population(pop_size, bit_length=5, min_val=0, max_val=31):
    """Generate a random initial population of binary strings."""
    return [decimal_to_binary(random.randint(min_val, max_val), bit_length) for _ in range(pop_size)]

# Roulette Wheel Selection
def roulette_wheel_selection(population):
    """Select two parents using the roulette wheel method (probability proportional to fitness)."""
    fitness_values = [fitness(binary_to_decimal(chromosome)) for chromosome in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    selected = random.choices(population, probabilities, k=2)  # Select 2 parents
    return selected

# Single-Point Crossover
def single_point_crossover(parent1, parent2):
    """Perform single-point crossover between two parents."""
    point = random.randint(1, len(parent1) - 1)  # Choose a crossover point
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Two-Point Crossover
def two_point_crossover(parent1, parent2):
    """Perform two-point crossover between two parents."""
    point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

# Uniform Crossover
def uniform_crossover(parent1, parent2):
    """Perform uniform crossover where each bit is randomly selected from either parent."""
    child1 = ''.join(random.choice([p1, p2]) for p1, p2 in zip(parent1, parent2))
    child2 = ''.join(random.choice([p1, p2]) for p1, p2 in zip(parent1, parent2))
    return child1, child2

# Binary Mutation (Single Bit Flip)
def binary_mutation(chromosome, mutation_rate=0.01):
    """Perform binary mutation by flipping a random bit with a small probability."""
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'  # Flip bit
    return ''.join(chromosome)

# Swap Mutation
def swap_mutation(chromosome):
    """Perform swap mutation by swapping two random positions in the chromosome."""
    chromo_list = list(chromosome)
    idx1, idx2 = random.sample(range(len(chromo_list)), 2)
    chromo_list[idx1], chromo_list[idx2] = chromo_list[idx2], chromo_list[idx1]
    return ''.join(chromo_list)

# Inversion Mutation
def inversion_mutation(chromosome):
    """Perform inversion mutation by reversing a random segment."""
    chromo_list = list(chromosome)
    start, end = sorted(random.sample(range(len(chromo_list)), 2))
    chromo_list[start:end+1] = reversed(chromo_list[start:end+1])
    return ''.join(chromo_list)

# Genetic Algorithm
def genetic_algorithm(pop_size=10, generations=50, mutation_rate=0.01, crossover_method='single', mutation_method='binary'):
    """Run the genetic algorithm to find the optimal solution."""
    # Initialize population
    population = initialize_population(pop_size)

    for _ in range(generations):
        # Selection
        parents = roulette_wheel_selection(population)

        # Crossover (Choose method)
        offspring = []
        for _ in range(pop_size // 2):  # Generate new population
            if crossover_method == 'single':
                child1, child2 = single_point_crossover(parents[0], parents[1])
            elif crossover_method == 'two-point':
                child1, child2 = two_point_crossover(parents[0], parents[1])
            elif crossover_method == 'uniform':
                child1, child2 = uniform_crossover(parents[0], parents[1])
            offspring.extend([child1, child2])

        # Mutation (Choose method)
        for i in range(len(offspring)):
            if mutation_method == 'binary':
                offspring[i] = binary_mutation(offspring[i], mutation_rate)
            elif mutation_method == 'swap':
                offspring[i] = swap_mutation(offspring[i])
            elif mutation_method == 'inversion':
                offspring[i] = inversion_mutation(offspring[i])

        # Update population
        population = offspring

    # Find the best solution
    best_chromosome = max(population, key=lambda c: fitness(binary_to_decimal(c)))
    best_x = binary_to_decimal(best_chromosome)
    best_fitness = fitness(best_x)

    return best_x, best_fitness

# Run the Genetic Algorithm with parameters
if __name__ == "__main__":
    pop_size = 10  # Population size
    generations = 50  # Number of generations
    mutation_rate = 0.01  # Mutation probability
    crossover_method = 'single'  # Choose: 'single', 'two-point', 'uniform'
    mutation_method = 'binary'  # Choose: 'binary', 'swap', 'inversion'

    best_x, max_fitness = genetic_algorithm(pop_size, generations, mutation_rate, crossover_method, mutation_method)
    print(f"Best x: {best_x}, Maximum f(x): {max_fitness}")

"""equation question"""

import random

# Function to evaluate fitness: f(x) = x^2 + x
def fitness(x):
    return x**2 + x

# Convert binary string to integer
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Convert integer to 5-bit binary string
def decimal_to_binary(num):
    return format(num, '05b')

# Generate initial population of binary strings
def initialize_population(pop_size):
    return [decimal_to_binary(random.randint(0, 31)) for _ in range(pop_size)]

# Roulette wheel selection based on fitness
def roulette_wheel_selection(population):
    fitness_values = [fitness(binary_to_decimal(chromosome)) for chromosome in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    selected = random.choices(population, probabilities, k=2)  # Select 2 parents
    return selected

# Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, 4)  # Choose a crossover point (1 to 4)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Single-bit mutation
def mutate(chromosome, mutation_rate=0.01):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'  # Flip bit
    return ''.join(chromosome)

# Genetic Algorithm
def genetic_algorithm(pop_size, generations, mutation_rate):
    population = initialize_population(pop_size)

    for _ in range(generations):
        # Selection
        parents = roulette_wheel_selection(population)

        # Crossover
        offspring = []
        for _ in range(pop_size // 2):  # Create new population
            child1, child2 = crossover(parents[0], parents[1])
            offspring.append(child1)
            offspring.append(child2)

        # Mutation
        offspring = [mutate(child, mutation_rate) for child in offspring]

        # Update population
        population = offspring

    # Find best solution
    best_chromosome = max(population, key=lambda c: fitness(binary_to_decimal(c)))
    best_x = binary_to_decimal(best_chromosome)
    best_fitness = fitness(best_x)

    return best_x, best_fitness

# Parameters
pop_size = 10
generations = 50
mutation_rate = 0.01

# Run the Genetic Algorithm
best_x, max_fitness = genetic_algorithm(pop_size, generations, mutation_rate)
print(f"Best x: {best_x}, Maximum f(x): {max_fitness}")

"""book arrangment"""

import random

# Define book widths (Example: 6 books with given widths)
books = [5, 7, 3, 8, 6, 4]

# Constraints (Example: book 2 must be next to book 3, and books 1 & 5 can't be adjacent)
must_be_next_to = (2, 3)
cannot_be_adjacent = (1, 5)

# Generate an initial population (random permutations of books)
def initialize_population(pop_size, num_books):
    return [random.sample(range(num_books), num_books) for _ in range(pop_size)]

# Fitness function: minimize the total width (inverted for maximization)
def fitness(arrangement):
    total_width = sum(books[i] for i in arrangement)

    # Apply penalties for constraint violations
    penalty = 0
    for i in range(len(arrangement) - 1):
        if (arrangement[i], arrangement[i + 1]) == must_be_next_to or \
           (arrangement[i + 1], arrangement[i]) == must_be_next_to:
            penalty -= 5  # Bonus if constraint is met
        if (arrangement[i], arrangement[i + 1]) == cannot_be_adjacent or \
           (arrangement[i + 1], arrangement[i]) == cannot_be_adjacent:
            penalty += 10  # Penalty if constraint is violated

    return 1 / (total_width + penalty + 1)  # Higher fitness for lower total width

# Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return random.choices(population, probabilities, k=2)  # Select 2 parents

# Single-Point Crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + [x for x in parent2 if x not in parent1[:point]]
    child2 = parent2[:point] + [x for x in parent1 if x not in parent2[:point]]
    return child1, child2

# Mutation (Swap Mutation)
def mutate(arrangement, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(arrangement)), 2)
        arrangement[i], arrangement[j] = arrangement[j], arrangement[i]
    return arrangement

# Genetic Algorithm Function
def genetic_algorithm(pop_size, generations, mutation_rate):
    population = initialize_population(pop_size, len(books))

    for _ in range(generations):
        fitness_values = [fitness(chrom) for chrom in population]
        new_population = []

        for _ in range(pop_size // 2):  # Half as two parents create two children
            parent1, parent2 = roulette_wheel_selection(population, fitness_values)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])

        population = new_population  # Update with new generation

    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)

# Run the Genetic Algorithm
best_arrangement, best_fitness = genetic_algorithm(pop_size=10, generations=50, mutation_rate=0.1)

print("Best book arrangement:", best_arrangement)
print("Fitness:", best_fitness)

"""travelling salesman problem"""

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def ucs(self, graph, start, goal):

        frontier = [(start, 0)]
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}

        while frontier:

            frontier.sort(key=lambda x: x[1])


            current_node, current_cost = frontier.pop(0)


            if current_node in visited:
                continue


            visited.add(current_node)


            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print(f"Goal found with UCS. Path: {path}, Total Cost: {current_cost}")
                return path


            for neighbor, cost in graph[current_node].items():
                new_cost = current_cost + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    frontier.append((neighbor, new_cost))

        print("Goal not found")
        return None


    def act(self, percept, graph, depth_limit=None):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:

            return self.ucs(graph, percept, self.goal)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node, depth_limit=None):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph, depth_limit)
    print(action)


graph = {
    '1': {'2': 10, '3': 15, '4': 20},
    '2': {'1': 10, '3': 35, '4': 25},
    '3': {'1': 15, '2': 35, '4': 30},
    '4': {'1': 20, '2': 25, '3': 30}
}


start_node = '1'
goal_node = '4'


agent = GoalBasedAgent(goal_node)
environment = Environment(graph)

run_agent(agent, environment, start_node)

"""Implement a genetic algorithm to solve the TSP (Traveling Salesman Problem) for a
given set of 10 cities.
"""

import random
import math


def distance(city1, city2):

    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def total_route_distance(route, cities):

    return sum(distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1)) + distance(
        cities[route[-1]], cities[route[0]])


def fitness(route, cities):

    return 1 / total_route_distance(route, cities)


def roulette_wheel_selection(population, fitness_values):

    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected = random.choices(population, probabilities, k=2)
    return selected


def crossover(parent1, parent2):

    size = len(parent1)
    p1, p2 = sorted(random.sample(range(size), 2))
    child1 = [-1] * size
    child2 = [-1] * size
    child1[p1:p2] = parent1[p1:p2]
    child2[p1:p2] = parent2[p1:p2]

    fill_child(child1, parent2, p2)
    fill_child(child2, parent1, p2)

    return child1, child2


def fill_child(child, parent, start):

    index = start
    for gene in parent:
        if gene not in child:
            if index >= len(child):
                index = 0
            child[index] = gene
            index += 1


def mutate(route, mutation_rate):

    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route


def genetic_algorithm(cities, population_size=50, generations=100, mutation_rate=0.02):

    num_cities = len(cities)
    population = [random.sample(range(num_cities), num_cities) for _ in range(population_size)]

    for _ in range(generations):
        fitness_values = [fitness(route, cities) for route in population]
        new_population = []

        for _ in range(population_size // 2):
            parents = roulette_wheel_selection(population, fitness_values)
            offspring = crossover(parents[0], parents[1])
            new_population.extend(mutate(child, mutation_rate) for child in offspring)

        population = new_population

    best_route = min(population, key=lambda route: total_route_distance(route, cities))
    return best_route, total_route_distance(best_route, cities)

cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
best_route, best_distance = genetic_algorithm(cities)

print("Best route:", best_route)
print("Total distance:", best_distance)

#PRACITCE QUESTIONS

#GRID TO GRAPH 

# Grid
grid = [
    ['S',1,4,3,5],
    ['#',1,2,'#',3],
    [5,2,1,1,2],
    ['#',2,'#',1,3],
    [2,1,2,2,'G']
]

rows = len(grid)
cols = len(grid[0])

directions = [(0,1),(1,0),(0,-1),(-1,0)]

# Create graph
graph = {}

for i in range(rows):
    for j in range(cols):

        if grid[i][j] != '#':
            neighbors = []

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != '#':
                    neighbors.append((ni, nj))

            graph[(i,j)] = neighbors

# Find start and goal
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            start = (i,j)
        if grid[i][j] == 'G':
            goal = (i,j)

"BFS"

def bfs(graph, start, goal):

    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:

        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("\nBFS:")
bfs(graph, start, goal)
                            

"DFS"
def dfs(graph, start, goal):

    visited = []
    stack = []

    visited.append(start)
    stack.append(start)

    while stack:

        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            return

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


print("\nDFS:")
dfs(graph, start, goal)

"UCS"
def get_cost(cell):
    if grid[cell[0]][cell[1]] in ['S','G']:
        return 0
    return grid[cell[0]][cell[1]]


def ucs(graph, start, goal):

    frontier = [(start, 0)]
    visited = set()

    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:

        frontier.sort(key=lambda x: x[1])

        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:

            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()
            print("Path:", path)
            print("Cost:", current_cost)
            return

        for neighbour in graph[current_node]:

            new_cost = current_cost + get_cost(neighbour)

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                came_from[neighbour] = current_node
                frontier.append((neighbour, new_cost))


print("\nUCS:")
ucs(graph, start, goal)

#QUESTION 02

grid = [
    ['S',4,2,0,1],
    [3,'#',3,'#',1],
    [2,2,2,1,1],
    ['#',3,'#',1,2],
    [3,2,3,2,'G']
]

rows = len(grid)
cols = len(grid[0])

directions = [(0,1),(1,0),(0,-1),(-1,0)]

graph = {}

for i in range(rows):
    for j in range(cols):

        if grid[i][j] != '#':
            neighbors = []

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != '#':
                    neighbors.append((ni, nj))

            graph[(i,j)] = neighbors

# start and goal
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            start = (i,j)
        if grid[i][j] == 'G':
            goal = (i,j)

# heuristic
def h(node):
    val = grid[node[0]][node[1]]
    if val in ['S','G']:
        return 0
    return val


"GBFS"
def greedy(graph, start, goal):

    frontier = [(start, h(start))]
    visited = []

    while frontier:

        frontier.sort(key=lambda x: x[1])

        current_node, _ = frontier.pop(0)

        print(current_node, end=" ")

        if current_node == goal:
            print("\nGoal found!")
            return

        if current_node not in visited:
            visited.append(current_node)

            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    frontier.append((neighbour, h(neighbour)))


print("\nGreedy Best First:")
greedy(graph, start, goal)

"A STAR"
def astar(graph, start, goal):

    frontier = [(start, 0)]
    visited = set()

    g_cost = {start: 0}
    came_from = {start: None}

    while frontier:

        frontier.sort(key=lambda x: x[1])

        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:

            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()
            print("Path:", path)
            print("Cost:", g_cost[goal])
            return

        for neighbour in graph[current_node]:

            new_g = g_cost[current_node] + 1

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                f = new_g + h(neighbour)

                came_from[neighbour] = current_node
                frontier.append((neighbour, f))


print("\nA* Search:")
astar(graph, start, goal)