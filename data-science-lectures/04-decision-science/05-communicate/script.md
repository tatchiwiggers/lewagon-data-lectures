# COMMUNNICATE
Good morning, everyone. Welcome to your final day of Decision Science. Congratulations for getting through this tough week. Today is a bit more chill. I mean, a bit more fun in terms of what I'm going to expect from you tonight. You're going to present in a notebook based slides the presentation of the the result of your analysis of the last four days. And that's why the lecture of the day is about communication. So I'll today give you tips on how to present and how to communicate as a data scientist.

# Where are we now? What have we seen/done/studied?
we've seen from the beginning of the week the importance of cleaning your data and coding in a repository, your project so that you can call your methods and function that you have defined earlier. And the importance of multivariate regression. To better understand your data, make it speak for you and explain kind of intuitively the importance, the influence of a variable over another one. So today the program is cost benefit analysis, how to present a trade off in a visual and meaningful manner, synthesize your results and thoughts and communicate them well as a data scientist. 

# 1. Why communication?
So why communication in data science particularly? 

# (Typical interview question for Data Science and Analytics jobs)
I'd like to share a typical interview question for data scientist that you get if you apply for a for a job, maybe after the bootcamp. Tell me about a project where you actually changed the course of action of your business or your company because of your data. 
So it's not just analyzing data, but it's activating your analysis to make other people change their mind or make a decision. 
So your role is to make the data speak and then influence others. Thanks to your result, we call it data science as a U-turn. For that, you'll have to collaborate with other data scientists, Product manager that analysts and other engineers and your code will have to be readable by others and improved by others, so I'll teach you a bit how to kind of document your code so it can be replicated. Once you have finished the project or left the company. 

# 2. Qualities of a Well-Communicated DS Project
So what are the qualities of a well-documented data science project? 

# Make the complex easy to understand
First and foremost make the complex easy to understand. So it's very easy to take half an hour to explain something. It's much harder to explain the same thing in five minutes. For example, who here can summarize in one sentence the P value. Well, when you understand something. Well that you can explain it even better. 
Here is a nice quotation from a French philosopher that says: "What is well understood will be explained clearly and the words to say it come easily". But that's not all. You also have to be very concise because in today's businesses, no one really has a lot of time to hear you explain all the details of your data science model. And we need to basically start with the preconceived idea that no one has time. And then if they do have time, then good for you. But starts with this axiom. You don't have a lot of time to say what you want, so go to the essential. 

### In statistics, the p-value is the probability of obtaining results at least as extreme as the observed results of a statistical hypothesis test, assuming that the null hypothesis is correct ###

# Follow the Pyramid Principle
So how to do that in the frame of a data consulting project?
Follow a pyramid principle when you answer a data consulting project. So the pyramid principle basically tells you to start with the answer of the question and then only explain why instead of doing a deductive logic where you really explain your how you went to this answer. And it's a storytelling sort of way to tell your results. So if you only have ten minutes to convince an audience that this is what they should do, apply the pyramid principle.

# 👉 Action/Answer first, explain why after!
So what's the pyramid principle? It's on the right side here. It's the action. Action first - explain why after. And it's efficient under time constraints. It's an inductive approach which is different from the deductive one.

The deductive approach it could be used for starting with what's wrong? So Olist is not making a great deal of revenue because it's reviews are quite low. What's causing it? We've seen that wait time may be an issue or no. Maybe it's the delay. So do we have sellers that take a longer time to deliver a product than others? So after analyzing the seller I finally realize that maybe some sellers are really bad and should be removed from the platform. So this is my final argument and my answer comes at the end. 

 In an inductive approach, you would do the opposite. Basically, you should remove your worst performing seller from your platform. How? By removing the one who has the lowest reviews, removing the one that takes the longest time to deliver, and so on... And for each argument, explain why. So you see, you go in a cascading downward pyramid that is called the pyramid principle.

 # CREATE A PYRAMID WITH YOUR ANSWER AND SPPORTING ARGUMENTS
