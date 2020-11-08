# ViralCast - HackRPI 2020
[Rohan Agarwal](https://github.com/roaga) / 
[Jed Magracia](https://github.com/nordaxion) / 
[Hanif Fauzan](https://github.com/hanifzaans) / 
[Bao Tran](https://github.com/baotran01)
## Inspiration
The rampant spread of misinformation on platforms like Twitter caused much confusion and chaos in the face of an unprecedented pandemic, possibly leading to many preventable deaths. For the remainder of the COVID-19 pandemic and for any future pandemics, it is therefore important to be able to attack misinformation at its source. This is why we wanted to leverage machine learning to predict the spread of social media posts. If successful, platforms could use this technique to monitor and flag potential fake news **before** it goes viral and **before** it misleads thousands, not after.

## What It Does
ViralCast demonstrates a model for predicting the spread of a tweet, predicting both the number of favorites and retweets it will receive, based on the properties of the tweet's text and the tweeter's follower count. The web app lets a user type in a tweet and fake follower count, and then receive a prediction.

## How We Built It
We used a dataset of around 500k tweets related to COVID-19. Using IBM Watson Natural Language Understanding, we added data on sentiment, emotion, entities, and more to each entry. We trained a regression model using SciKit-Learn on this enhanced data. Using React and a Flask server, we created an interactive demo showcasing the model and its predictions.

## Challenges We Ran Into
Our first major challenge was figuring out how to represent Twitter text numerically with enough features to train an accurate model. After looking through numerous solutions, we settled on IBM Watson NLU for its easy-to-use API and multiple different analyses, such as sentiment, emotion, entities, and entity sentiment and emotion.

Once this was settled, another big challenge we ran into was efficiency. How can we preprocess thousands of rows of data quick enough for a 24-hour project? Our solution was to implement multithreading into our data processing script.

Finally, we were considering 11 total text features and predicting 2 different variables. We needed to figure out a good model for handling this complexity, so we settled on regression in SciKit-Learn.

On another note, the team was split across two hemispheres, making communication and time management another challenge we learned to overcome.

## Accomplishments that We're Proud of
We are proud of the technologies and techniques we learned to use over the course of 24 hours, from IBM's products to machine learning and multithreading, from Flask servers to React frontend and data visualization, and how we could bring them all together to address this issue. We're glad we were able to learn so much and demonstrate a potential pathway to tackling a large and current problem in the world.

## What We Learned
We learned a lot about visualization, natural language processing through the cloud, program efficiency, machine learning involving multiple variables over large datasets, and tying together frontend and backend through flask. We also explored the capabilities of machine learning and data science in solving a real-world issue, which was a valuable experience.

## What's next for ViralCast
Our first next step is to train on more data and potentially integrate more features into the model, such as word embeddings. This will allow the model to reach its full potential. We could also explore ways to integrate the web app with a person's Twitter feed, perhaps through a browser extension, so that it can be put to use in daily life. Additionally, we can explore alternate datasets, such as "fake news" sets or sets for other topics impacted by misinformation, and see how well the concept generalizes.

## More Information
Check out our [video demo](https://youtu.be/BCXJ6Oxg_Hc) and [DevPost submission](https://devpost.com/software/tbd-4cpvig).
