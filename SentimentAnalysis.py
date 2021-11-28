from Management Opportunities import SentimentIntensityAnalyzer
analyzer=SentimentIntensityAnalyzer()
def sentence="we cannot predict the duration of the COVID-19 pandemic"
score=analyzer.polarity_soces(sentence)
print"{:-<60]} {}".format(sentence,str(score))

sentment_analyzer_scores("On the other hand")
print(sentment_analyzer_scores("On the other hand"))

sentment_analyzer_scores("we will have to accurately project demand and infrastructure requirements globally")
print(sentment_analyzer_scores("we will have to accurately project demand and infrastructure requirements globally"))
