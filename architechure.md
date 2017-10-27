
        Conv2D(32, (3,3))
                |
           MaxPooling2D
                |
            Flatten
                |
             LSTM(64)
                |
            Flatten
                |
            Dense(32)
                |
            Dropout(0.5)
                |
           Dense(softmax)
