from blisschart import *
from neural_net.neural_net import NeuralNet


class BlissWeb(BlissChart):
    """
    A class for graphing semantics in Blissymbols as a web.
    ~
    Each web has a maximum number of outgoing/incoming connections
    between nodes (e.g. 2).
    ~
    BlissChart takes text_image as input and can visualize graphs
    of Blissymbols.
    ~
    - Language is input in words.
    - Blissymbols are internally represented by 4-digit unicode IDs.
    - Graphs are visualized in Blissymbol characters.
    """
    def __init__(self, language="English"):
        BlissChart.__init__(self, language)
        self.connections = dict()
        self.neural_net = NeuralNet(blissweb=self)

    def add_node(self, label, outgoing):
        node = self.neural_net.create_node(label, outgoing)
        self.neural_net.add_node(node)

    def add_state(self, state, label, incoming=set(), outgoing=set()):
        self.states.add(state)
        self.add_state_label(state, label)
        self.add_incoming(state, incoming)
        self.add_outgoing(state, outgoing)

    def add_state_label(self, state, label):
        state_cxn = self.connections.setdefault(state, dict())
        state_cxn["label"] = label

    def add_state_labels(self, state, labels):
        state_cxn = self.connections.setdefault(state, dict())
        state_cxn.setdefault("label", set())
        state_cxn["label"].update(labels)

    def add_incoming(self, state, incoming):
        state_cxn = self.connections.setdefault(state, dict())
        state_cxn.setdefault("in", set())
        state_cxn["in"].update(incoming)

    def add_outgoing(self, state, outgoing):
        state_cxn = self.connections.setdefault(state, dict())
        state_cxn.setdefault("out", set())
        state_cxn["out"].update(outgoing)

    def add_connection(self, label, incoming=set(), outgoing=set()):
        state = self.new_state()
        self.add_state(state, label, incoming, outgoing)

    def state_connections(self, state):
        """
        Returns a dictionary of all destination states for the given state.

        :param state: int, state number to return destinations for
        :return: dict[int, Set], all destinations for this state
        """
        state_connections = [c for c in self.connections if c == state]
        destinations = dict()

        for statechar in state_connections:
            dests = self.connections[statechar]["out"]
            labels = self.connections[statechar]["label"]
            for dest in dests:
                destinations.setdefault(dest, set())
                destinations[dest].update(labels)

        return destinations

    def state_transitions(self, state):
        """
        Returns a dictionary of all destination states for the given state.

        :param state: int, state number to return destinations for
        :return: dict[int, Set], all destinations for this state
        """
        transitions = set()
        for s in self.state_connections(state).values():
            transitions.update(s)
        return transitions

    def state_outgoing_labels(self, state):
        """
        Returns a dictionary of all destination states for the given state.

        :param state: int, state number to return destinations for
        :return: dict[int, Set], all destinations for this state
        """
        labels = self.state_connections(state)
        label_dict = {label: self.beside_all(labels[label], mini=True) for label in labels}
        return label_dict

    def find_incoming(self, node):
        return self.neural_net.find_incoming(node, self.neural_net.net)

    def node_img(self, node, selected=False):
        blissymbol = self.blissword_blissymbol(node.label)
        circ = self.state_circle("")
        if selected:
            bg_circ = circle(circ.width+2, circ.height+2, outline="grey")
            circ = overlay(circ, bg_circ)
        bliss_img = self.bliss_image(blissymbol)
        img = overlay(bliss_img, circ)
        return img

    def shortest_path(self, node1, node2):
        """
        Returns the shortest path of NeuralNodes from NeuralNode node1
        to NeuralNode node2.
        ~
        If node1 and node2 are equal, finds the shortest cycle from
        node1 back to itself.
        ~
        Performs a breadth-first recursive search for node2 on node1's
        outgoing nodes and each their children.

        :param node1: NeuralNode, start node
        :param node2: NeuralNode, destination node
        :return: List[NeuralNode], nodes in path from node1 to node2
        """
        seen = {node1}
        goal_paths = list()

        def below_min_path(p): return len(goal_paths) == 0 or len(p) < len(goal_paths[0])

        def short_path(node, path):
            # TODO: make this a more effective breadth-first search!
            p = path[:]
            p.append(node)

            if below_min_path(p):
                if node2 in node.outgoing:
                    p.append(node2)
                    if below_min_path(p):
                        goal_paths.insert(0, p)
                else:
                    for nd in node.outgoing:
                        if nd not in seen or node2 in nd.outgoing:
                            short_path(nd, p)
                            seen.add(nd)

        short_path(node1, path=list())

        if len(goal_paths) != 0:
            return goal_paths[0]

    def longest_path(self, node1, node2=None):
        """
        Returns the longest path of NeuralNodes from NeuralNode node1
        to NeuralNode node2.
        ~
        If node1 and node2 are equal, finds the longest cycle from
        node1 back to itself.
        ~
        Performs a depth-first recursive search for node2 on node1's
        outgoing nodes and each their children.

        :param node1: NeuralNode, start node
        :param node2: NeuralNode, destination node
        :return: List[NeuralNode], nodes in path from node1 to node2
        """
        seen = {node1}
        goal_paths = list()

        def above_max_path(p): return len(goal_paths) == 0 or len(p) > len(goal_paths[0])

        def long_path(node, path):
            # TODO: make this a more effective depth-first search!
            p = path[:]
            p.append(node)
            print "goal paths:", goal_paths

            if above_max_path(p):
                print "\tpath:", p
                if node2 is None or node2 in node.outgoing:
                    if node2 is not None:
                        p.append(node2)
                    if above_max_path(p):
                        goal_paths.insert(0, p)
                else:
                    for nd in node.outgoing:
                        if nd not in seen:
                            print "\tnode:", nd
                            long_path(nd, p)
                            seen.add(nd)

        long_path(node1, path=list())

        if len(goal_paths) != 0:
            return goal_paths[0]

    def find_cycle(self, start_node):
        """
        Finds the shortest cycle from this node back to itself.

        :param start_node: NeuralNode, node to start/end cycle
        :return: List[NeuralNode], nodes along cycle from start to end
        """
        return self.shortest_path(start_node, start_node)

    def visualize_node(self, node):
        cxn = self.neural_net.find_node_cxns(node)
        outs = list(cxn[1])
        img = self.node_img(node)
        print "cxns:", node.all_connections()
        angle_inc = int(180.0 / len(node.all_connections()))

        for i in range(len(outs)):
            out = outs[i]
            if len(self.neural_net.find_node_cxns(out)[1]) == 0:
                out_img = self.node_img(out)
            else:
                #out_img = self.visualize_node(out)
                out_img = self.node_img(out)
            img = self.connect_states(img, out_img, angle=angle_inc * i, length=100*len(outs))
            # TODO: vary angle by len of shortest path from out back to original node(?)
            #angle += angle_inc
            print angle_inc * i

        return img

    def visualize_connections(self):
        seen = set()
        todo = [self.neural_net.nodes[0]]
        img = self.empty_image()

        while len(todo) != 0:
            node = todo.pop(0)
            if node not in seen:
                node_img = self.visualize_node(node)
                img = beside(img, node_img)
                todo.extend(node.outgoing)
                seen.add(node)

        img.show()
        return img

    def visualize_cycle(self, nodes):
        """
        Visualizes these nodes as a self-contained cycle.

        :param nodes: List[NeuralNode]
        :return: Image
        """
        cycle = self.find_cycle(nodes)
        if cycle is None:
            return
        nodes = cycle
        # angles of a shape always add up to 90 (?)
        angle = 0
        angle_inc = int(180.0/len(nodes))
        pos = True
        nodes_img = self.empty_image()

        for node in nodes:
            node_img = self.visualize_node(node)
            node_img = rotate(node_img, angle)
            nodes_img = beside(nodes_img, node_img)
            angle += angle_inc

            if pos:
                pos = False
            else:
                angle = -angle
                pos = True

        nodes_img.show()
        return nodes_img

