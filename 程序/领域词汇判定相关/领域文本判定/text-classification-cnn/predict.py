# coding: utf-8

from __future__ import print_function

import os
import tensorflow as tf
import tensorflow.contrib.keras as kr

from cnn_model import TCNNConfig, TextCNN
from data.cnews_loader import read_category, read_vocab

try:
    bool(type(unicode))
except NameError:
    unicode = str

base_dir = 'data/cnews'
vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')

save_dir = 'checkpoints/textcnn'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径


class CnnModel:
    def __init__(self):
        self.config = TCNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextCNN(self.config)

        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess=self.session, save_path=save_path)  # 读取保存的模型

    def predict(self, message):
        # 支持不论在python2还是python3下训练的模型都可以在2或者3的环境下运行
        content = unicode(message)
        data = [self.word_to_id[x] for x in content if x in self.word_to_id]

        feed_dict = {
            self.model.input_x: kr.preprocessing.sequence.pad_sequences([data], self.config.seq_length),
            self.model.keep_prob: 1.0
        }

        y_pred_cls = self.session.run(self.model.y_pred_cls, feed_dict=feed_dict)
        return self.categories[y_pred_cls[0]]


def read_file_predict(path, r_file_name, w_file_name):
    cnn_model = CnnModel()

    count = 0
    line_count = 0
    fp = open(path + r_file_name + '.json', 'r', encoding='utf-8')
    w_fp = open(path + w_file_name + '.json', 'a', encoding='utf-8')
    for line in fp:
        line_count += 1
        if line_count % 1000 == 0:
            print(line_count)
        temp = line[1:]
        dic = eval(temp)
        res = cnn_model.predict(dic['detail'])
        if res == '审计':
            count += 1
            w_fp.write(temp)
            # print(dic['title'])
    fp.close()
    print('共计:', count, '个词条')


def test():
    cnn_model = CnnModel()
    test_demo = ['加拿大媒体指责中国绕开WTO报复美国 中使馆回应',
                 '对经济责任关系主体经济责任的履行情况监督、审查、评价和证明的一种方式。']
    for i in test_demo:
        print(i)
        print('属于：', cnn_model.predict(i), ' 领域\n')


if __name__ == '__main__':

    # read_file_predict('D:/workspace/data/', '根据越姐所给资料进一步爬的数据', '第二批数据')
    cnn_model = CnnModel()
    test_demo = ['加拿大媒体指责中国绕开WTO报复美国 中使馆回应',
                 '对经济责任关系主体经济责任的履行情况监督、审查、评价和证明的一种方式。']
    for i in test_demo:
        print(i)
        print('属于：', cnn_model.predict(i), ' 领域\n')
