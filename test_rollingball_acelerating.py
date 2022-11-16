import pytest
from main import Ball

tests = [(55, 1.2, 9, 155.29), (5, 1, 12, 106.48)]


@pytest.mark.parametrize('acceleration, radius, time, angle', tests)
def speed_test(acceleration, radius, time, angle):
    """Проверяет правильность нахождения угла поворота при равноускоренном движении."""
    assert Ball(0, acceleration, radius, time).find_angle_speed() == angle

# tests = [("как", 9, "Дела?", '-b'), (-6, 9, -1, 15), ([5, 8, 55, ' '])]
# @pytest.mark.xfail(raises = ValueError)
# def test_err_uniform_moving(acceleration, radius, time, angle):
#     with pytest.raises(ValueError):
#         Ball(acceleration, radius, time, angle)
