class Stack():
    def __init__( self ):
        self.stack = []

    def push( self, value ):
        self.stack.append( value )

    def pop( self ):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size( self ):
        return len( self.stack )

def dfs( starting_vertex, graph ):
        stack   = Stack()
        visited = []

        stack.push( [ starting_vertex ] )

        while stack.size():
            path = stack.pop()
            node = path[ -1 ]

            if node not in visited:
                visited.append( node )

            for parent in graph.get( node, [] ):
                stack.push( path + [ parent ] )
        
        return visited[ -1 ]

def earliest_ancestor( ancestors, starting_node ):
    graph = {}

    for parent, child in ancestors:
        if child not in graph:
            graph[ child ] = [ parent ]
        else:
            graph[ child ].append( parent )
    
    if starting_node not in graph:
        return -1

    return dfs( starting_node, graph )\
