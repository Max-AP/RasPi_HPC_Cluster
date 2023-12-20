# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.
#Broadcasting data

def main(args):
    return 0

if __name__ == '__main__':
    from mpi4py import MPI
    import sys
    
    comm = MPI.COMM_WORLD
    rank = comm.rank
    
    if rank == 0:
        data = {"a":1, "b":2, "c":3}
    else:
        data = None
        
    data = comm.bcast(data, root=0)
    print("Rank: {}, Data: {}, {}, {}"
    .format(rank, data["a"], data["b"], data["c"]))
