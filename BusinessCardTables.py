
from math import sqrt

def is_prime(n):
    if n<2: return False
    if n==2: return True
    if n%2==0: return False
    for i in xrange(3, int(sqrt(n)), 2):
        if n%i==0: return False
    return True


if __name__ == '__main__':

    from math import log10, floor, ceil, sin, pi, cos, tan

    ROWS = 20
    COLS = 5

    for i in range(2,ROWS):
        print(r"            \cellcolor{CELL}\textbf{" +
              r"{:1.1f}".format(i*0.5) +
              r"} & $\;$" +
              r" & $\;$".join("{:0.4f}".format(log10(i*0.5 + j*0.1))[2:] for j in range(COLS)) +
              r" \\" + (r"" if i%4 in (0,3) else r" \rowcolor{ROW}") + (r"" if i!=ROWS-2 else r" \smallskip"))

    print("")

    for i in range(ROWS-2):
        print(r"            \cellcolor{CELL}\textbf{" +
              r"{:02d}".format(i*5) +
              r"$\boldsymbol{^{\circ}}$} & $\;$" +
              r" & $\;$".join("{:0.4f}".format(sin(pi*(i*5+j)/180))[2:] for j in range(COLS)) +
              r" \\" + (r"" if i%4 in (1,2) else r" \rowcolor{ROW}") + (r"" if i!=ROWS-4 else r" \medskip"))

