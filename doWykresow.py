import csv
import time
import random
import tkinter as tk
from datetime import datetime
from os import listdir
from os.path import isfile, join

from matplotlib import pyplot as plt


class Maze:
    def __init__(self):
        self.maze_dictionary = {}
        self.maze_iteration = 1
        self.canvas = None
        self.agent = None
        self.line_with = 32
        self.goal = (20, 20)

    def LoadMaze(self, url):
        with open(url, 'r') as maze_file:
            lane = csv.reader(maze_file)
            next(lane)
            for i in lane:
                c = i[0].split(',')
                c[0] = int(c[0].lstrip('('))
                c[1] = int(c[1].rstrip(')'))
                self.maze_dictionary[tuple(c)] = {"E": int(i[1]), "W": int(i[2]), "N": int(i[3]), "S": int(i[4])}
        return self.maze_dictionary

    def ChangeTrace(self, url):
        with open(url, 'r') as maze_file1:
            lane1 = csv.reader(maze_file1)
            next(lane1)
            for i in lane1:
                c = i[0].split(',')
                c[0] = int(c[0].lstrip('('))
                c[1] = int(c[1].rstrip(')'))
                self.maze_dictionary[tuple(c)] = {"E": int(i[1]), "W": int(i[2]), "N": int(i[3]), "S": int(i[4])}
        return self.maze_dictionary

    def DrawMaze(self, maze_dictionary):
        if self.canvas is None:
            self.canvas = tk.Canvas(window, width=1200, height=720, bg="black")
            self.start_time = datetime.now()
            self.canvas.create_text(800, 100, text="Etap: ", fill="white", font=('Helvetica 25 bold'))
            self.canvas.pack()

        self.canvas.delete('maze')
        self.canvas.create_rectangle(self.goal[0] * self.line_with, self.goal[1] * self.line_with,
                                     self.goal[0] * self.line_with + self.line_with,
                                     self.goal[1] * self.line_with + self.line_with, fill="green", tags='maze')
        for i in maze_dictionary:
            if maze_dictionary[i]["E"] == 0:
                self.canvas.create_line(self.line_with * i[1] + self.line_with, self.line_with * i[0],
                                        self.line_with * i[1] + self.line_with, self.line_with * i[0] + self.line_with,
                                        fill="white", tags='maze')
            if maze_dictionary[i]["W"] == 0:
                self.canvas.create_line(self.line_with * i[1], self.line_with * i[0], self.line_with * i[1],
                                        self.line_with * i[0] + self.line_with, fill="white", tags='maze')
            if maze_dictionary[i]["N"] == 0:
                self.canvas.create_line(self.line_with * i[1], self.line_with * i[0],
                                        self.line_with * i[1] + self.line_with, self.line_with * i[0], fill="white",
                                        tags='maze')
            if maze_dictionary[i]["S"] == 0:
                self.canvas.create_line(self.line_with * i[1], self.line_with * i[0] + self.line_with,
                                        self.line_with * i[1] + self.line_with, self.line_with * i[0] + self.line_with,
                                        fill="white", tags='maze')

    def DrawAgent(self):
        # self.canvas.delete('agent')
        if self.agent is not None:
            x, y = self.agent
            x1, y1 = x * 32 + 6, y * 32 + 6
            x2, y2 = x1 + 20, y1 + 20
            # self.canvas.create_oval(x1, y1, x2, y2, fill='red', tags='agent')

    def move_agent(self, action, maze_dictionary):
        # # self.canvas.delete('stoper')
        # elapsed_time = datetime.now() - self.start_time
        # formatted_time = str(elapsed_time).split(".")[0]
        # self.canvas.create_text(850, 200, text=f"Czas: {formatted_time}", fill="White", font=('Helvetica 25 bold'),
        #                         tags="stoper")

        x, y = self.agent
        if action == 'up' and y > 1 and maze_dictionary[y, x]["N"] == 1:
            self.agent = (x, y - 1)
        elif action == 'down' and y < 20 and maze_dictionary[y, x]["S"] == 1:
            self.agent = (x, y + 1)
        elif action == 'left' and x > 1 and maze_dictionary[y, x]["W"] == 1:
            self.agent = (x - 1, y)
        elif action == 'right' and x < 20 and maze_dictionary[y, x]["E"] == 1:
            self.agent = (x + 1, y)

    def get_state(self):
        return self.agent

    def is_goal_reached(self):
        return self.agent == self.goal

    def reset_agent(self):
        self.agent = (1, 1)
        # self.canvas.delete('count')
        # self.canvas.create_text(870, 100, text=text_iteration_episodes, fill="white", font=('Helvetica 25 bold'),
        #                         tags='count')


