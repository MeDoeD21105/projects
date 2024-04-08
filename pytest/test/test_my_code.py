from my_code import division

import pytest


@pytest.mark.parametrize("a, b, x",[(10, 2, 5),
                                    (50, 25, 2),
                                    (100, 10, 10),
                                    (30, -3, -10),
                                    (10,1,10),
                                    (1, 1, 1)
                                    ])
def test_division_good(a, b, x):
    assert division(a, b) == x
    
    
@pytest.mark.parametrize("expected, a, b",[(ZeroDivisionError,10, 0),
                                          (TypeError, 10, "2"),
])
def test_division_expected(a, b, expected):
    with pytest.raises(expected):
        division(a,b)