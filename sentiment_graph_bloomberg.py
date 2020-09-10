import Sentiment_Data_for_bloomberg
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import io

df = Sentiment_Data_for_bloomberg.sentiment_data()

def sentiment_graph():
    plt.title("Sentiment Analysis")
    plt.xlabel("Sentiment")
    plt.ylabel("Counts")
    df["Analysis"].value_counts().plot(kind="bar")
    bytes_image_2 = io.BytesIO()
    plt.savefig(bytes_image_2, format='png')
    bytes_image_2.seek(0)
    return bytes_image_2