class Agent:
    def __init__(self, actions):
        self.actions = actions
        self.action = None
        self.state = None
        self.epsilon = 0.1
        self.learning_rate = 0.1
        self.discount_factor = 0.1
        self.q_table = {}
        self.q_table_iteration = 1
        self.q_table_path = "test_q_table" + str(self.q_table_iteration) + ".csv"
        self.episode_rewards = []
        self.last_known_maze = None

    def choose_action(self, state):
        self.state = state
        if random.random() < self.epsilon:
            self.action = random.choice(self.actions)
        else:
            q_values = [self.q_table.get((state, a), 0.0) for a in self.actions]
            max_q = max(q_values)
            best_actions = [a for a, q in zip(self.actions, q_values) if q == max_q]
            self.action = random.choice(best_actions)
        return self.action

    def learn(self, next_state, reward):
        q_value = max([self.q_table.get((next_state, a), 0.0) for a in self.actions])

        if maze.is_goal_reached():
            reward += 100  # Nagroda za osiągnięcie celu
        else:
            reward -= 1  # Kara za każdy ruch

        if next_state == self.state:
            reward -= 2  # Kara za uderzenie w ścianę

        self.q_table[(self.state, self.action)] = (1 - self.learning_rate) * self.q_table.get(
            (self.state, self.action), 0.0) + self.learning_rate * (reward + self.discount_factor * q_value)

    def reset(self):
        self.state = None

    def monitor_route(self, maze_dictionary):
        if self.last_known_maze is not None and maze_dictionary[self.state[1], self.state[0]] != self.last_known_maze[
            self.state[1], self.state[0]]:
            print("Trasa uległa zmianie. Resetowanie agenta.")
            self.save_q_table_to_csv()
            maze.reset_agent()
            self.q_table.clear()
            self.load_q_table_from_csv()
            self.last_known_maze = None
            window.update()

    def save_q_table_to_csv(self):
        print("Zapis,", self.q_table_iteration)
        with open(self.q_table_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, value in self.q_table.items():
                state, action = key
                csv_writer.writerow([state[0], state[1], action, value])
        self.q_table_iteration += 1
        self.q_table_path = "q_table" + str(self.q_table_iteration) + ".csv"

    def load_q_table_from_csv(self):
        self.q_table = {}
        with open(self.q_table_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                state = (int(row[0]), int(row[1]))
                action = row[2]
                value = float(row[3])
                self.q_table[(state, action)] = value

    def run_episode(self, maze, maze_dictionary):
        maze.reset_agent()
        self.reset()
        total_reward = 0

        while not maze.is_goal_reached():
            state = maze.get_state()
            action = self.choose_action(state)
            maze.move_agent(action, maze_dictionary)
            next_state = maze.get_state()

            if maze.is_goal_reached():
                reward += 100  # Nagroda za osiągnięcie celu
            else:
                reward = -1  # Kara za każdy ruch

            if next_state == state:
                reward -= 2  # Kara za uderzenie w ścianę

            total_reward += reward
            self.learn(next_state, reward)
            self.monitor_route(maze_dictionary)
            # maze.DrawAgent()
            # window.update()
            # time.sleep(0.001)

        self.episode_rewards.append(total_reward)
        print("Suma nagród dla epizodu:", total_reward)

#####################   Main ######################

iteration_episodes = 1
num_episodes = 10000000
tablica = list(range(1, num_episodes + 1))
window = tk.Tk()
maze = Maze()
maze_dictionary = maze.LoadMaze("Maze"+str(maze.maze_iteration)+".csv")
print(maze_dictionary)
# maze.DrawMaze(maze_dictionary)
# maze.DrawAgent()
agent = Agent(['up', 'down', 'left', 'right'])
agent.load_q_table_from_csv()
j = 0
for _ in range(num_episodes):
    tablica2 = list(range(1, (_-j)+1))
    last20 = 0
    srednia = 0
    if _ > 20:
        last20 = agent.episode_rewards[-10:]
        srednia = sum(last20) / len(last20)
        if min(last20) >= srednia - 10 and max(last20) <= srednia + 10:

            plt.plot(tablica2, agent.episode_rewards[-(_-j):])
            plt.xlabel('Epizody')
            plt.ylabel('Suma Nagród')
            plt.title('epsilon = {:.1f} | learning rate = {:.1f} | discount factor = {:.1f}'.format(agent.epsilon, agent.learning_rate, agent.discount_factor))
            plt.show()
            j = _
            agent.q_table.clear()
            iteration_episodes = 1
            agent.discount_factor += 0.1


    text_iteration_episodes = str(iteration_episodes)
    iteration_episodes = iteration_episodes + 1
    agent.run_episode(maze, maze_dictionary)

window.mainloop()

