# Fish Food Factory

In an unrealistic, imaginary world, let's say every time you went to a grocery store, you knew when you would eat each item bought. Our program tracks users food consumption to reduce food waste.

## Authors
* Yuina Barzdukas
* Anjali Mehta
* Sara Inoue
* Mindy Zheng

## Inspiration
Our inspiration for Fish Food Factory stems from the popular game, "Kitty Collector," where players collect and care for virtual cats that possess distinct physical attributes and personalities. Our platform similarly centers around the concept of collecting animals, albeit with a focus on marine creatures. Users can obtain different sea creatures by acquiring various groceries. However, to ensure that these sea creatures remain within the user's ecosystem, it is imperative to maintain a low food waste percentage each week. Otherwise, the sea creatures will begin to depart from the ecosystem. By analyzing the user's grocery list and food consumption for the week, we are able to calculate the food waste, which serves as a determining factor for the ecosystem's overall condition. A lower food waste percentage indicates a healthier ecosystem.

## What it does
Our software enables users to effectively monitor their groceries and reduce food waste. The core feature of our program involves storing groceries and calulating food waste. Users can add groceries, which generates a list of perishable and non-perishable groceries. As the week progresses, users can input the amount of food they have consumed, and the program will automatically calculate their weekly food waste in pounds. Additionally, the program provides a visual representation of the user's food waste history through a plotted graph.

In relation to the animal collecting aspect, every new food item added to the user's list introduces a new sea creature into their virtual ecosystem. However, excessive food waste can prompt sea creatures to leave. To prevent this, our app employs Twilio to alert users when their food is nearing expiration. Additionally, users are incentivized to decrease their food waste through an award system. When users successfully reduce their food waste or make greener food choices, they earn a coveted clam medal.

## How we built it
We built our app with Python and the library, Tkinter, which helped build the GUIs.

## Challenges we ran into
Our team encountered a significant obstacle while developing our program, specifically in our use of Tkinter. Despite our collective experience with Python, we found it challenging to layer images and ensure they functioned precisely as intended.

## Accomplishments that we're proud of
We are proud in the final product of our game, which surpassed our initial expectations. We are particularly pleased with the polished appearance of the images and buttons, which add to the overall quality of the game.

## What we learned
We learned how to use Tkinter and the class system within Python (something we were not familiar with).

## What's next for Fish Food Factory
Moving forward, we have several exciting ideas to enhance our program. Firstly, we plan to imbue each animal with a unique name and personality to provide a more immersive and personalized experience for users. Moreover, we aim to expand the award system to offer a greater variety of incentives for users who actively reduce their food waste. Another planned feature is the inclusion of a recipe database, where users can save and access their favorite recipes.

Additionally, we intend to make our game accessible online, enabling users to visit their friends' ecosystems and observe what they're eating and recipes they use. Moreover, we plan to offer users the opportunity to exchange clam achievements in exchange for furniture, accessories, and food, further increasing the game's level of engagement.
