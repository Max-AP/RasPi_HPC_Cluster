# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.

def main(args):
    return 0

if __name__ == '__main__':
	from mpi4py import MPI
	import sys

	comm = MPI.COMM_WORLD
	name = MPI.Get_processor_name()

	print("Hello World! Name: {}, My rank is {}".format(name, comm.rank))

