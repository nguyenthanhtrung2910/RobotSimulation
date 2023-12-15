from Cell import Cell
import logging as log
class Robot:
    """
    Robot object
    The robot has at a certain time: name, position, direction, load, and a counter of delivered load.
    The following actions are available: forward 1 step (forward), rotate (rotate), take a load (set_load),
    throw a load (throw_load). Each action takes the time specified by the duration parameter.
    The robot can only step on a cell in the store object, which contains free cells. When moving forward, 
    robot must first take the front cell from the store; if this fails, then you must wait until another 
    robot put back this cell to the store. Then, freeing the previous cell, robot return it to store.
    When initializing, immediately set the robot as an object located on a cell and occupy this cell from store.
    """
    def __init__(self, env, store, cell, name, direction = 90, load = 0, count = 0) -> None:
        self.env = env
        self.cell = cell
        self.store = store
        self.name = name
        self.direction = direction
        self.load = load
        self.count = count
        self.cell.located = self.name
        self.store.get(lambda cell: cell == self.cell)

    def __repr__(self) -> str:
        return '{} locates in position {}, has direction {} and load {}'.format(self.name, self.cell, self.direction, self.load)
    
    #Next cell corresponding to the robot's direction
    @property
    def next_cell(self):
        if self.direction == 90: return self.cell.front
        if self.direction == 180: return self.cell.left
        if self.direction == 270: return self.cell.back
        if self.direction == 0: return self.cell.right

    def forward(self, duration):
        log.info('{} locates in position {}, starting move forward'.format(self.name, self.cell))
        yield self.store.get(lambda cell: cell == self.next_cell)
        yield self.store.put(self.cell)
        self.cell.located = None
        self.next_cell.located = self.name
        self.cell = self.next_cell
        yield self.env.timeout(duration)
        log.info('{} locates in position {}, finishing move forward'.format(self.name, self.cell))
        
    def rotate(self, angel, duration):
        log.info('{} locates in position {}, starting rotate'.format(self.name, self.cell))
        self.direction = (self.direction + angel)%360
        yield self.env.timeout(duration)
        log.info('{} locates in position {}, finishing rotate'.format(self.name, self.cell))

    def set_load(self, load, duration):
        log.info('{} locates in position {}, starting set load'.format(self.name, self.cell))
        self.load = load
        yield self.env.timeout(duration)
        log.info('{} locates in position {}, finishing set load'.format(self.name, self.cell))
    
    def throw_load(self, duration):
        log.info('{} locates in position {}, starting throw load'.format(self.name, self.cell))
        self.load = 0
        self.count = self.count +1
        yield self.env.timeout(duration)
        log.info('{} locates in position {}, finishing throw load'.format(self.name, self.cell))

    def run(self, commands, duration):
        for i, command in enumerate(commands):
            command = command.split()
            if command[0] == 'FORWARD': 
                if self.next_cell == None :
                    log.error('The robot moves outside the field. The command {} on line {} is illegal'.format(' '.join(command), i))
                    break
                yield self.env.process(self.forward(duration))
            if command[0] == 'ROTATE' : 
                if int(command[1]) % 90 != 0 :
                    log.error('The robot cannot turn through an angle other than a multiple of 90. The command {} on line {} is illegal'.format(' '.join(command), i))
                    break
                yield self.env.process(self.rotate(int(command[1]), duration))
            if command[0] == 'SETLOAD': 
                if self.cell.color != 'gr' :
                    log.error('The robot can take the load only if the cell is green. The command {} on line {} is illegal'.format(' '.join(command), i))
                    break
                yield self.env.process(self.set_load(int(command[1]), duration))
            if command[0] == 'THROWLOAD': 
                if self.cell.color != 'y' :
                    log.error('The robot can throw the load only if the cell is yellow. The command {} on line {} is illegal'.format(' '.join(command), i))
                    break
                yield self.env.process(self.throw_load(duration))