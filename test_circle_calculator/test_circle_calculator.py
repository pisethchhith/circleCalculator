from circle import radiusCalculation, diameterCalculation, UnitConversion
import pytest

def test_radiuscalculation():
    assert radiusCalculation("1 cm") == 2 * 3.14 * pow(0.01, 2)
    assert radiusCalculation("500 m") == 2 * 3.14 * pow(500, 2)

def test_diameterCalculation():
    assert diameterCalculation("500 m") == (3.14/4) * pow(500, 2)
def test_UnitConversion():
    assert UnitConversion(1, "cm") == 0.01
    assert UnitConversion(500, "km") == 500000.0

def test_string_in_bothCalculation():
    with pytest.raises(ValueError):
        assert radiusCalculation("1c cm")
        assert diameterCalculation("22c cm")

def test_user_put_unit_without_space_in_both_calculation():
    with pytest.raises(ValueError):
        assert radiusCalculation("200cm")
        assert diameterCalculation("3dm")
