# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.
#Print total number of processes in the cluster

def main(args):
    return 0

if __name__ == '__main__':
    from mpi4py import MPI
    import time
    import sys

    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    print("Rank: {}, Process Count: {}".format(rank, size))
