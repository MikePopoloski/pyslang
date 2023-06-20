from pyslang import *


def test_ast_visitor_single_counting_of_statements():
    """
    Test the visitor interface in pyslang using a port of slang's
    tests/unittests/VisitorTests.cpp:"Test single counting of statements".
    """

    tree = SyntaxTree.fromText(
        """
module m;
    int j;
    initial begin : asdf
        j = j + 3;
        if (1) begin : baz
            static int i;
            i = i + 2;
            if (1) begin : boz
                i = i + 4;
            end
        end
    end
endmodule
    """
    )

    class Visitor:
        def __init__(self):
            self.count = 0

        def visit(self, node):
            if isinstance(node, Statement):
                self.count += 1

    c = Compilation()
    c.addSyntaxTree(tree)
    v = Visitor()
    c.getRoot().visit(v.visit)
    assert v.count == 11
