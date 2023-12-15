from Cell import Cell
class Field:
    """
    Field object
    It contains a list of cells. Its description can be loaded from a file.
    Each line of the file contains information to create each cell: coordinate, color, target, located object and neighboring cells.
    For example, the string for cell "a1" is: a1 w 0 None a2 None None b1
    """
    def __init__(self, size, file_for_field_name) -> None:
        self.size = size
        self.__load_from_file(file_for_field_name)
        self.repr_cells = [[self.get_cells_by_coordinate(chr(i)+str(j))[0] 
                       for i in range(97,97+self.size)] for j in range(self.size, 0, -1)]
        
    def get_cells_by_coordinate(self, *coordinates):
        res = []
        for c in coordinates:
            if c == 'None':
                res.append(None)
            else:
                res = res + list(filter(lambda cell: cell.coordinate == c, self.cells))
        return res
    
    def get_cells_by_color(self, color):
        return list(filter(lambda cell: cell.color == color, self.cells))
    
    def get_cells_by_target(self, target):
        return list(filter(lambda cell: cell.target == target, self.cells))
    
    def __load_from_file(self, file):
        self.cells = []
        with open(file, 'r') as f:
            text = f.read().split('\n')
        for cell_datas in text:
            self.cells.append(Cell(*cell_datas.split()[:3]))
        for cell, cell_datas in list(zip(self.cells, text)):
            cell.set_adj(*self.get_cells_by_coordinate(*cell_datas.split()[4:]))
   
    def BFS(self, src, dest, cannot_step, pred, dist):
        v = self.size**2
        queue = []
        visited = [False for i in range(v)]
        for i in range(v):
            dist[i] = 1000000
            pred[i] = Cell('none')
        visited[self.cells.index(src)] = True
        dist[self.cells.index(src)] = 0
        queue.append(src)
        while (len(queue) != 0):
            u = queue[0]
            queue.pop(0)
            for adj in u.adj:
                if (visited[self.cells.index(adj)] == False) and adj not in cannot_step:
                    visited[self.cells.index(adj)] = True
                    dist[self.cells.index(adj)] = dist[self.cells.index(u)] + 1
                    pred[self.cells.index(adj)] = u
                    queue.append(adj)
                    if (adj == dest):
                        return True
        return False
    
    def shortest_path(self, s, dest, cannot_step):
        v = self.size**2
        pred=[0 for i in range(v)]
        dist=[0 for i in range(v)]
    
        if (self.BFS(s, dest, cannot_step, pred, dist) == False):
            return [1 for i in range(100)]
    
        path = []
        crawl = dest
        path.append(crawl)
        
        while (pred[self.cells.index(crawl)] != Cell('none')):
            path.append(pred[self.cells.index(crawl)])
            crawl = pred[self.cells.index(crawl)]
        path.reverse()
        return path

    def print_field(self):
        for ele in self.repr_cells:
            for cell in ele:
                print(cell, end = '   ')
            print('\n')