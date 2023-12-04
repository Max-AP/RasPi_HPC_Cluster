#Scattering data

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
