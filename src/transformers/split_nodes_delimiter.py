from models.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter in node.text:
            node_parts = node.text.split(delimiter)
            if len(node_parts) % 2 == 0:
                raise Exception("Error:  ivalid markdown syntax when splitting nodes")

            for i in range(0, len(node_parts)):
                if i % 2 == 1 and i < len(node_parts) - 1:
                    new_nodes.append(TextNode(node_parts[i], text_type))
                    continue
                new_nodes.append(TextNode(node_parts[i], TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes
