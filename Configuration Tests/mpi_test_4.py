# Copyright
# Pajankar, A. (2017). Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts. Apress.
# This reference was used for understanding and implementing MPI4PY functionalities in the context of Raspberry Pi-based supercomputing.
#sending data

def main(args):
    return 0

if __name__ == '__main__':
    from mpi4py import MPI
    import time
    import sys

    comm = MPI.COMM_WORLD
    name = MPI.Get_processor_name()
    rank = comm.rank
    size = comm.size
    shared = 3.14

    if rank == 0:
        data = shared
        comm.send(data, dest=1)
        comm.send(data, dest=2)
        comm.send(data, dest=3)
        comm.send(data, dest=4)
        comm.send(data, dest=5)
        comm.send(data, dest=6)
        comm.send(data, dest=7)
        comm.send(data, dest=8)
        comm.send(data, dest=9)
        comm.send(data, dest=10)
        comm.send(data, dest=11)
        comm.send(data, dest=12)
        comm.send(data, dest=13)
        comm.send(data, dest=14)
        comm.send(data, dest=15)

        print("From rank {}, we sent {}".format(name,data))
        time.sleep(5)
    else:
        data = comm.recv(source=0)
        print("On rank {}, we received {}".format(name,data))
