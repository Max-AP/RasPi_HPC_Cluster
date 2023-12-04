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
