import scipy
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import coo_matrix
import sys
import os
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)

def genSolution(T,M,TEST):
    print(T,M,TEST)
    mach = np.random.choice(list(range(M)), size=TEST, replace=False)
    tasks = np.hstack((np.random.RandomState().permutation(T), np.random.choice(list(range(T)), size=TEST-T, replace=True)))
    return mach,tasks

def check_X(X, E, D, eta):
    assert np.all(np.sum(X, axis=0) <= 1)
    assert np.all(np.sum(X, axis=1) >= 1)
    assert np.sum((E / np.sum(np.multiply(eta, X), axis=1) - D) > 0) == len(E)

        
def getData(NT, NM):
    E = np.random.random(NT)
    D = np.random.random(NT)
    eta = np.random.random((NT, NM))
    rows, cols = genSolution(NT, NM, NM)
    X = coo_matrix((np.ones(NM), (cols, rows)), shape=(NT, NM)).todense()
    print(X.shape)
    print(E.shape)
    print(D.shape)
    print(eta.shape)
    return X, E, D, eta
        
if __name__ == "__main__":
    NT= 10
    NM = 50

    E = np.random.random(NT)
    D = np.random.random(NT)
    eta = np.random.random((NT, NM))
    rows, cols = genSolution(NT, NM, NM)
    X = coo_matrix((np.ones(NM), (cols, rows)), shape=(NT, NM)).todense()
    print(X.shape)
    print(E.shape)
    print(D.shape)
    print(eta.shape)