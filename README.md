
# RasPi_HPC_Cluster

Welcome to the RasPi_HPC_Cluster GitHub repository! This repository is dedicated to the development and documentation of a Raspberry Pi-based high-performance computing (HPC) cluster. The focus here is on leveraging the MPI4PY library for parallel computing with a Raspberry Pi cluster. The tests and benchmarks included in this repository provide insights into various functionalities of MPI4PY and demonstrate the capabilities of Raspberry Pi in a high-performance computing context.

The Raspberry Pis need to be configured with the OpenMPI and MPI4PY implementations of MPI. 

## Configuration Tests

These configuration tests are designed as an introduction to some of the key functionalities of the MPI4PY library, as described in the book "Raspberry Pi Supercomputing and Scientific Programming: MPI4PY, NumPy, and SciPy for Enthusiasts" by Ashwin Pajankar.

1. **mpi_test.py**: A simple communication test between processes. It can only be run on 16 processes, where a string from process 0 (master) is sent to the other 15, which then complete the information with their respective ranks.

2. **mpi_test_1.py**: A version of the classic “Hello World” test program. It prints this message on the console, specifying the hostname of the Raspberry Pi where it is executed and the assigned process number.

3. **mpi_test_2.py**: Conditional check test. This program aims to demonstrate how code can be executed on a designated compute node using its assigned number as a reference.

4. **mpi_test_3.py**: Programmatically checks the total number of processes that can be used in the cluster.

5. **mpi_test_4.py**: Data transfer test between processes. A variable is created in the master node and sent to the other nodes. To verify, the received data packet is printed.

6. **mpi_test_5.py**: Similar to mpi_test_4.py, but with dynamically assigned variable values. The destinations of this data are also dynamically assigned by the script.

7. **mpi_test_6.py**: Data labeling test. To identify the origin of the data each process receives, a label can be added. This test performs this task and then verifies the information by printing the contents of the data depending on its label.

8. **mpi_test_7.py**: Data transmission test. Unlike previous tests where the data destination was specified, this task involves transmitting data from a particular node to all others. The data created in the master node are printed from the other nodes to verify this.

9. **mpi_test_8.py**: Broadcast test. Similar to the transmission test, this task sends data generated on the master node to the others. However, instead of sending a copy of all the data, it distributes them in equal parts before sending.

10. **mpi_test_9.py**: Gathering test. The master node collects the results of the computing operations from the other nodes for use. 

## Performance Tests

The performance tests, including test2.py, test4.py, and HPL (High-Performance Linpack), are designed to measure the cluster's performance by timing the execution of computationally intensive mathematical operations. HPL, developed by J. Dongarra, J. Bunch, C. Moler, and G. W. Stewart, is available as free software at [https://www.netlib.org/benchmark/hpl/](https://www.netlib.org/benchmark/hpl/).

1. **test2.py**: Performance test using the Monte Carlo method for estimating pi. This method involves dividing the points to be processed equally among each node, reducing counting time and speeding up the pi estimation process.

2. **test3.py, test4.py, test5.py**: Performance tests using matrix multiplication. These scripts contain the algorithm to divide matrix multiplication into parts that can be independently processed by each node. To address outliers, different versions were created to ensure there were no errors in the algorithm. After verification, test4.py was established as the preferred method, using a dot product method optimized by the NumPy library.

---

