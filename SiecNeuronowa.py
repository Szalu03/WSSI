import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.bias = bias
        if weights is not None:
            self.weights = np.array(weights)
        else:
            self.weights = np.random.rand(n_inputs)

    def _activation_function(self, x):
        return max(x * .1, x)

    def __call__(self, inputs):
        return self._activation_function(inputs @ self.weights + self.bias)

class Layer:
    def __init__(self, n_neurons, n_inputs_per_neuron, layer_name, bias=0.):
        self.layer_name = layer_name
        self.neurons = [Neuron(n_inputs_per_neuron, bias=bias) for _ in range(n_neurons)]

    def propagate(self, inputs):
        print(f"Propagating through {self.layer_name}...")
        return np.array([neuron(inputs) for neuron in self.neurons])

class Network:
    def __init__(self, structure, layer_names):
        self.structure = structure
        self.layers = [Layer(structure[i], structure[i - 1], layer_names[i]) for i in range(1, len(structure))]

    def propagate(self, inputs):
        for layer in self.layers:
            inputs = layer.propagate(inputs)
        return inputs

    def visualize(self):
        G = nx.DiGraph()
        pos = {}
        node_counter = 0
        color_map = {'input': 'red', 'hidden 1': 'blue', 'hidden 2': 'blue', 'output': 'green'}

        for i, layer_size in enumerate(self.structure):
            for j in range(layer_size):
                G.add_node(node_counter, layer=self.layers[i-1].layer_name if i > 0 else 'input')
                pos[node_counter] = (i, j - layer_size / 2)
                node_counter += 1

        for i in range(len(self.structure) - 1):
            for j in range(self.structure[i]):
                for k in range(self.structure[i + 1]):
                    G.add_edge(sum(self.structure[:i]) + j, sum(self.structure[:i + 1]) + k)

        plt.figure(figsize=(9, 6))
        nx.draw(G, pos, with_labels=False, node_size=5000,
                 node_color=[color_map[data['layer']] for node, data in G.nodes(data=True)], edge_color='gray')

        for node, data in G.nodes(data=True):
            plt.text(pos[node][0], pos[node][1], data['layer'], ha='center', va='center', fontsize=12,
                     bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

        plt.show()

network_structure = [3, 4, 4, 1]
layer_names = ['input', 'hidden 1', 'hidden 2', 'output']
network = Network(network_structure, layer_names)
network.propagate(np.array([1, 2, 3]))
network.visualize()
