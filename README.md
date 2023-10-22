# Binary_tree_test
Для всех тестов кроме последнего генерируются бинарные деревья с помощью стратегии для генерации случайных бинарных деревьев.

1. test_height_size:

Тест проверяет свойство, что высота дерева всегда больше или равна 0.

2. test_size_property_null:

Тест проверяет свойство, что размер дерева всегда больше или равен 0.

3. test_node_sum_null:

Тест проверяет, что сумма значений в дереве всегда больше или равна 0.

4.test_node_sum:

Тест проверяет, что функция node_sum возвращает правильную сумму значений всех узлов в дереве.
Он сравнивает сумму значений, возвращенную функцией node_sum, с ожидаемой суммой, вычисленной с помощью функции calculate_tree_sum.

5. test_height_property:

Этот тест также проверяет свойство высоты дерева.
Он генерирует случайное бинарное дерево и проверяет, что высота дерева не превосходит 2^n - 1, где n - это высота дерева.

6. test_size_property:

Этот тест проверяет, что размер дерева, возвращенный функцией node_size, соответствует ожидаемому размеру, вычисленному с помощью функции count_nodes.

7. test_non_negative_values:

Этот тест проверяет, что все значения в дереве неотрицательные.
Он использует функцию check_non_negative, чтобы рекурсивно проверить, что все значения неотрицательные.

8. test_node_height_correct:

Этот тест проверяет, что высота дерева, возвращенная функцией node_height, соответствует ожиданиям.
Он использует рекурсивную функцию calculate_height, чтобы проверить правильность вычисления высоты.

9. test_empty_tree_sum:

Этот тест проверяет, что сумма значений в пустом дереве равна 0.
Он создает пустое дерево с корнем, значение которого равно 0, и затем проверяет, что функция node_sum возвращает 0 для этого дерева.
