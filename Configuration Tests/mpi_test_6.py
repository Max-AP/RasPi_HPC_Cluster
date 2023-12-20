# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.
#Tagging data

def main(args):
    return 0

if __name__ == '__main__':
    from mpi4py import MPI
    import sys
    
    comm = MPI.COMM_WORLD
    name = MPI.Get_processor_name()
    rank = comm.rank
    size = comm.size
    
    if rank == 0:
        shared1 = {"d1":55, "d2":42}
        comm.send(shared1, dest=1, tag=1)
        
        shared2 = {"d3":25, "d4":22}
        comm.send(shared2, dest=1, tag=2)
        
    if rank == 1:
        receive1 = comm.recv(source=0, tag=1)
        print("d1: {}, d2:{}".format(receive1["d1"], receive1["d2"]))
        receive2 = comm.recv(source=0, tag=2)
        print("d3: {}, d4:{}".format(receive2["d3"], receive2["d4"]))
