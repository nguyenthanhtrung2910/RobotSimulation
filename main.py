import logging as log
import simpy
from Cell import Cell
from Field import Field 
from Robot import Robot
from GetCommand import GetCommand
log.basicConfig(level=log.INFO, 
                filename="evens.log", 
                filemode="w", 
                format="%(levelname)s: At %(asctime)s %(message)s", 
                datefmt='%m/%d/%Y %I:%M:%S %p')

field = Field(size=9, file_for_field_name='field.txt')

env = simpy.rt.RealtimeEnvironment(factor=1)
store = simpy.FilterStore(env, capacity=81)
store.items = field.cells.copy()

robot1 = Robot(cell=field.get_cells_by_coordinate('c2')[0], name='robotA', env=env, store=store)
robot2 = Robot(cell=field.get_cells_by_coordinate('c4')[0], name='robotB', env=env, store=store)

robot1.action = env.process(robot1.run(commands=GetCommand('commands/command1.txt').set_сommands(), duration=1))
robot2.action = env.process(robot2.run(commands=GetCommand('commands/command2.txt').set_сommands(), duration=1))

env.run()

