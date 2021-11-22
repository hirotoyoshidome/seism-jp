cdef extern from "sample.hpp":
    cdef int calc_add(int x, int y)

def sample_add(int x, int y):
    cdef int ans
    ans = calc_add(x, y)
    return ans
