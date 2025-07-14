# rubiks/tests/test_turns.py
from rubiks.core.cube import Cube
from rubiks.view.net_ascii import show_net

def test_turns():
    cube = Cube()
    print("Initial solved cube:")
    show_net(cube)
    moves = ['U', 'U\'', 'U2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'D', 'D\'', 'D2', 'L', 'L\'', 'L2', 'B', 'B\'', 'B2']
    for move in moves:
        cube.move(move)
        print(f"After {move}:")
        show_net(cube)
        # Reverse to back
        reverse = move.replace("2", "") + "'" if '2' not in move else move.replace("2", "")
        reverse = reverse.replace("''", "") if "''" in reverse else reverse
        if '2' in move:
            reverse = move
        cube.move(reverse)
        print(f"After reverse {reverse} (should revert):")
        show_net(cube)

if __name__ == "__main__":
    test_turns()
    print("Turn test complete!")