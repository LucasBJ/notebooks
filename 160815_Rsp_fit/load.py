import numpy as np

mrg_base = "data\mrg_L%s_z%s.dat"
rsp_base = "data\L%s_rsp_z%s.dat"

def read_int_ids(fname):
    """ Helper function. Neccessary to prevent truncation.
    """

    with open(fname)as fp: s = fp.read()
    lines = s.split("\n")
    col0s = [[tok for tok in line.split(" ") if tok!=""][0]
             for line in lines if line!=""]
    return np.array(map(int, col0s), dtype=int)

def load_box_data(L_str, z_str):
    """ load_box_data loads the R_sp, R_200m, and Gamma_200m data
    from the files conrresponding to a particular pair of L and z strings.
    """

    mrg_ids = read_int_ids(mrg_base % (L_str, z_str))
    order = np.argsort(mrg_ids)
    rsp_ids = read_int_ids(rsp_base % (L_str, z_str))
    mrg_idxs = np.searchsorted(mrg_ids[order], rsp_ids)

    r, g = np.loadtxt(mrg_base % (L_str, z_str),
                      usecols=(3, 4), unpack=True)
    r = r[order][mrg_idxs]
    g = g[order][mrg_idxs]
    rsp = np.loadtxt(rsp_base % (L_str, z_str), usecols=(3,))

    return rsp, r, g


if __name__ == "__main__":
    L_strs = ["63", "125", "250", "500"]
    z_strs = ["0", "05", "1", "2"]
    zs = [0.0, 0.5, 1.0, 2.0]

    rsp, r200, g200 = load_box_data(L_strs[2], z_strs[3])

    print "R_sp"
    print rsp[:10]
    print "R_200m"
    print r200[:10]
    print "Gamma_200m"
    print g200[:10]
