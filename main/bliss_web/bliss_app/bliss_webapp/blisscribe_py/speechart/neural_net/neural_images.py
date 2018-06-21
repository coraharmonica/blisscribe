# coding: utf-8
"""
NEURAL_IMAGES:

    Used to produce images of NeuralNets and NeuralNodes.
"""
from neural_net import *
from main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.speechart.blissweb import *


class NeuralNetImage(NeuralNet):
    NODE_RADIUS = 20
    
    def __init__(self, nodes, blissweb=None):
        NeuralNet.__init__(self, nodes, blissweb)

    def create_neural_node_image(self, label, x, y):
        """
        Returns a NeuralNodeImage with this label, x, and y.

        :param label: Any, any type to store info for this node
        :param x: int, x-coordinate in web
        :param y: int, y-coordinate in web
        :return: NeuralNodeImage, with this label, x, and y as inputs
        """
        return NeuralNodeImage(label, x, y)

    def node_to_neural_node_image(self, node, x, y):
        """
        Returns a NeuralNodeImage with node's label, x, and y.

        :param node: NeuralNode, holding label for NeuralNodeImage
        :param x: int, x-coordinate in web
        :param y: int, y-coordinate in web
        :return: NeuralNodeImage, with node's label, x, and y as inputs
        """
        return self.create_neural_node_image(node.label, x, y)

    def nodes_to_neural_node_images(self, nodes):
        """
        Returns a list of NeuralNodeImages with each node's label.
        ~
        N.B. Nodes, x_vals, and y_vals must all be of the same length.
        Every NeuralNodeImage needs a corresponding x and y value in a web.

        :param nodes: List[NeuralNode], holding labels for NeuralNodeImages
        :return: List[NeuralNodeImage], with nodes' labels and paired x and y
        """
        node_imgs = list()
        x_vals = self.nodes_x_vals(nodes)
        y_vals = self.nodes_y_vals(nodes)

        for i in range(len(nodes)):
            node = nodes[i]
            x = x_vals[i]
            y = y_vals[i]
            print node, x, y
            node_img = self.create_neural_node_image(node.label, x, y)
            node_imgs.append(node_img)

        return node_imgs

    def draw_web(self):
        for layer in self.layers:
            self.draw_layer(layer)
        neural_node_imgs = self.nodes_to_neural_node_images(self.nodes)
        print neural_node_imgs
        return neural_node_imgs

    def item_in_layers(self, item):
        return [layer for layer in self.layers if item in layer]

    def item_in_layer(self, item):
        return self.item_in_layers(item)[0] if len(self.item_in_layers(item)) != 0 else list()

    def node_x_val(self, node):
        layer = self.item_in_layer(node)
        x_val = (layer.index(node)+1) * self.NODE_RADIUS * 2
        return x_val

    def node_y_val(self, node):
        layer = self.item_in_layer(node)
        y_val = (self.layers.index(layer)+1) * self.NODE_RADIUS * 2
        return y_val

    def nodes_x_vals(self, nodes):
        x_vals = list()
        for i in range(len(nodes)):
            x_val = self.node_x_val(nodes[i])
            x_vals.append(x_val)
        return x_vals

    def nodes_y_vals(self, nodes):
        y_vals = list()
        for i in range(len(nodes)):
            y_val = self.node_y_val(nodes[i])
            y_vals.append(y_val)
        return y_vals

    def draw_layers(self):
        img = make_blank_img(0, 0, opacity=0)
        between_img = make_blank_img(1, self.NODE_RADIUS*2, opacity=0)
        for layer in self.layers:
            img = above(img, between_img)
            img = above(img, self.draw_layer(layer))
        img.show()
        return img

    def draw_layer(self, layer, arrows=True):
        layer_imgs = [self.node_img(node, arrows=arrows) for node in layer]
        img = beside_all(layer_imgs, space=self.NODE_RADIUS*2)
        return img

    def node_img(self, node, arrows=True):
        if self.blissweb is not None:
            img = self.blissweb.node_img(node)
        else:
            node_num = self.find_node_number(node)
            num_text = text_image(str(node_num))
            circ = circle(self.NODE_RADIUS, outline='black')
            img = overlay(num_text, circ)

        print "MAKING NODE IMAGE FOR", node, node.outgoing
        if arrows:
            arros = list()
            num_arrows = len(node.outgoing)
            angle = 0
            addn = int(90.0/num_arrows) if num_arrows != 0 else 0
            lswing = True
            for i in range(num_arrows):
                if lswing:
                    angle -= addn
                else:
                    addn = 2*addn
                    angle += addn
                lswing = not lswing
                arro = arrow(width=2, height=self.NODE_RADIUS*2, angle=angle, fill='black')
                arros.append(arro)
                print "ANGLE:", angle
                #print "ARROWS:", arros
            arros_img = beside_all(arros)
            img = above(img, arros_img)

        return img


class NeuralNodeImage(NeuralNode):
    def __init__(self, label, x, y):
        NeuralNode.__init__(self, label)
        self.x = x
        self.y = y

    def create_image(self, node_radius):
        return circle(node_radius, outline='black')

