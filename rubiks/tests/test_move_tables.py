# rubiks/tests/test_move_tables.py
import numpy as np
from rubiks.core.tables import MOVES
from rubiks.core.cube import Cube
from rubiks.view.net_ascii import show_net

def test_move_cycles():
    cube = Cube()
    state0 = cube.state.copy()
    print("Initial solved cube:")
    show_net(cube)
    cube.move('U')
    print("After U (top face clockwise):")
    show_net(cube)
    cube.move("U'")
    print("After U' (revert):")
    show_net(cube)
    assert np.array_equal(cube.state, state0), "U then U' should revert to solved"
    cube = Cube()  # Reset
    cube.move('U2')
    print("After U2 (180°):")
    show_net(cube)
    cube.move('U2')
    print("After U2 twice (revert):")
    show_net(cube)
    assert np.array_equal(cube.state, state0), "U2 twice should revert"

def test_long_sequence():
    cube = Cube()
    sequence = "U R F U' R' F'"
    print("Initial solved cube:")
    show_net(cube)
    for move in sequence.split():
        cube.move(move)
        print(f"After {move}:")
        show_net(cube)
    cube.move('U2')
    print("After final U2 (should not fully revert):")
    show_net(cube)
    assert not np.array_equal(cube.state, Cube().state), "Long sequence should not revert to solved"

if __name__ == "__main__":
    test_move_cycles()
    test_long_sequence()
    print("Move tables test passed!")