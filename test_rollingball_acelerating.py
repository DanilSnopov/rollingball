import pytest
from main import Ball

tests = [(55, 1.2, 9, 155.29), (5, 1, 12, 106.48)]


@pytest.mark.parametrize('acceleration, radius, time, angle', tests)
def test_speed(acceleration, radius, time, angle):
    """Проверяет правильность нахождения угла поворота при равноускоренном движении."""
    assert Ball(0, acceleration, radius, time).find_angle_acceleration() == angle


@pytest.mark.xfail(raises = ValueError)
def test_err_uniform_moving():
    with pytest.raises(ValueError):
        Ball(-1, "5", 18, "Hello")
