# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.
#Sending data dynamically


def main(args):
    return 0

if __name__ == '__main__':
    from mpi4py import MPI
    import sys
    
    comm = MPI.COMM_WORLD
    name = MPI.Get_processor_name()
    rank = comm.rank
    size = comm.size
    
    shared = (rank + 1) * (rank + 1)
    
    comm.send(shared, dest=(rank+1) % size)
    data = comm.recv(source=(rank-1) % size)
    print("Name: {}\n"
    "Rank: {}\n"
    "Data {} came from rank {}\n"
    "=========================================="
    .format(name, rank, data, (rank - 1)%size))


