Hi everyone! I want to thank everyone for coming to this event to hear me talk a little about my string of improbable and unverified breakthroughs in several fields of Computer Science. Sarcasm aside, I present exactly one small, relatively maybe unsurprising result today on the present capabilities of powerful computers to recognize things that I think look good and things that I don’t. Before I begin I want to encourage anyone with a question to raise their hand to ask -- I’m new to this so if you have a question it’s probably me, not you.

So the idea for this thesis actually did not originate from an interest in machine creativity but actually machine learning. I started out this semester with an interest in getting my hands dirty with neural networks -- applying the latest and greatest machine learning techniques to a dusty problem and seeing what happened. And I succeeded, both in finding a topic that I found agreeable and in getting my hands moderately dirty with neural networks. In case you don’t know already, neural networks are statistical models inspired by the high-level behavior of the neurons between our ears. The first reason I wanted to work with neural networks was because their name sounds super cool. I think the best part of doing a thesis involving neural networks is getting to tell people that you’re doing a thesis on neural networks. Once you say the word neural network theres a predictable eyebrow raise as everyone is utterly blown away at how smart you must be. In actuality, the basic mechanics of neural networks are relatively simple, and for this study I performed very little research of neural networks themselves. Sadly, everyone who may have thought I’m smarter for this reason is sorely mistaken.

No, the main focus of this research involves the budding field of computational aesthetics, which essentially boils down to two questions.

1. How can we model the way in which humans make subjective judgements of beauty? and 2. How can we implement these insights to produce accurate systems for automatically judging the beauty of art, music, design, or video? From here on out I’ll use the word aesthetics interchangeably with the word beauty.

So the first questions that people usually ask is how a computer could ever decide what’s good looking and what’s not, when we can’t even agree on what’s good looking and what’s not! There are a few responses to this question, but the main response it that the research community generally agrees that aesthetic judgements are inherently subjective, and so a model expressing aesthetic preferences would naturally be subjective as well. That isn’t to say that there aren’t unifying generalizations we can make about how people experience the sensation of beauty, but that those generalizations can only go so far before colliding with more personal parameters such as experiences and culture. Very few tasks short of general intelligence intersect with so many aspects of psychology as computational aesthetics. Think about it, if we had a system that could perfectly predict whether you’d like something a movie, we would likely have in hand a complete model of you as a person. When you expand the subject of aesthetics beyond media to ideas and concepts, such as mathematics, we start to see that the human aesthetic judgement system may have a lot to do with general purpose critical thinking. Concluding that judging the beauty of a thing on behalf of someone else is an extremely difficult problem, we can only make baby steps by dramatically reducing the scope and ambitions of this problem until it becomes manageable.

A good way to visualize the effectiveness of computational aesthetics is to use those measures of beauty in the generation of new artwork. Others have tried to apply machine learning techniques to the problem I describe, but they had done so using manual feature extraction and shallow neural networks rather than automatic feature extraction using deep neural networks. Their system was actually effective at generating novel artwork, which lead me to believe that more advanced neural networks might be even better suited for a more sophisticated image recognition task.

​

As an aside, many scientists have been thinking critically about the sensation of beauty and how it relates to information theory and machine learning. In the 30s a mathematician named Birkoff proposed a theoretical aesthetic measure. He put beauty = order/complexity. The general thinking behind this, which has been somewhat validated, is that beauty is the pleasurable resolution of sophisticated stimuli into compact internal representation. The greater the compression ratio, the greater the beauty. An example where this resolution is almost conscious resolution of cubist art, which predated Birkoff’s theory by a few decades. Later scientists have generalized this measure into the term “effective complexity”, which seeks to capture the sentiment of birkoff’s measure in the observation that humans are generally attracted to the things that are the most complex in the colloquial sense. This sense of the word complexity is meant to encapsulate the complexity of life and all the factors that go into the subjective complexity of a thing, such as novelty, surprisingness, contextual relevance, etc. A scientist called Galanter theorizes that the human aesthetic system is useful at a high level for guiding the acquisition of the most relevant information, and sophistication is generally a good heuristic for this.

​

[effective complexity chart]

​

I was unable to find any papers conducting research similar to mine; that is, I found no research attempting to train a machine learning model to recognize good generative art from bad generative art (as opposed to different kinds of generative art), especially using automatically extracted features. Upon reflection, this suggests that we chose either an entirely unexplored area of research, or that we’re testing an ambitious hypothesis. The later seems more likely.

Ways to reduce the scope? Reduce the complexity of the media. Prefer media with fewer symbolic dependencies. Increase the size of the training set by using generative art. Try to use compositional building blocks to produce interpretable experimental results (try and build a model for composition and color theory).

With my background research out of the way, I began setting up my experiment. The final formulation of this first experiment became: Let’s first generate a dataset of subjectively rated generative art. Next, lets train a state-of-the-art classifier on part of the dataset, and see how well its learning generalizes to other the other part of the dataset. Finally, lets do some analysis on the results to see what kind of images the classifier was good at rating, and what kind of images it was bad at rating.

​[flow chart image of experiment]

It is important to note this experiment involves an extremely sophisticated dataset, one which would require a high level of visual understanding to separate. If we were to succeed, we would be doing something that had really never been done. For example, see if you guys can classify these, based on the images on the left:

[few slides with pretty images on the left, test images on the right]

Setting up my experiment took longer than I would have liked, but I found the final setup agreeable.

​

