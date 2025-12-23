class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        string_props = []
        for key in self.props.keys():
            string_props.append(f' {key}="{self.props[key]}"')
        html_props = "".join(string_props)
        return html_props

    def __repr__(self) -> str:
        string_repr = f"HTMLNode({self.tag}, {self.value}, children: {self.children}"
        if self.props:
            string_repr += f",{self.props_to_html()}"
        return string_repr + ")"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Error: all leaf nodes must have a value")
        if not self.tag:
            return f"{self.value}"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        string_repr = f"LeafNode({self.tag}, {self.value}"
        if self.props:
            string_repr += f",{self.props_to_html()}"
        return string_repr + ")"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Error: parentnode must have tag")
        if not isinstance(self.children, list):
            raise ValueError("Error: parent node must have list of children nodes")
        if len(self.children) < 1:
            raise ValueError("Error: list of children is empty")
        return f"<{self.tag}{self.props_to_html()}>{"".join(list(map(lambda child: child.to_html(), self.children)))}</{self.tag}>"

    def __repr__(self) -> str:
        string_repr = f"ParentNode({self.tag}, children: {self.children}"
        if self.props:
            string_repr += f",{self.props_to_html()}"
        return string_repr + ")"

