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
