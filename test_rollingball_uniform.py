import pytest
from main import Ball

tests = [(80, 1, 5, 238.31), (60, 66.5, 128, 137.02)]


@pytest.mark.parametrize('speed, radius, time, angle', tests)
def test_speed(speed, radius, time, angle):
    """Проверяет правильность нахождения угла поворота при равномерном движении."""
    assert Ball(speed, 0, radius, time).find_angle_speed() == angle


# tests = [(-1, 0, ValueError), (5, "Привет", 'проверяльщики', -1, ValueError), ([5, 8, 55], ValueError)]
# @pytest.mark.xfail('speed, radius, time, angle, error', tests)
# def test_err_uniform_moving(speed, radius, time):
#     with pytest.raises(ValueError):
#         Ball(speed, radius, time)
