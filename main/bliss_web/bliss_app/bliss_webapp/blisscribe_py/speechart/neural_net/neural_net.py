"""
NEURAL NET:

    A data structure for graphs with multiple
    incoming/outgoing edges.
"""


class NeuralNet():
    """
    Initializes a NeuralWebGame with these nodes and constructs a
    net consisting of these nodes.
    ~
    If input to blissweb parameter is a BlissWeb, it is initialized
    as this NeuralNet's blissweb.  Otherwise, blissweb is None.

    :param nodes: List[NeuralNode], nodes to become part of this net
    :param blissweb: Optional[BlissWeb], Blissymbols web parent for this net
    """
    def __init__(self, nodes=list(), blissweb=None):
        self.nodes = nodes  # list of NeuralNodes
        self.node_no = 0
        self.net = None
        self.web = None
        self.layers = None
        self.blissweb = None
        self.init_blissweb(blissweb)
        self.init_nets()

    def init_blissweb(self, blissweb):
        """
        If this NeuralNet's blissweb is None, initializes
        self.blissweb to input blissweb.

        :param blissweb: Optional[BlissWeb], BlissWeb to set as blissweb
        :return: None
        """
        if self.blissweb is None:
            self.blissweb = blissweb

    def init_nets(self):
        """
        Initializes this NeuralNet's net, web, and layers
        according to its nodes.

        :return: None
        """
        self.net = self.create_net(self.nodes)
        self.web = self.spin_web(self.net)
        layers = self.layer_nodes(self.root_nodes(self.nodes))
        print "LAYERS:", layers
        self.layers = layers

    def root_nodes(self, nodes):
        if len(nodes) != 0:
            min_ins = len(min(nodes, key=lambda n: len(n.incoming)).incoming)
        else:
            min_ins = 0
        return [node for node in nodes if len(node.incoming) == min_ins]

    def add_node(self, node):
        """
        Adds this NeuralNode to nodes and re-initializes
        its nets accordingly.

        :param node: NeuralNode, node to add to nodes
        :return: None
        """
        self.nodes.append(node)
        self.init_nets()

    def add_nodes(self, nodes):
        """
        Adds these NeuralNodes to nodes and re-initializes
        its nets accordingly.

        :param nodes: List[NeuralNode], node to add to nodes
        :return: None
        """
        self.nodes.extend(nodes)
        self.init_nets()

    def set_nodes(self, nodes):
        """
        Sets this NeuralNet's nodes to input nodes and
        re-initializes its nets accordingly.

        :param nodes: List[NeuralNode], nodes to set nodes to
        :return: None
        """
        self.nodes = nodes
        self.init_nets()

    def create_node(self, label, outgoing=list()):
        """
        Returns a NeuralNode with this label and outgoing nodes.

        :param label: str, node's label
        :param outgoing: List[NeuralNode], node's outgoing nodes
        :return: NeuralNode, node with label and outgoing nodes
        """
        nn = NeuralNode(label)
        nn.set_outgoing(outgoing)
        return nn

    def add_outgoing(self, node, outgoing):
        """
        Adds outgoing to this NeuralNode's outgoing nodes.

        :param node: NeuralNode, node in this net to add outgoing to
        :param outgoing: List[NeuralNode], outgoing NeuralNodes
        :return: None
        """
        node.set_outgoing(outgoing)

    def create_net(self, nodes, reverse=False):
        """
        Returns a dictionary representing each NeuralNode in
        nodes.
        ~
        If reverse is True, keys are ints and values are
        NeuralNodes. Else, keys are NeuralNodes and values ints.

        :param nodes: List[NeuralNode], nodes to create net for
        :param reverse: bool, whether to reverse keys
        :return: dict(NeuralNode, int), where...
            key (NeuralNode) - NeuralNode with state number
            val (int) - state number for this node
        """
        net = dict()
        self.node_no = 0

        for node in nodes:
            node_no = self.new_node_number()
            if reverse:
                net[node_no] = node
            else:
                net[node] = node_no
        return net

    def find_incoming(self, node, net):
        """
        Returns a list of NeuralNodes for which
        this node is outgoing.

        :param node: NeuralNode, node to find incoming nodes for
        :param net: dict(NeuralNode, int), where...
            key (NeuralNode) - NeuralNode with state number
            val (int) - state number for this node
        :return: List[NeuralNode], incoming nodes for this node
        """
        return [n for n in net if node in n.outgoing]

    def spin_web(self, net):
        """
        From a dictionary of state numbers and nodes,
        transforms the dictionary into a web.

        :param net: dict(NeuralNode, int), where...
            key (NeuralNode) - NeuralNode with state number
            val (int) - state number for this node
        :return: dict(NeuralNode, 2-tuple), where...
            key (NeuralNode) - a node in this network
            val (2-tuple) - in and out NeuralNodes sets for this node
        """
        web = dict()
        new_set = lambda: (set(), set())

        for node in net:
            node_out = node.outgoing
            web.setdefault(node, new_set())
            web[node][0].update(self.find_incoming(node, net))
            web[node][1].update(node_out)

        return web

    def layer_node(self, node):
        """
        From this node, returns a list of its layers of outgoing nodes.

        :param node: NeuralNode, NeuralNodes in a network
        :return: List[list], layers of NeuralNodes in this network
        """
        layers = [[node]]
        seen = set(layers)

        outs = node.outgoing[:]
        print "\nNODE:", node
        print "\tOUTS:", outs
        print "\tSEEN:", seen

        for i in range(len(outs)):
            out = node.outgoing[i]
            if out not in seen:
                seen.add(out)
            else:
                outs.remove(out)

        if len(outs) != 0:
            layer = self.layer_node(out) #self.layer_node(outs)
            layers.extend(layer)

        print "layers:", layers
        return layers

    def layer_nodes(self, nodes):
        """
        From this list of nodes, returns a list of
        node layers sorted by numbers of incoming and outgoing nodes.

        :param nodes: List[NeuralNode], NeuralNodes in a network
        :return: List[list], layers of NeuralNodes in this network
        """
        layers = list()
        seen = set(nodes)

        def layer_subnodes(subnodes):
            if len(subnodes) == 0:
                return list()
            else:
                sublayers = [subnodes]

                for subnode in subnodes:
                    outs = subnode.outgoing[:]
                    print "\nNODE:", subnode
                    print "\tOUTS:", outs
                    print "\tSEEN:", seen

                    # if largest node incoming to each outgoing node is
                    # subnode, keep it on this layer

                    # otherwise push it to above layer

                    for i in range(len(outs)):
                        out = subnode.outgoing[i]
                        if out not in seen and subnode == max(out.incoming, key=self.find_node_number):
                            seen.add(out)
                        else:
                            outs.remove(out)

                    if len(outs) != 0:
                        layer = layer_subnodes(outs)
                        sublayers.extend(layer)

                return sublayers

        layers.extend(layer_subnodes(nodes))
        print "layers:", layers
        return layers

    def find_node_number(self, node):
        """
        Returns this node's state number in the net.

        :param node: NeuralNode, node in net
        :return: int, this node's state number
        """
        return self.net[node]

    def find_nodes_numbers(self, nodes):
        """
        Returns a set of state numbers for these nodes.

        :param nodes: Set(NeuralNode), node in net
        :return: Set(int), this node's state number
        """
        return {self.net[node] for node in nodes}

    def find_node_cxns(self, node):
        """
        Returns a 2-tuple of this node's incoming-outgoing
        connections to other NeuralNodes.

        :param node: NeuralNode, node to find connections for
        :return: 2-tuple, incoming-outgoing node connections
        """
        return self.web[node]

    def find_node_transitions(self, node):
        """
        Returns a 2-tuple of this node's incoming-outgoing
        transitions to other state numbers.

        :param node: NeuralNode, node to find transitions for
        :return: 2-tuple, incoming and outgoing transitions for node
        """
        node_cxns = self.find_node_cxns(node)
        incoming = sorted(self.find_nodes_numbers(node_cxns[0]))
        outgoing = sorted(self.find_nodes_numbers(node_cxns[1]))
        states = (incoming, outgoing)
        return states

    def new_node_number(self):
        """
        Returns this NeuralWebGame's node_no and increments by 1.

        :return: int, number for a node
        """
        node_no = self.node_no
        self.node_no += 1
        return node_no

    def __iter__(self):
        return iter(self.nodes)


