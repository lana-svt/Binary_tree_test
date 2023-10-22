from hypothesis import strategies as st
from hypothesis import given

from proekt import Node, node_height, node_size, node_sum
@st.composite
def binary_tree(draw, min_value=0, max_depth=5):
    value = draw(st.integers(min_value=min_value))
    if max_depth == 0:
        return Node(value)
    left = draw(binary_tree(min_value, max_depth - 1))
    right = draw(binary_tree(min_value, max_depth - 1))
    return Node(value, left, right)

#Тестирование свойства высоты дерева
@given(tree=binary_tree())
def test_height_size(tree):
    assert node_height(tree) >= 0 # Высота всегда должна быть больше или равна 0

#Тестирование свойства размера дерева
@given(tree=binary_tree())
def test_size_property_null(tree):
    assert node_size(tree) >= 0 # Размер всегда должен быть больше или равен 0

# Проверка, что сумма значений в дереве больше или равна 0
@given(binary_tree())
def test_node_sum_null(node):
    assert node_sum(node) >= 0

#Тест для проверки, что сумма значений всех узлов правильная
@given(node=binary_tree())
def test_node_sum(node):
    sum_value = node_sum(node)
    expected_sum = calculate_tree_sum(node)
    assert sum_value == expected_sum

# Функция для вычисления суммы значений всех узлов в дереве
def calculate_tree_sum(node):
    if node is None:
        return 0
    return node.value + calculate_tree_sum(node.left) + calculate_tree_sum(node.right)

# Тест для проверки, что высота дерева не превосходит 2^n - 1
@given(tree=binary_tree())
def test_height_property(tree):
    height = node_height(tree)
    assert height <= 2 ** height - 1

# Тест для проверки, что размер дерева считается правильно
@given(tree=binary_tree())
def test_size_property(tree):
    size = node_size(tree)
    expected_size = count_nodes(tree)
    assert size == expected_size

# Функция для подсчета количества узлов в дереве
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Тест для проверки, что все значения в дереве неотрицательные
@given(node=binary_tree())
def test_non_negative_values(node):
    assert check_non_negative(node)

def check_non_negative(node):
    if node is None:
        return True
    if node.value < 0:
        return False
    return check_non_negative(node.left) and check_non_negative(node.right)


# Проверка, что высота дерева считается правильно
@given(binary_tree())
def test_node_height_correct(node):
    def calculate_height(node):
        if node is None:
            return 0
        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)
        assert node_height(node) == max(left_height, right_height) + 1
        return 1 + max(left_height, right_height)
    calculate_height(node)


# Тест для проверки, что сумма значений в пустом дереве равна 0
def test_empty_tree_sum():
    empty_tree = Node(0)
    assert node_sum(empty_tree) == 0