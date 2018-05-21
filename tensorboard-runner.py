import tensorflow as tf
from tensorboard import main as tb
tf.flags.FLAGS.logdir = "./logs"
tb.main()
