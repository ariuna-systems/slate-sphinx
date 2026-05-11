from docutils import nodes
from docutils.parsers.rst import Directive


class NotificationBanner(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self) -> list[nodes.Element]:
        self.assert_has_content()
        node = nodes.container(classes=["slate-node"])
        title = nodes.paragraph(text=self.arguments[0], classes=["slate-node__title"])
        node += title
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]
