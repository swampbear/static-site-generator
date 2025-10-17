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
            return None

        string_props = []
        for key in self.props.keys():
            string_props.append(f' {key}="{self.props[key]}"')
        html_props = "".join(string_props)
        return html_props

    def __repr__(self) -> str:
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children={self.children}, props={self.props_to_html()})'
