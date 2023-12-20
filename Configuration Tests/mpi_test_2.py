# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.
#Check conditional statements

def main(args):
    return 0

if __name__ == '__main__':
    from mpi4py import MPI
    import sys

    comm = MPI.COMM_WORLD

    print("My rank is {}".format(comm.rank))

    if comm.rank == 0:
    	print("Doing the task of Rank {}".format(comm.rank))

    if comm.rank == 1:
    	print("Doing the task of Rank {}".format(comm.rank))
