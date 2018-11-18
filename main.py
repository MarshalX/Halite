import hlt

from hlt import constants
from hlt.positionals import Direction

import random
import logging

game = hlt.Game()

game_map = game.game_map

links_count = (game_map.width * game_map.height) * 2
node_count = game_map.width * game_map.height

graph = [[0 for _ in range(links_count)] for _ in range(node_count)]

current_link = 0
for node_number in range(node_count):
    if (node_number + 1) % game_map.height != 0:
        graph[node_number][current_link] = 1
        graph[node_number + 1][current_link] = 1

        current_link += 1

    if node_number % game_map.width == 0:
        graph[node_number][current_link] = 1
        graph[node_number + game_map.width - 1][current_link] = 1

        current_link += 1

    if node_number < game_map.height:
        graph[node_number][current_link] = 1
        graph[game_map.width * game_map.height - game_map.width + node_number][current_link] = 1

        current_link += 1

    if node_number + game_map.width < node_count:
        graph[node_number][current_link] = 1
        graph[node_number + game_map.width][current_link] = 1

        current_link += 1

# with open('graph.txt', 'w') as f:
#     for i in range(node_count):
#         for j in range(links_count):
#             symbol = '\n' if j == links_count - 1 else ', '
#             f.write('{}{}'.format(graph[i][j], symbol))

game.ready("MyPythonBot")

logging.info("Successfully created bot! My Player ID is {}.".format(game.my_id))

while True:
    game.update_frame()

    me = game.me
    game_map = game.game_map

    command_queue = []

    for ship in me.get_ships():
        if game_map[ship.position].halite_amount < constants.MAX_HALITE / 10 or ship.is_full:
            command_queue.append(
                ship.move(
                    random.choice([Direction.North, Direction.South, Direction.East, Direction.West])))
        else:
            command_queue.append(ship.stay_still())

    if game.turn_number <= 200 and me.halite_amount >= constants.SHIP_COST and not game_map[me.shipyard].is_occupied:
        command_queue.append(me.shipyard.spawn())

    game.end_turn(command_queue)
