from maze import escape
import pytest

# Instance tests
class TestEscape(object):
    def test_0(self):
        maze = ['#####',
                '#@  #',
                '### #']
        assert escape(maze) == True

    def test_1(self):
        maze = ['#####',
                '#@  #',
                '#####']
        assert escape(maze) == False

# Function tests
def test_0():
    maze = ['#####',
            '#@  #',
            '#####']
    assert escape(maze) == False

# Parameterizing tests
mazes = [
    (['#####',
    '#@  #',
    '### #'], True),
    (['#####',
    '#@  #',
    '#####'], False),
]
@pytest.mark.parametrize('maze, expected', mazes)
def test_1(maze, expected):
    assert escape(maze) == expected

    