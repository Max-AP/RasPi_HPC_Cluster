# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.
#Gathering data

def main(args):
    return 0

if __name__ == '__main__':
    from mpi4py import MPI
    import sys
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    if rank == 0:
        data = [x for x in range(0, size)]
        print("Scattering: " + " ".join(str(x) for x in data))
    else:
        data = None
    
    data = comm.scatter(data, root=0)
    print("Rank: {} has data {}".format(rank, data))
    data *= data
    
    newData = comm.gather(data, root=0)
    
    if rank == 0:
        print("We have gathered: " + " ".join(str(x) for x in newData))