class NeuralNode():
    """
    Represents a node in a NeuralNet.
    ~
    N.B. Init parameter 'label' can be any type,
    e.g. int (1), str ("one"), or even a custom type,
    e.g. Blissymbol("life").

    :param label: X, label for this NeuralNode
    """
    def __init__(self, label):
        self.label = label
        self.outgoing = list()  # outgoing connections
        self.incoming = list()  # incoming connections
        self.connections = list()
        self.num = None

    def add_outgoing(self, node):
        """
        Adds outgoing NeuralNode to this NeuralNode's
        outgoing NeuralNodes.

        :param node: NeuralNode, outgoing node to add
        :return: None
        """
        if node not in self.outgoing:
            self.outgoing = self.outgoing[:] + [node]
        if self not in node.incoming:
            node.add_incoming(self)

    def extend_outgoing(self, nodes):
        """
        Adds all NeuralNodes in nodes list to this
        NeuralNode's outgoing NeuralNodes.

        :param nodes: List[NeuralNode], outgoing nodes to add
        :return: None
        """
        #self.outgoing = self.outgoing[:] + nodes
        for node in nodes:
            self.add_outgoing(node)
            #if self not in node.incoming:
            #    node.add_incoming(self)

    def set_outgoing(self, nodes):
        """
        Sets this NeuralNode's outgoing list to this
        list of NeuralNodes.

        :param nodes: List[NeuralNode], nodes to set outgoing to
        :return: None
        """
        self.outgoing = nodes
        for node in nodes:
            if self not in node.incoming:
                node.add_incoming(self)

    def empty_outgoing(self):
        """
        Sets this NeuralNode's outgoing nodes to an empty list.

        :return: None
        """
        self.outgoing = list()

    def add_incoming(self, node):
        """
        Adds incoming NeuralNode to this NeuralNode's
        incoming NeuralNodes.

        :param node: NeuralNode, incoming node to add
        :return: None
        """
        if node not in self.incoming:
            self.incoming = self.incoming[:] + [node]
        if self not in node.outgoing:
            node.add_outgoing(self)

    def extend_incoming(self, nodes):
        """
        Adds all NeuralNodes in nodes list to this
        NeuralNode's incoming NeuralNodes.

        :param nodes: List[NeuralNode], incoming nodes to add
        :return: None
        """
        #self.incoming = self.incoming[:] + nodes
        for node in nodes:
            self.add_incoming(node)
            #if self not in node.outgoing:
            #    node.add_outgoing(self)

    def set_incoming(self, nodes):
        """
        Sets this NeuralNode's incoming list to this
        list of NeuralNodes.

        :param nodes: List[NeuralNode], nodes to set incoming to
        :return: None
        """
        self.incoming = nodes
        for node in nodes:
            if self not in node.outgoing:
                node.add_outgoing(self)

    def empty_incoming(self):
        """
        Sets this NeuralNode's incoming nodes to an empty list.

        :return: None
        """
        self.incoming = list()

    def all_connections(self):
        """
        Returns a set of this NeuralNode's incoming
        and outgoing NeuralNodes.

        :return: Set(NeuralNode), this node's incoming and
            outgoing nodes
        """
        return set(self.incoming + self.outgoing)

    def __eq__(self, other):
        return self.label == other.label

    def __hash__(self):
        return hash(self.label)

    def __str__(self):
        return self.label

    def __repr__(self):
        return str(self)


