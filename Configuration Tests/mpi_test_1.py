def main(args):
    return 0

if __name__ == '__main__':
	from mpi4py import MPI
	import sys

	comm = MPI.COMM_WORLD
	name = MPI.Get_processor_name()

	print("Hello World! Name: {}, My rank is {}".format(name, comm.rank))

