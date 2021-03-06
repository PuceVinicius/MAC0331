# -*- coding: utf-8 -*-

"""Algoritmos para o Problema do Fecho Convexo:

Dado um conjunto de pontos, determinar o seu fecho convexo.

Algoritmos disponiveis:
- Graham
- Embrulho Para Presente
- Quick Hull
- Incremental Probabilistico
- Merge Hull
- Um algoritmo otimo proposto por Chan
- Um algoritmo otimo proposto por Bhattacharya e Sen

algoritmo otimo = executa em tempo O(n lg(h)), n = numero de pontos, 
                                               h = numero de arestas no fecho
"""
from . import graham
from . import gift
from . import quickhull
from . import incremental
from . import incr_prob
from . import mergehull
from . import chan
from . import bhatta_sen

# cada entrada deve ter:
#  [ 'nome-do-modulo', 'nome-da-funcao', 'nome do algoritmo' ]
children = ( 
	( 'graham', 'Graham', 'Graham' ),
	( 'gift', 'Gift', 'Embrulho\nPara Presente' ),
	( 'quickhull', 'Quickhull', 'Quickhull' ),
	( 'incremental', 'Incremental', 'Incremental' ),
	( 'incr_prob', 'IncrProb', 'Incremental\nProbabilistico' ),
	( 'mergehull', 'Mergehull', 'Mergehull' ),
	( 'chan', 'Chan', 'Chan' ),
	( 'bhatta_sen', 'Bhatta_Sen', 'Bhattacharya\nSen')

)

#children = algorithms

#__all__ = [ 'graham', 'gift' ]
__all__ = [a[0] for a in children]
