# Simulation for delivery Robot by simpy
* The field of the environment consists of cells, each of them is instance of Cell object. The Cell object has coordinates, color, target, the robot located on it and neighboring cells (front, right, back, left). Field's informations are loaded from _field.txt_ file. <br/>
* Commands from controller for each robot in _commands_ folder. <br/>
* When robot go outside the field or pick up or drop off illegally load or turn through illegal angel, program stop and report it in .log file. <br/>
* All robots shares common field and can not go forward until the next cell is free.
## Color Map:
| 9 |   W |    W |    Y |    W |    Y |    W |    Y |    W |    W |   
|:---------:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 8 |   W |    W |    W |    W |    W |    W |    W |    W |    W |    
| 7 |   Y |    W |    W |    W |    W |    W |    W |    W |    Y |    
| 6 |   W |    W |    W |    W |    W |    W |    W |    W |    W |     
| 5 |   Y |    W |    W |    W |    W |    W |    W |    W |    Y |    
| 4 |   W |    W |    W |    W |    W |    W |    W |    W |    W |   
| 3 |   Y |    W |    W |    W |    W |    W |    W |    W |    Y |   
| 2 |   W |    W |    G |    W |    G |    W |    G |    W |    W |   
| 1 |   W |    W |    W |    W |    W |    W |    W |    W |    W |   
|   |   a |    b |    c |    d |    e |    f |    g |    h |    i | 
- Y - yellow
- W - white
- G - green

## Target Map:
| 9 |    |     |    1 |    |    4 |     |    7 |     |     |   
|:---------:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 8 |    |     |      |    |      |     |      |     |     |     
| 7 |  3 |     |      |    |      |     |      |     |  6  |     
| 6 |    |     |      |    |      |     |      |     |     |       
| 5 |  2 |     |      |    |      |     |      |     |  5  |         
| 4 |    |     |      |    |      |     |      |     |     |       
| 3 |  1 |     |      |    |      |     |      |     |  9  |        
| 2 |    |     |      |    |      |     |      |     |     |      
| 1 |    |     |      |    |      |     |      |     |     |       
|   |  a  |  b   |  c    | d   |   e   |  f   |   g   |  h   |  i   |       
            
## Commands:
- FORWARD
- ROTATE "_angel_"
- SETLOAD "_load_"
- THROWLOAD

## Example you can see in file _evens.log_. This file is created by command:
``` bash
python main.py 
```