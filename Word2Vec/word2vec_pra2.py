from gensim.models import word2vec


#コーパスの読み込み
file = open('data.txt')
corpus = file.read().splitlines()

#学習モデルの生成
corpus = [sentence.split() for sentence in corpus]
model = word2vec.Word2Vec(corpus, size=200, min_count=20, window=10)

#「文学」と似たキーワードを出力
similar_words = model.wv.most_similar(positive=['文学'], topn=9)
print(*['',join([v, str("{:.2f}".format(s))]) for v, s in similar_words], sep='\n')

'''エラーが出る…。'''
