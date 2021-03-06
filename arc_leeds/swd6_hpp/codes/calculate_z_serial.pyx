def calculate_z_serial_purepython(int maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    cdef int n, z, c
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
	z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

