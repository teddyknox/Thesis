# Thesis Proposal: Train a Convolutional Neural Network to Play GeoGuessr
[GeoGuessr](https://www.geoguessr.com) is a geography quiz game that tests a player's ability to extract locational information from panoramic photographs. In each round, the player is presented a random Google Streetview scene and asked to guess the location of that scene on the planet using only contextual clues. After seven rounds, the player's score is calculated based on guess accuracy.

I would like to propose a programming a computer to play this game, using [Caffe](http://caffe.berkeleyvision.org/), a popular and actively developed Convolutional Neural Network (CNN) framework. I will train the system on random labeled streetview locations all over the world, and then test its competency on the GeoGuessr game. I will train the model with textual labels of location names (rather than geographical coordinates) to manage the complexity of the model and ensure intuitive outputs. If I have time, I will convert the model from a label-oriented classifier to a geographic coordinate regressor to further optimize the program's accuracy.

Executing this project will involve four stages:
0. Developing a better understanding of CNNs and the Caffe framework
0. Implementing a programmatic framework for gathering training data and for testing the system.
0. Combining the Caffe framework and the data framework to build a system for guessing geographical locations
0. Optimizing this system for accuracy

In order to learn more about Convolutional Neural Networks, I will immerse myself in the abundant online resources describing their mechanics. Caffe itself is a well-documented project, with several tutorials and demos to learn from. I also expect that Professor Scharstein will be valuable resource for his familiarity with the field of computer vision. Additionally, I would be able to seek guidance from Dartmouth C.S. student and researcher [Feynman Liang](http://feynmanliang.com), who is currently pursuing novel research on CNNs and is familiar with the Caffe framework.

In my experience, gathering training data for such models tends to be surprisingly time-consuming and troublesome. With this expectation in mind, I will strive to complete this research task as early in the semester as possible. Trivial inspection of the geoguessr website suggests I should be able to reverse engineer their API to collect training data and test the program's accuracy. An understanding of the open Google Streetview API will also be necessary, since GeoGuessr relies on them for imagery. Google Streetview data comes down in tiles, which will need to be intelligently stitched to minimize distortion. Additionally, I will build a random GeoGuessr agent as a control to measure my model against.

Combining the Caffe framework with the data framework will require an understanding of CNNs and the API interface of Caffe. The Caffe framework is written in C++, and exposes a Python interface. My significant experience with Python leads to anticipate programming as a straightforward task.

To optimize the model's accuracy I will closely inspect bottlenecks to the project's performance and prioritize fixing those offering the cheapest gains. I expect to make tradeoffs in the program's design for the sake of producing results, which I will then go back and inspect closely. Such anticipated tradeoffs include: using conventional CNN structure for modeling behaviour, adopting conventional CNN hyperparameters, using country labels rather than geographic coordinates, introducing distortion when stitching photos, preventing the computer from strafing around a streetview location, and reducing the resolution of training images. I will almost certainly make more tradeoffs as the project progresses.

If my program can do better than random, I will be satisfied. My hope is that my program, given the advantage of thorough training over a large dataset with state-of-the-art image recognition algorithms, will be able to do better than the average human. In any case, I will be methodical about recording what works and what doesn't for science.

Given the computational expensive of CNN techniques, it may be beneficial for me to conduct my research on more a more powerful desktop computer.
