from random import shuffle


class Queue():
    def __init__( self ):
        self.que = []

    def enqueue( self, value ):
        self.que.append( value )

    def dequeue( self ):
        if self.size() > 0:
            return self.que.pop( 0 )
        else:
            return None

    def size( self ):
        return len( self.que )


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for u in range( num_users ):
            self.add_user( u )

        # Create friendships
        friends = []
        
        for uid in self.users:
            for fid in range( uid + 1, self.last_id + 1 ):
                friends.append( ( uid, fid ) )

        shuffle( friends )

        rng = num_users * avg_friendships // 2
        for i in range( rng ):
            uid, fid = friends[ i ]
            self.add_friendship( uid, fid )

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        que = Queue()

        que.enqueue( [ user_id ] )

        while que.size():
            path = que.dequeue()
            node = path[ -1 ]

            if node not in visited:
                visited[ node ] = path

                friends = self.friendships[ node ]

                for friend in friends:
                    que.enqueue( path + [ friend ] )

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
