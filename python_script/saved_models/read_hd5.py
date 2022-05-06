import h5py

f = h5py.File('BankOfBaroda.h5', 'r')
list(f.keys())