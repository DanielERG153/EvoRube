"""Index cycles for 3×3×3 cube — 18 half-turn-metric moves."""
MOVES={}
# helper to build face cycles quickly
def faces(c):
    return (c,c+2,c+8,c+6),(c+1,c+5,c+7,c+3)
# U(0), R(9), F(18), D(27), L(36), B(45)
UF = [(36,18,9,45),(37,19,10,46),(38,20,11,47)]
RF = [(2,45,27,20),(5,48,30,23),(8,51,33,26)]
FF = [(6,36,27,11),(7,39,28,14),(8,42,29,17)]
DF = [(24,15,33,42),(25,16,34,43),(26,17,35,44)]
LF = [(0,18,27,53),(3,21,30,50),(6,24,33,47)]
BF = [(0,9,27,36),(1,12,28,37),(2,15,29,38)]
base = {'U':faces(0)+tuple(UF),'R':faces(9)+tuple(RF),'F':faces(18)+tuple(FF),'D':faces(27)+tuple(DF),'L':faces(36)+tuple(LF),'B':faces(45)+tuple(BF)}
for k,v in base.items():
    MOVES[k]=v
    MOVES[k+"'"]=tuple(tuple(reversed(c)) for c in v)
    MOVES[k+'2']=tuple((c[0],c[2]) for c in v)