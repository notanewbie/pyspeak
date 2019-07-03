from BRIAN import BRIAN
def core(r="", a=""):
    z = raw_input("YOU: ");
    r = BRIAN(z,a)
    core(z,r);
core();
