import Sentiment_Data_for_bloomberg
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
plt.style.use('fivethirtyeight')


df = Sentiment_Data_for_bloomberg.sentiment_data()

allWords = " ".join([twts for twts in df["Tweets"]])
wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 119).generate(allWords)

def word_cloud():
    plt.imshow(wordCloud, interpolation = "bilinear")
    plt.axis("off")
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image