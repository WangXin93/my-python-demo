import numpy as np
import tensorflow as tf

x = tf.placeholder(tf.float32, [1,2], name='x')
y = tf.placeholder(tf.float32, [1,1], name='y')
# First layer
with tf.variable_scope('Layer1'):
	b1 = tf.Variable(tf.ones([1,2]), name='b1')
	w1 = tf.Variable(tf.ones([2,2]), name='w1')
	h1 = tf.nn.relu(tf.matmul(x, w1) + b1)
# Second layer
with tf.variable_scope('Layer2'):
	w2 = tf.Variable(tf.ones([2,1]), name='w2')
	b2 = tf.Variable(tf.ones([1,1]), name='b2')
	h2 = tf.matmul(h1, w2) + b2
loss = (y - h2)**2
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
feed_dict = {x:np.random.randn(1,2), y:np.random.randn(1,1)}

def run_once():
	sess.run(train_op, feed_dict=feed_dict)
	out_w1, out_w2, out_b1, out_b2 = sess.run([w1,w2,b1,b2],
											  feed_dict=feed_dict)
	print("w1:\n%s\nb1:\n%s\nw2:\n%s\nb2\n%s" % (out_w1, out_b1, out_w2, out_b2))

count = 0
for i in range(3):	
	count += 1
	print("This is the %sth train." % count)
	run_once()
	print("="*50)
#writer = tf.summary.FileWriter('./log', sess.graph)
sess.close()