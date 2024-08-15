from graphs.graph import GNode, DAG
import pytest

from graphs.exceptions import (
    CycleInGraphError,
    NodeAlreadyExistsError,
    NodeNotFoundError,
)


def test_dag_paths():
    a = GNode("a")
    dag = DAG(a)
    b = dag.add_node("b")
    c = dag.add_node("c")
    d = dag.add_node("d")
    e = dag.add_node("e")
    f = dag.add_node("f")
    g = dag.add_node("g")
    h = dag.add_node("h")
    j = dag.add_node("j")

    dag.add_edge("a", "b")
    dag.add_edge("a", "c")
    dag.add_edge("a", "d")
    dag.add_edge("b", "e")
    dag.add_edge("b", "f")
    dag.add_edge("c", "e")
    dag.add_edge("c", "g")
    dag.add_edge("c", "h")
    dag.add_edge("d", "j")

    assert dag.paths() == [
        [a, b, e],
        [a, b, f],
        [a, c, e],
        [a, c, g],
        [a, c, h],
        [a, d, j],
    ]


def test_dag_walk_through():
    a = GNode("a")
    dag = DAG(a)
    b = dag.add_node("b")
    c = dag.add_node("c")
    d = dag.add_node("d")
    e = dag.add_node("e")
    f = dag.add_node("f")
    g = dag.add_node("g")

    dag.add_edge("a", "b")
    dag.add_edge("a", "c")
    dag.add_edge("b", "d")
    dag.add_edge("b", "e")
    dag.add_edge("c", "f")
    dag.add_edge("c", "g")

    assert dag.walk_graph() == [a, b, d, e, c, f, g]


def test_create_cyclic_dag():
    a = GNode("a")
    dag = DAG(a)
    b = dag.add_node("b")
    dag.add_edge("a", "b")
    with pytest.raises(CycleInGraphError) as excinfo:
        dag.add_edge("b", "a")
    assert (
        "Adding this edge would create a cycle, which is not allowed in a DAG."
        in str(excinfo.value)
    )


def test_adding_existing_node():
    a = GNode("a")
    dag = DAG(a)
    with pytest.raises(NodeAlreadyExistsError) as excinfo:
        dag.add_node("a")
    assert "Node with name a already exists in the DAG." in str(excinfo.value)


def test_adding_edge_to_nonexistent_node():
    a = GNode("a")
    dag = DAG(a)
    with pytest.raises(NodeNotFoundError) as excinfo:
        dag.add_edge("a", "b")
    assert "Both nodes must exist in the DAG before adding an edge." in str(
        excinfo.value
    )