So what does it look like, for instance, in a real project? This is typically the type of question you would have as an interview for consulting strategic consultant. You would say, how can I reduce the cost by 5 million? So you improve my operational margin for a company and then you give the three main answers:
- first, so you can outsource some function, 
- then you can simplify core functions, 
- and finally review your supplier costs,
and then for each of them, explain how you do that. 

So the idea here is to have less or at max three arguments per solution. Well this is just the rule of thumb. Feel free to apply it or not. But it's a good template to keep in mind. And the nice thing also with induction pyramids like this is that sometimes when you've already seen cases like that and you want to try to answer quickly before diving into a long deductive approach, you can start directly by an idea, a preconceived idea of the solution in the form of a tree like this. And just check if your intuition is atrong -  and if your intuition happens not to like to this specific problem, then just cut one branch of the tree. And so you would have only two thirds of the tree here. And then you would focus on the on the two aspects here. And maybe both will be a good solution. Or maybe you can discard one more and only keep the last one. So it's a kind of a quicker way to answer a problem when you already have seen similar problem in the past. You know, it's kind of applying a template of reasoning to to go quickly to the solution. 

# SLIDE TO BE PRODUCED
so this is how a pyramid principle would be put back into slides, an introduction which just very briefly explains what was the question that was asked so far at least, how can I improve customer satisfaction while preserving operational margin? And then slide two, boom directly? Your answer. You answer with maybe a small induction tree that shows you know everything about your presentation in one slide. You can show the tree. And then you go branch by branch in your presentation. Slide three You start with your first branch and then you explain your supporting argument. Then you're back up one level to your second branch and then down one level to your supporting argument etc...

So don't start to tell a story. It's not going to work in five minutes.I mean, straight to the point. The Pyramid principle works and it works quite well. 

# 3. Insist on Trade-Offs 9mins
what is a trade off? A trade-off is a situational decision that involves diminishing or losing one quality, quantity, or property of a set or design in return for gains in other aspects. In simple terms, a tradeoff is where one thing increases, and another must decrease.
You can present them the, the cost benefit analysis and some trade offs between this option, A, option B, option C, And if you present it in a nice way, then they be able to choose for you. It can even be done during the presentation, but it has to be very nicely packaged.
So that everything is intuitive. The decision making process shouldn't be long and shouldn't require pen and paper equation solving, etcetera. So present on a plate, a different options and let your project the one who sold the who asked you to solve the question answer for you. So let's take one example. 

# 🥋Let's take an example:
So you are working in a in a in a data science company and your product manager comes with an idea to increase conversion rate on the website. You can think about Olist. Conversion rate is the ratio between people who buy something when they connect to your site over the total number of people who connect. 

Say your website today has 100,000 visitors per month and each visitor on average provides 20 reals of benefits. Okay. You also have a team of three engineers that costs $500 each per day. So basically you have a 1500 reals per day cost for if you were to use this team to develop the feature that the product manager wants you to develop. Okay. So I don't know personally how long it will take to code the feature because I just have an idea of the feature I want to create in the website. And I don't know the lift either, that is, the the increase in terms of conversion rate. So I will have to make hypothesis about it. Ask my PM to give me a range of days or my team to ask my team of engineers to give me a range of days it should take to code this feature from, let's say 20 days to 60 days and then ask the product manager to give me an estimate also of the of the lift this feature could make in terms of conversion rate. So maybe a 1% increase, two, three, four, 5% increase. So I have an order of magnitude of the time it will take to code it and an order of magnitude of the improvement in in lift that this feature can can make. And so what I want to create now is sort of a sensitivity matrix between the number of days it will take to code it and the improvement it will make to the platform. So we'll try to do that together. 

