import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # Data

'''
Regression
========
Source: https://www.tensorflow.org/versions/master/tutorials/mnist/beginners/index.html#implementing-the-regression
'''
# Input for the image x
x = tf.placeholder(tf.float32, [None, 784])

# Weights
W = tf.Variable(tf.zeros([784, 10]))

# Bias
b = tf.Variable(tf.zeros([10]))

# Model
'''
First, we multiply x by W with the expression tf.matmul(x, W).
This is flipped from when we multiplied them in our equation, where we had Wx,
as a small trick to deal with x being a 2D tensor with multiple inputs.
We then add b, and finally apply tf.nn.softmax.

Source: https://www.tensorflow.org/versions/master/tutorials/mnist/beginners/index.html#implementing-the-regression
'''
y = tf.nn.softmax(tf.matmul(x, W) + b)

'''
Training
========
Source: https://www.tensorflow.org/versions/master/tutorials/mnist/beginners/index.html#training
'''
# Cross-Entropy
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

# Tutorial's optimization strategy
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# Initialize the variables we created
init = tf.initialize_all_variables()

# Launch the model in a Session, and run the operation that initializes the variables
sess = tf.Session()
sess.run(init)

# Let's train -- we'll run the training step 1000 times!
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

'''
Evaluating Our Model
========

Well, first let's figure out where we predicted the correct label.
tf.argmax is an extremely useful function which gives you the index of the
highest entry in a tensor along some axis. For example, tf.argmax(y,1) is the
label our model thinks is most likely for each input, while tf.argmax(y_,1) is
the correct label. We can use tf.equal to check if our prediction matches the truth.

Source: https://www.tensorflow.org/versions/master/tutorials/mnist/beginners/index.html#evaluating-our-model
'''

# Does the prediction match the truth? - outputs list of booleans
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

# Determines accuracy out of 100 percent
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# Print accuracy -- should be about 91% (says the tutorial)
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
