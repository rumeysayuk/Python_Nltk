
import pandas as pd  # veri işleme, CSV dosyaları
import re  # Regex için gerekli modul
import string
import nltk
from nltk.corpus import stopwords

df = pd.read_csv("turkish_news_70000.csv/turkish_news_70000.csv", index_col="id")

# print(df.head(3))  # veri setindeki ilk 3 satır

news_dataset = df[["text"]]
# print(news_dataset.head(3))

# nltk nın içindeki noktalama işaretleri kümesi
punctuationSet = string.punctuation

# nltk nın içindeki etkisiz kelimeler kumesi
ineffectiveElementSet = stopwords.words("turkish")

# Bu kelimelere ek olarak kelime ekleme
ineffectiveElementSet.extend(["bir", "kadar", "çok"])


# Bu fonksiyon bütün veriler üzerinde gezecek
def cleanUpData(text):
    # Kelimeler küçük harfe çevrildi
    text = text.lower()

    # boşluk gördüğünde yeni satıra geçecek
    text = text.replace("\n ", " ")

    # Kesme işareti ve sonrasında gelen ifadeler regex ile kaldırılır
    text = re.sub("'(\w+)", "", text)
    # text = re.sub("[", ',', "]", "", text)

    # Sayıların kaldırılması
    text = re.sub("[0-9]+", "", text)

    # Noktalama işaretlerinin kaldırılması
    text = "".join(list(map(lambda x: x if x not in punctuationSet else " ", text)))

    # Etkisiz kelimelerin çıkarılması
    text = " ".join([i for i in text.split() if i not in ineffectiveElementSet])

    # Tek kalan harflerin çıkarılması
    text = " ".join([i for i in text.split() if len(i) > 1])
    return text


text = news_dataset.iloc[5].text
# temizlenmemiş data
print(text)
#  temizlenen data
print(cleanUpData(text))

# Texleri tokenize etme
news_dataset["cleared_text_token"] = news_dataset["cleared_text"].apply(lambda x: x.split())
print(news_dataset.head(10))

