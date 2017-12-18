import numpy as np

class DataGenerator(object):
  'Generates data for Keras'
  def __init__(self, dim_x = 32, dim_y = 32, dim_z = 32, batch_size = 32, shuffle = True):
      'Initialization'
      self.dim_x = dim_x
      self.dim_y = dim_y
      self.dim_z = dim_z
      self.batch_size = batch_size
      self.shuffle = shuffle

  def generate(self, labels, lists):
      'Generates batches of samples'
      # Infinite loop
      while 1:
          # Generate order of exploration of dataset
          indexes = self.__get_exploration_order(lists)

          # Generate batches
          imax = int(len(indexes)/self.batch_size)
          for i in range(imax):
              # Find list of IDs
              lists_temp = [lists[k] for k in indexes[i*self.batch_size:(i+1)*self.batch_size]]

              # Generate data
              X, y = self.__data_generation(labels, lists_temp)

              yield X, y

  def __get_exploration_order(self, lists):
      'Generates order of exploration'
      # Find exploration order
      indexes = np.arange(len(lists))
      if self.shuffle == True:
          np.random.shuffle(indexes)

      return indexes

  def __data_generation(self, labels, list_arrs_temp):
      'Generates data of batch_size samples' # X : (n_samples, v_size, v_size, v_size, n_channels)
      # Initialization
      X = np.empty((self.batch_size, self.dim_x, self.dim_y, self.dim_z),dtype=int)
      y = np.empty((self.batch_size), dtype = int)

      # Generate data
      for i, arr in enumerate(list_arrs_temp):
          # Store volume
          if arr.shape != (6720,64,64):
              arr = np.transpose(arr, [2, 1, 0])
          #print arr.shape
          X[i] = arr
                            

          # Store class
          y[i] = labels[i]
      return X, sparsify(y)

def sparsify(y):
    'Returns labels in binary NumPy array'
    n_classes = 3 # Enter number of classes
    return np.array([[1 if y[i] == j else 0 for j in range(n_classes)]
                   for i in range(y.shape[0])])