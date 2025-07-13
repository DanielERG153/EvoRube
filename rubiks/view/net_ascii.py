PALETTE=['\033[47m','\033[41m','\033[42m','\033[43m','\033[45m','\033[44m']; RESET='\033[0m'
def show_net(cube):
    s=cube.state.reshape(6,9)
    def row(f,r): return ''.join(f'{PALETTE[s[f,3*r+c]]}  {RESET}' for c in range(3))
    for r in range(3): print('      '+row(0,r))
    for r in range(3): print(''.join(row(f,r) for f in (4,2,1,5)))
    for r in range(3): print('      '+row(3,r))