### Sensitivity analysis is the study of how the uncertainty in the output of a mathematical model or system (numerical or otherwise) can be divided and allocated to different sources of uncertainty in its inputs.
### where S is the sensitivity matrix containing all derivatives of the model responses (temperatures, pressures, and vapor mole fractions) with respect to the parameters, and Σ is a matrix holding all variances of the measurements on its diagonal.

# Step 1️⃣ - Model Benefits
 First things I want to do is think about the potential benefits of this new feature. And my project manager told me that the potential lift is between 1 and 4%. 
 #### change
 So what I could do is compute for each lift between 1 and 4%. So one, two, three, 4%. I could compute. The hypothetical benefits it would create for my company. Because if I increase by 1% my conversion rate, given that I have 100,000 people per month, which each bring on average €20. If I increase it by 1%, then I get the 20,000 real benefits. If this feature were to increase my conversion rate by 2%, I would gain 40,000. 3%. 60,000. 4%. 80,000. Just rule of thumbs here. So I have a range of potential benefits for this new feature. And I'm going to do the same with the costs. 

 # Step 2️⃣ - Model Costs
 I will model costs which is proportionate to the number of days spent by my engineering team. And we as a team estimated it would take between 20 and 50 days. Okay. You know, it's an oversimplified problem, but that's the point of the morning lecture, right? 
 ### change
 So I can compute exactly the same things in terms of if it were to take 20 days, how much would it cost? Just the number of manday times The daily salary of my engineer, and there are three engineers. So basically I have a small table here which tells me 20 days should cost 30,000. Up to 50 days would cost 75,000. Okay. So far, so good. 

 # Step 3️⃣ - Sensitivity Matrix
 ### manday - a day regarded in terms of the amount of work that can be done by one person within this period.
 And the ID that I want us to do and to live code together is to come to sort of a sensitivity matrix. It helped me to see the trade off. So I want to end up with a result in pink like here, where basically I would have the lift on the x axis, the potential mandate it would take. And all the combination of lift and manday that would give me costs and benefits. And if I do the difference, I get either a profitable initiative here or a very costly initiative here. Okay. So this is like illustrating the trade off that I mentioned before.
 So this is like illustrating the trade off that I mentioned before. So you present that to your manager and you say, should we take the risk of developing this feature now? We know in which region it would be profitable and in which region based on the time and lift it would be a mistake to develop it.

 But right now we only have two tables like this left and right. So this is a benefit table and the cost table. So how to how to go from these to small table here to the sensitivity table at the top. Sensitivity has a 16 figures to compute here. 4x4. Here I only have four and here I only have four. I'll show you how you can do this with Pandas.

 And here we need to compute sort of every combination of leaf time mandays, right? For each combination of the two. We need to compute the cost and benefits. Trying to compute every combination between this table and that table is called a Cartesian product. So I have a four element here and four element here.
 
# Step 3.1
What I want to start with is something like this. I want to create an intermediary table that takes all the mandays here, 20 mandays, 30 mandays, 40, 50. And for each mandays I will take all the combination of lift one, two, three, four. Then one, two, three, four. And once I have this, I have my 16 different costs and benefits. And then we'll create the arrow by doing the subtraction. So I want to cut that together and ask you a bit. 
So  to move from this to this table here i should merge the data frame on a column that is similar in both data tables.

So that's what I'm going to do. I'm going to create The columns of ones for both costs and benefits. And when I have a column of ones , I'm going to do a merge on cost and benefits. So costs.benefits or pandas.merge cost benefits and I'm going to do it on the columns of ones and this will create every 16 combination of potential lift and benefits. So I don't need the ones column after the merge. So I just drop it and I get this combination of Cartesian product. 
And I can then compute the ROI between cost and benefits or return on investments for ROI, which is simply the difference between benefits and cost. So I am naming this as this is kind of. The matrix of 16 arrow that I now want to make in a square 4x4 dimension as shown here. And so this is called pivoting. So I don't think we've seen that so far. So it's important that we discuss we discuss it here.