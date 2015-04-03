# Thesis Proposal
Teddy Knox

_Feb 21, 2015_


## Hybrid Computational Aesthetic Evaluation using Convolutional Neural Networks: Filtering Generative Art by Interactively Modeling User Tastes

Recent advances in machine learning techniques have resulted in increasingly effective algorithms for discovering creative solutions to quantifiable optimization problems. In general, problems unaffected by advances in machine learning are not those involving creativity, but those whose optimization functions are difficult to quantify. To teach a computer to produce aesthetically pleasing artwork, one first must define a "cost" function for what makes a piece aesthetically pleasing, either manually or automatically.

Evaluating an aesthetic cost function manually would involve repeatedly asking a human whether something was aesthetically pleasing to them, ad-naseum. The problem with this approach is user fatigue; there are only so many ratings a user can give before their rating quality decreases. Crowdsourcing aesthetic ratings also tends to produce uninspired as the average of conflicting opinions tends to do (so you might be able to teach a computer to produce pop music). Thus, Interactive Evolutionary Programming (IEP) techniques are difficult scale in the field of artistry.

Evaluating an aesthetic cost function automatically would involve infusing a computer with a way to evaluate universal and personal aesthetic tastes. This could be done either through programming, based fundamental principles of aesthetics, or through the modeling of a user's personal tastes. Understanding the fundamental principles of aesthetics turns out to be pretty tough to do (to start, try defining what art is). Art theory provides rough guidelines towards the aesthetically pleasing, but almost all of the underlying human mechanisms that explain these guidelines remain to be discovered. This leaves the option of modeling an individual user's personal tastes; teaching a powerful generic model to differentiate aesthetically pleasing and displeasing artworks based on a relatively small set of training ratings given by the user. This approach avoids the pitfall of asking _why_ humans find certain things pleasing, and would produce ratings at scale. In the scientific community, this task is referred to as Computation Aesthetic Evaluation (CAE), and is the holy grail of generative art research problems (I think?). If such a significantly accurate model could be developed, then today's machine learning techniques could likely be successfully applied to the world of generative art.

For my thesis I will build an interactive system for generating custom artwork according to user aesthetic preferences.  In developing this system, we hope to explore the applicability of generic Convolutional Neural Networks (CNNs) to Computational Aesthetic Evaluation (CAE). The system will randomly generate an artful images, and evaluate their aesthetic appeal using this experimental Convolutional Neural Network Computational Aesthetic Evaluation (CNN-CAE). If the CNN-CAE is unconfident in its rating, the system will prompt the user to rate the image for training. If the CNN-CAE is confident in its rating and the rating is above a constant threshold, it will be shown to the user for another training rating (the rating system is TBD, possibly binary). Otherwise, the image will be discarded.

The system will have three parts: the part that generates the art, the part that evaluates the art (CNN-CAE), and the part that connects the two and prompts the user for training ratings.

I'm still exploring art generation strategies. One idea I had was to generate colored fractal images like those seen in wallpapers. This would be fairly easy to parameterize and would produce a large range of results.

I plan to use a framework called Caffe to implement the Convolutional Neural Network. Our main research question asks whether CNNs (as implemented by Caffe) are predisposed to do meta-analysis on the aesthetic qualities of an image, or whether their strength lies solely in image classification based on relatively low-level features. A likely result is that Caffe will learn to identify that Teddy likes fractals colored blue/yellow and orange/green, but won't be able to make the generalization that Teddy likes fractals with colors opposite each other on the color wheel.

### References

- Galanter, Philip. [The Problem with Evolutionary Art Is ...](http://www.academia.edu/301908/The_Problem_With_Evolutionary_Art_Is..)
- Galanter, Philip. [Computational Aesthetic Evaluation: Steps Towards Machine Creativity](http://www.generativeart.com/on/cic/GA2010/2010_31.pdf)
- Takagi, Hideyuki. [Interactive Evolutionary Computation: Fusion of the Capabilities of EC Optimization and Human Evaluation](http://www.design.kyushu-u.ac.jp/~takagi/TAKAGI/IECpaper/ProcIEEE_3.pdf)
