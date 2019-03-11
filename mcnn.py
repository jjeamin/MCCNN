from ops import *

def net9(x):
    # w x h x 3 -> w x h x 16
    net = conv(x, 16, kernel=9, stride=1, padding='same', scope='conv_1_9x9')
    net = relu(net)
    # w x h x 16 -> w/2 x h/2 x 16
    net = pool(net, kh=2, kw=2, stride=2,  padding='same', scope='pool_1_9x9')
    # w/2 x h/2 x 16 -> w/2 x h/2 x 32
    net = conv(net,32, kernel=7, stride=1, padding='same', scope='conv_2_9x9')
    net = relu(net)
    # w/2 x h/2 x 32 -> w/4 x h/4 x 32
    net = pool(net, kh=2, kw=2, stride=2,  padding='same', scope='pool_2_9x9')
    # w/4 x h/4 x 32 -> w/4 x h/4 x 16
    net = conv(net, 16, kernel=7, stride=1, padding='same',scope='conv_3_9x9')
    net = relu(net)
    # w/4 x h/4 x 32 -> w/4 x h/4 x 8
    net = conv(net, 8, kernel=7, stride=1, padding='same',scope='conv_4_9x9')
    net = relu(net)
    return net

def net7(x):
    # w x h x 3 -> w x h x 20
    net = conv(x, 20, kernel=7, stride=1, padding='same', scope='conv_1_7x7')
    net = relu(net)
    # w x h x 20 -> w/2 x h/2 x 20
    net = pool(net, kh=2, kw=2, stride=2, padding='same', scope='pool_1_7x7')
    # w/2 x h/2 x 20 -> w/2 x h/2 x 40
    net = conv(net, 40, kernel=5, stride=1, padding='same', scope='conv_2_7x7')
    net = relu(net)
    # w/2 x h/2 x 40 -> w/4 x h/4 x 40
    net = pool(net, kh=2, kw=2, stride=2, padding='same', scope='pool_2_7x7')
    # w/4 x h/4 x 40 -> w/4 x h/4 x 20
    net = conv(net, 20, kernel=5, stride=1, padding='same', scope='conv_3_7x7')
    net = relu(net)
    # w/4 x h/4 x 20 -> w/4 x h/4 x 10
    net = conv(net, 10, kernel=5, stride=1, padding='same', scope='conv_4_7x7')
    net = relu(net)
    return net

def net5(x):
    # w x h x 3 -> w x h x 24
    net = conv(x, 24, kernel=5, stride=1, padding='same', scope='conv_1_5x5')
    net = relu(net)
    # w x h x 24 -> w/2 x h/2 x 24
    net = pool(net, kh=2, kw=2, stride=2, padding='same', scope='pool_1_5x5')
    # w/2 x h/2 x 24 -> w/2 x h/2 x 48
    net = conv(net, 48, kernel=3, stride=1, padding='same', scope='conv_2_5x5')
    net = relu(net)
    # w/2 x h/2 x 48 -> w/4 x h/4 x 48
    net = pool(net, kh=2, kw=2, stride=2, padding='same', scope='pool_2_5x5')
    # w/4 x h/4 x 48 -> w/4 x h/4 x 24
    net = conv(net, 24, kernel=3, stride=1, padding='same', scope='conv_3_5x5')
    net = relu(net)
    # w/4 x h/4 x 24 -> w/4 x h/4 x 12
    net = conv(net, 12, kernel=3, stride=1, padding='same', scope='conv_4_5x5')
    net = relu(net)
    return net

def merge_net(net5,net7,net9):
    net = tf.concat([net5,net7,net9],axis=3)
    net = conv(net,1,kernel=3,stride=1,padding='same',scope='conv_merge')
    return net


'''
# network test

import numpy as np

if __name__ == "__main__":
    x = tf.placeholder(tf.float32, [1, 200, 300, 1])
    net = build(x)
    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    d_map = sess.run(net,feed_dict={x:255*np.ones(shape=(1,200,300,1), dtype=np.float32)})
    prediction = np.asarray(d_map)
    prediction = np.squeeze(prediction, axis=0)
    prediction = np.squeeze(prediction, axis=2)
'''