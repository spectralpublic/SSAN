# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from tensorflow.contrib import slim
import tensorflow as tf
from utils import patch_size, Prepare_data, Height, Width, Band, Database, n_classes, num_band, num_classes
import numpy as np
import os
import scipy.io
import time
from nonlocal_resnet_utils import nonlocal_dot
import copy

# tf Graph input
x = tf.placeholder("float", [None, patch_size, patch_size, Band])
y = tf.placeholder("float", [None, n_classes])
is_training = tf.placeholder(tf.bool)


def conv_net(x):
    batch_norm_params = {
      'decay': 0.95,
      'epsilon': 1e-5,
      'scale': True,
      'updates_collections': tf.GraphKeys.UPDATE_OPS,
      'is_training': is_training,
      'fused': None,
    }

    with slim.arg_scope([slim.conv2d, slim.fully_connected],
                      activation_fn=tf.nn.relu,
                      normalizer_fn=slim.batch_norm,
                      normalizer_params=batch_norm_params):
        #tf.set_random_seed(0)
        x = tf.transpose(x,[0,3,1,2])
        ######################################### spectral feature learning 
        net0 = tf.reshape(x, [-1, num_band, patch_size, patch_size, 1]) 
        print(net0.shape)
        net1 = slim.conv3d(net0, 32, kernel_size=[7, 1, 1], stride=[1, 1, 1], padding='SAME', scope='conv1')
        print(net1.shape)
        # block1
        net2 = slim.conv3d(net1, 32, kernel_size=[7, 1, 1], stride=[1, 1, 1], padding='SAME', scope='conv2')
        print(net2.shape)
        #net3 = slim.conv3d(net2, 32, kernel_size=[7, 1, 1], stride=[1, 1, 1], padding='SAME', scope='conv3')  
        #print(net3.shape)
        
        ######################################### spatial feature learning 
        net3 = tf.transpose(net2,[0,2,3,1,4])
        print(net3.shape)
        net3 = tf.reshape(net3, [-1, patch_size, patch_size, 32*num_band]) # UP:103  IP:220  num_band is the number of spectral bands.
        print(net3.shape)
        ######################################### nonlocal 
        net3 = nonlocal_dot(net3, 64)
        net4 = slim.conv2d(net3, 64, 3, padding='SAME', scope='conv4')
        print(net4.shape)
        ######################################### nonlocal 
        net4 = nonlocal_dot(net4, 64)
        net5 = slim.conv2d(net4, 64, 3, padding='SAME', scope='conv5')
        print(net5.shape)
        ######################################### nonlocal 
        net5 = nonlocal_dot(net5, 64)
        print(net5.shape)        



        ######################################### classification
        net = slim.flatten(net5)
        print(net.shape)
        #net = slim.fully_connected(net,256)
        #net = slim.dropout(net, 0.5, is_training=is_training)
        net = slim.fully_connected(net,256)
        net = slim.dropout(net, 0.5, is_training=is_training)
        logits = slim.fully_connected(net, num_classes, activation_fn=None)
        print(logits.shape)

    return logits