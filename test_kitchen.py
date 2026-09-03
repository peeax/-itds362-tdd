# Test List
# ☐ 200 g × 3 = 600 g
# ☐ multiplication must not change the original object
# ☐ quantities with the same amount and unit are equal
# ☐ 1 oz is not equal to 1 g
# ☐ 200 g + 300 g = 500 g
# ☐ 200 g + 1 oz converts the result to grams
# ☐ (200 g + 1 oz) × 2

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    flour.times(3)
    assert flour.amount == 600