import nbformat
import sys
from io import StringIO
from IPython import get_ipython

# Substitui a função input padrão por uma que retorna uma string vazia
original_input = input
def mock_input(*args, **kwargs):
    return "0"

# Função para executar o notebook e obter as funções
def get_function_from_notebook(notebook_path):
    # Substituindo a função input
    global input
    input = mock_input
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        for cell in nb.cells:
            if cell.cell_type == "code":
                exec(cell.source, globals())
    # Restaurando a função input original
    input = original_input

get_function_from_notebook("exercicios/exercicios_busca.ipynb")



# testes para os exercios que precisam ser resolvidos

def test_busca_sequencial():
    result = busca_sequencial([1, 2, 3, 4, 5], 3)
    if result is None:
        raise AssertionError("Função ainda não implementada")
    else:
        assert busca_sequencial([1, 2, 3, 4, 5], 3) == 2
        assert busca_sequencial([1, 2, 3, 4, 5], 6) == -1
        assert busca_sequencial([5, 4, 3, 2, 1], 3) == 2
        assert busca_sequencial([5, 4, 3, 2, 1], 6) == -1
    

def test_busca_binaria():
    result = busca_binaria([1, 2, 3, 4, 5], 3)
    if result is None:
        raise AssertionError("Função ainda não implementada")
    else:
        assert busca_binaria([1, 2, 3, 4, 5], 3) == 2
        assert busca_binaria([1, 2, 3, 4, 5], 6) == -1


def test_busca_binaria_com_contagem():
    result = busca_binaria_com_contagem([1, 2, 3, 4, 5], 3)
    if result is None:
        raise AssertionError("Função ainda não implementada")
    else:
        assert busca_binaria_com_contagem([1, 2, 3, 4, 5], 2) == (2, 2)
        assert busca_binaria_com_contagem([1, 2, 3, 4, 5], 3) == (2, 1)
        assert busca_binaria_com_contagem([1, 2, 3, 4, 5], 6) == -1

