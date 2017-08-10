import os
import sys
import tensorflow as tf
import numpy as np
import scipy.io
import scipy.misc

import pandas as pd

vgg=scipy.io.loadmat("vgg.mat")
layers=vgg['layers']#0 l 0 0 2 0 0

#intializing output directory
output="documents/greetings/output"
image_for_style="/Users/aparna/Documents/greetings/style.jpg"
content_image="/Users/aparna/Documents/greetings/i.jpg"

image_width=278
image_height=181
color_channels=3

beta=5#less content loss
alpha=100 #

mean_values= np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3))

def preprocess_input(path):
    image = scipy.misc.imread(path)
    image = np.reshape(image, ((1,) + image.shape))
    image = image - mean_values
    return image

def output(path,image):
    image = image + mean_values
    image = image[0]
    image = np.clip(image, 0, 255).astype('uint8')
    scipy.misc.imsave(path, image)

def model():
    style_layer=["conv1_1","conv2_1","conv3_1","conv4_1","conv5_1"]
    #loading the model


    def weight(l):
        """
        returns the weights of each of the required layers of VGG19
        """
        W=layers[0][l][0][0][2][0][0]
        b=layers[0][l][0][0][2][0][1]
        return W,b

    def  relu_func(input):
        return tf.nn.relu(input)

    def conv2d(prev,l):
        W=weight(l)[0]
        b=weight(l)[1]
        W=tf.constant(W)
        B= tf.constant(np.reshape(b, (b.size)))
        return tf.nn.conv2d(input=prev,filter=W,strides=[1,1,1,1],padding="SAME")+B

    def relu_plus_conv(prev,l):
        return relu_func(conv2d(prev,l))

    def pooling(prev):
        return tf.nn.avg_pool(input=prev,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

    graph = {}
    graph['input'] = tf.cast(tf.Variable(np.zeros((1, image_height, image_width, color_channels))),tf.float32)
    graph['conv1_1'] = relu_plus_conv(graph['input'], 0)
    graph['conv1_2'] = relu_plus_conv(graph['conv1_1'], 2)
    graph['relu1'] = relu_func(graph['conv1_1'])

    graph['conv2_1'] = relu_plus_conv(graph['relu1'], 5)
    graph['conv2_2'] = relu_plus_conv(graph['conv2_1'], 7)
    graph['relu2'] = relu_func(graph['conv2_2'])

    graph['conv3_1'] = relu_plus_conv(graph['relu2'], 10)
    graph['conv3_2'] = relu_plus_conv(graph['conv3_1'], 12)
    graph['conv3_3'] = relu_plus_conv(graph['conv3_2'], 14)
    graph['conv3_4'] = relu_plus_conv(graph['conv3_3'], 16)
    graph['relu3'] = relu_func(graph['conv3_4'])

    graph['conv4_1'] = relu_plus_conv(graph['relu3'], 19)
    graph['conv4_2'] = relu_plus_conv(graph['conv4_1'], 21)
    graph['conv4_3'] = relu_plus_conv(graph['conv4_2'], 23)
    graph['conv4_4'] = relu_plus_conv(graph['conv4_3'], 25)
    graph['relu4'] = relu_func(graph['conv4_4'])

    graph['conv5_1'] = relu_plus_conv(graph['relu4'], 28)
    graph['conv5_2'] = relu_plus_conv(graph['conv5_1'], 30)
    graph['conv5_3'] = relu_plus_conv(graph['conv5_2'], 32)
    graph['conv5_4'] = relu_plus_conv(graph['conv5_3'], 34)
    graph['relu5'] = relu_func(graph['conv5_4'])
    return graph

def generate_noise_image(content_image,):
    noise_image = np.random.uniform(-20, 20,(1, image_height,image_width,color_channels)).astype('float32')
    # White noise image from the content representation. Take a weighted average
    # of the values
    input_image = noise_image * 0.6 + content_image * 0.4#probability
    return input_image

def content_loss(x,p):
    return tf.reduce_sum(tf.pow(x-p,2))

def gram_matrix(n,m,x):
    x = tf.reshape(x, (m, n))
    return tf.matmul(tf.transpose(x), x)#finding aggregate

def style_loss_single(a,g,x):
    m=a.shape[1]*a.shape[2]
    n=a.shape[3]
    A=gram_matrix(n,m,a)
    G=gram_matrix(n,m,g)

    return (1/(4*n**2*m**2))*tf.reduce_sum(tf.pow(A-G,2))

def total_style_loss():
    sum=0
    for layer in style_layer:
        sum+=0.2*style_loss_single(sess.run(graph[layer]), graph[layer])
    return sum

#build the model
sess = tf.InteractiveSession()
content_image = preprocess_input(content_image)


style=preprocess_input(image_for_style)
graph= model()

input_image = generate_noise_image(content_image)

sess.run(tf.global_variables_initializer())

v=tf.Variable(graph['input'])
v.assign(content_image)
sess.run(v)
c_l=content_loss(sess.run(graph['conv4_2']), graph['conv4_2'])

sess.run(tf.assign(graph['input'],style))
s_l=total_style_loss()

total_loss = beta * c_l + alpha * s_l

optimizer = tf.train.AdamOptimizer(2.0)
train_step = optimizer.minimize(total_loss)

sess.run(tf.initialize_all_variables())
sess.run(graph['input'].assign(input))
iter=1000
for it in range(iter):
    sess.run(train_step)
    if it%100 == 0:
        # Print every 100 iteration.
        mixed_image = sess.run(graph['input'])
        print('Iteration %d' % (it))
        print('sum : ', sess.run(tf.reduce_sum(mixed_image)))
        print('cost: ', sess.run(total_loss))

        if not os.path.exists(output):
            os.mkdir(output)

        filename = 'output/%d.png' % (it)
        output(filename, mixed_image)
