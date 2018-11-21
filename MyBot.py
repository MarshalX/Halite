import random
import logging

import hlt

from hlt import constants
from hlt.positionals import Direction

from data.Graph import Graph

game = hlt.Game()

game_map = game.game_map

G = Graph(game_map)
logging.info(G)

game.ready("MyPythonBot")

logging.info("Successfully created bot! My Player ID is {}.".format(game.my_id))

while True:
    game.update_frame()

    me = game.me
    game_map = game.game_map

    G.update_weight(game_map)

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
