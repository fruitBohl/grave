"""
Grave Documentation
-------------------

"""

import networkx as nx


toy_network = nx.barbell_graph(10, 14)

node_options = {
    "node_color": "royalblue",
    "node_size": 50,
    "edgecolors": "white",
}

edge_options = {
    "line_color": "grey",
    "alpha": 0.7,
}

for node, node_attributes in toy_network.nodes(data=True):
    node_attributes["distance"] = my_compute(toy_network, node)


def protein_style(node_attributes):
    if node_attributes.get("type", "") == "protein":
        return {"color": "blue"}
    else:
        return {"color": "red"}


plot_the_graph(
    toy_network, layout="spring", node_style=protein_style, edge_stlye=edge_options
)