I wrote a training interface in python with Flask, sqlite3 and Pillow. It would generate the random abstract art, present it to the user (me), and store the user’s ratings for each image. The interface asks for a binary rating, a thumbs up or a thumbs down for each image, corresponding of a 0 or a 1 rating. An image’s eventual training label was calculated as the average of its ratings. I made sure to collect at least two ratings for each image, so as to reduce the effects of user fatigue on rating consistency. So I might see an image twice after some period of time. I also built a tinder-like swipe detector so I could rate images on the go. After a few days I had made about 4300 ratings of about 2150 images, and I felt satisfied with that. This part of the process didn’t end up being very scientific.

​

To model this data I would need a lot of computational horsepower, more than my laptop could provide. After trying a few options I ended up renting a GPU instance (g2.2xlarge) from Amazon, because it was the only option with a CUDA compatible video card. Caffe is programmed to optionally take advantage of Nvidia’s proprietary instruction set. The GPU provided with remote computer I used has 1536 CUDA cores, affording it an 11x speedup over the CPU-only algorithms. With the GPU instance training would converge after only a few hours. I’ll get to my results in in a minute, but my accuracy was better than random (based on accurate priors).

​

[screenshot training interface]

​

[graphic of average image]

So now I’m going to make an attempt explain the basic premise of convolutional neural network in only a few minutes. First I’ll see if I can explain how normal neural network works, and then then I’ll try and explain how convolutional networks aren’t much different.

[image of a neuron]

​

The basic unit of a neural network is the artificial neuron, which on its own is limited to computing a relatively simple non-linear function. An artificial neuron is like a biological neuron in that it takes a number of numerical inputs and produces a single numerical output. Intuitively, if the sum of the numerical inputs is great enough, the output of the neuron quickly switches from 0 to 1. The function computed by an artificial neuron is uniquely defined by its “internal weights”. A neuron’s internal weights are a vector of numbers that determine how much a given input will factor into that neuron’s activation. Formula for a neuron.

​

So it turns out that when you wire up neurons like this [image of neural network], providing inputs on the left, letting the computations percolate, and taking outputs on the right, a neural network can accurately approximate any function, provided you have enough neurons and the neurons have the right weights. In the interest of time I’ll skip over how we figure out what those weights should be. Just know that effective and relatively simple training method exists and can be derived with some simple calculus.

The percentage that this model classified as correct out of the box was 74%.

​

[side by comparison]

​

Here’s a side by side comparison of images I considered pretty, ugly, and images that the model considered pretty.

​

[side by side comparison with color sorting on]

​

So if you’re like me, you looked at these side-by-side comparisons and you squinted and saw the set on the right as better than the set in the middle. You’d be right, statistically the set on the right is more attractive than the set in the middle. At the same time, the predicted set is definitely not as attractive as the set on the left. Reasonable, you might say, the classifier is only 74% accurate. Well it turns out that there is a third set that the distribution of images is like most alike: the training set. It turns out that in my training set, 74% of my images are rated as unattractive. This means that my model would have demonstrated the same accuracy had it guessed ugly every time. So I present a null result -- my model demonstrates no intelligence in predicting ratings for the images.

​

Unfortunately this result only tells us what didn’t work, rather than what did work. It seems clear that either the classifier architecture was inadequate for the complexity of the problem presented, or that the dataset was too small to generalize from for the problem presented, or a combination of both. Here are a few more statistics on the result.

​

Distribution of the image scores.

Distribution of model guesses.

[graph of the model’s accuracy on pretty images vs ugly images; false positives vs false negatives]

The most obvious item of future work would be to figure out why the model was ineffective at even modest accuracy gains on the dataset. This could be a problem with the classifier or with the dataset, or both. I wish I was experienced enough with convolutional neural networks to try to engineer an improvement. It may be possible that the media form used in this experiment on computational aesthetics is too sophisticated. One to simplify the problem would be to break it in two: ask whether we can teach a computer recognize agreeable color palettes, or if we can teach it to recognize agreeable arrangements of black rectangles on a white background.

​

If we were capable of doing better than “random” on such an aesthetic task, we would be able to use our computational aesthetic evaluator to generate new art in inventive ways.

Implement genetic programming interface to connect the classifier to produce images.
put together a system for interactively providing ratings to the most novel images, to generate greater scales of training data (would require a low false-negative performance).
Investigate questions of effective complexity with respect to standard image recognition convolutional neural networks, i.e. test to see if meta-properties of a image recognition model could be fed into a system for recognizing novelty and aesthetic value, differences in the dataset).
allow for multiple users to use the system
generalize and build a recommendation engine for images (instagram)
​

Lots of possibilities. You can tell I had some time to think about this before I discovered that my classifier doesn’t work.

​Philip Galanter warned in his writing that making headway in the field of computational aesthetics would be difficult. [Baby steps quote.]

​

On the other hand, [anything a human can do in under a second quote]

​

Generative art and Intelligent Interactive Systems are going to change the face of design (reducing the cost and expanding availability), and recommendation engines are only going to improve, once they incorporate the content of media into recommendations.

​

The original hypothesis of my experiment was that current image recognition algorithms would be capable of separating images based on a relatively small set of training examples labeled with subjective aesthetic ratings.

​

My hypothesis turned out to incorrect, because my model was incapable of doing better than random on the test set.

​

Either more data is needed, or a different machine learning architecture is needed, or both. If further research into either of these options do not prove fruitful in the short term, a faster path toward progress may involve reducing the difficulty of the problem and trying again.

​

Along the way I learned a hard lesson in data science, and learned a lot about the fledgeling field of computational aesthetics and exploding field of machine learning. I was grateful to have the opportunity to study in these fields, and I hope to make real contributions to them in the future.
