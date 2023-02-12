# FitnessApp

An App that aids in Health Maintenance 
### Features :
- Major Basal metabolic rate(BMR)
- Know Your Body Mass Index
- Find Your Daily Calorie Needs
- Get Calorie, Fat, Protein and Sugar for your food

### GUI of Application
- [HomePage](https://github.com/Manav-56/FitnessApp/blob/main/Docs/GUI_1.png)
- [User_Choice](https://github.com/Manav-56/FitnessApp/blob/main/Docs/GUI_2.png)

## Exercise A for Advanced Software Engineering

### General
A Fitness Application is found in this repository. That user can assess their BMR(Basal Metabolic Rate), BMI(Body Mass Index), and track their calories depending on activity levels, as well as a wide range of dietary ingredients such as protein, carbs, fat, sugar, and vitamins. Furthermore, this software makes their lives easier, particularly in terms of health.

## Exercise B for Advanced Software Engineering

### 1 Git

I used Git to commit and publish my work to GitHub on a regular basis, and I did everything in my IDE (PyCharm), regularly uploading my code to GitHub through IDE. My git timings can be viewed on the GitHub [contribution chart](https://github.com/Manav-56).

### 2 UML

For this application, I produced three separate UML diagrams. If colors are used, green indicates that these features will be implemented. The purple hues indicate that the function has been activated.

- Characterize the system's dynamic characteristics An [Activity Diagram](https://github.com/Manav-56/FitnessApp/blob/main/Docs/Activity%20Diagarm.png) is essentially a flowchart that depicts the flow from one activity to another.

- A [Use Case Diagram](https://github.com/Manav-56/FitnessApp/blob/main/Docs/Use%20Case%20Diagram.png) is a visual representation of a user's potential interactions with a technology.

- A [State Diagram](https://github.com/Manav-56/FitnessApp/blob/main/Docs/State%20Diagram.png), it describes the state of the components as well as state changes caused by an event.


### 3 DDD

I created a [problem space](https://github.com/Manav-56/FitnessApp/blob/main/Docs/DDD%20Problem%20Space%20Final.png) with several subdomains that needed to be implemented for the project.  As shown in green color that part already has  been implemented, , while others will be implemented in the future, as shown in yellow color , once I will  receive the investment from Edlich.


### 4 Matrics

I utilized SonarQube, which automatically analyzes the submitted source code based on various criteria. SonarQube is an open-source tool for continuous code quality inspection that does automated inspections with static code analysis to find bugs and code smells, as well as many other Matrices.

 ###### The Following Metrics shows overall analysis of code by SonarCloud :

- Maintainability Rating : [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Security Rating : [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Bugs : [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Vulnerabilities :[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Duplicated Lines (%) :[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Reliability Rating :[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Lines of Code :[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Code smells :[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)
- Technical Debt [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Manav-56_FitnessApp&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Manav-56_FitnessApp)

Quick overview of SonarCloud analysis can be found [here](https://sonarcloud.io/summary/overall?id=Manav-56_FitnessApp).


### 5 Clean Code Development

I have included a majors [sheet](https://github.com/Manav-56/FitnessApp/blob/main/files/sheet.py) that I used when completing this application. This project was created with the Python programming language.

-  Used either ' ' or " " throught out the application develpoment. I used " " for this application. [Example](https://github.com/Manav-56/FitnessApp/blob/main/files/bmi.py#L18)
-  Use Constant for avoid re-write same code. [Example](https://github.com/Manav-56/FitnessApp/blob/main/files/bmi.py#L6)
-  Give meaningful name to variables and functions. [Example](https://github.com/Manav-56/FitnessApp/blob/main/files/bmi.py#L41)
-  Naming Conventions [Example](https://github.com/Manav-56/FitnessApp/blob/main/files/bmi.py#L182)
-  Give meaningful comment whenever possible, it allows anyones to understand your code better. [Example](https://github.com/Manav-56/FitnessApp/blob/main/files/bmi.py#L82)

### 6 Build Management

Maven is used for build management.

Just to learn how to use a building tool I wrote this Java program using Maven. However, For build in CI /CD Pipelines i utilizing GitHub Actions.

This is not a part of my FitnessApp Project, but for the purpose of build management. I wrote java code. My Java [Code](https://github.com/Manav-56/FitnessApp/blob/main/files/AppTest.java).

You can also view my [pom.xml](https://github.com/Manav-56/FitnessApp/blob/main/files/pom.xml) file, it is mentioned with all the require dependencies.

Also, you can see my successful build. [Here](https://github.com/Manav-56/FitnessApp/blob/main/Docs/Maven_Buid.png) 

I also included the project's final output with the passed test case to demonstrate that the build was successful. [Output](https://github.com/Manav-56/FitnessApp/blob/main/Docs/Maven_Test.png)

### 7 Unit-Tests

I've written a 5 test case to test each of my features before they go into production.

I've also provided a [snapshot](https://github.com/Manav-56/FitnessApp/blob/main/Docs/test_case.png) of all passed test cases.

Also, you can see my test cases [here](https://github.com/Manav-56/FitnessApp/blob/main/files/test_bmi.py).

### 8 Continuous Delivery

I utilized GitHub Actions for the continuous delivery pipeline. Every time I push to my repository, a new build is initiated, and test cases are executed.

Also, i have created 2 Jobs. 1)  Build 2)  Test

I have an attached 2 scripts files for [build](https://github.com/Manav-56/FitnessApp/blob/main/files/build.yml) and [test](https://github.com/Manav-56/FitnessApp/blob/main/files/test.yml).

You can see successful implementation of both the Jobs. For [Build](https://github.com/Manav-56/FitnessApp/blob/main/Docs/cd_build.png) and [Test](https://github.com/Manav-56/FitnessApp/blob/main/Docs/cd_test.png).




### 9 IDE 

For this application development, I utilized PyCharm as an IDE. PyCharm is a development tool for the Python programming language.

PyCharm has numerous capabilities , one of which is an integrated git plugin for committing, pushing and pulling.

Shortcuts I used while making this application :

- Ctrl + Shift + K : For Push Commit to application.
- Ctrl + k : For commit.
- Used TAB: For automatic get variable or function name  when typing.
- Ctrl +/ : Add/remove line or block comment
- Ctrl+Shift+/ : Comment out a line or block of code.







### 10 DSL

This DSL has no relevance on my FitnessApp project ( it written be in python language)

In this program, individuals can find out how much they eat in terms of calories, sugar, protein, and sugar. Overall, what they eat and how much calorie, sugar, protein, and sugar they consume on a daily basis from dawn to night. This will assist them in tracking food measurement.

The external DSL code is stored in the [.dsl file](https://github.com/Manav-56/FitnessApp/blob/main/files/fitness.dsl). The [interpreter](https://github.com/Manav-56/FitnessApp/blob/main/files/fitness.py) converts the .dsl file into Python code and runs each line.

### 11 Functional Programming

I created python code to compute BMI (Body Mass Index). It is not part of my project, however I am interested in learning about functional programming techniques.

- ### Final data structures: 
    Often known as immutables, are data structures that cannot be changed after they have been formed. Using final data structures in functional programming helps to avoid side effects and make programs more predictable. [See here](https://github.com/Manav-56/FitnessApp/blob/main/files/FP.py#L44)

- ### Side effect free functions: 
    Pure functions are those that have no side effects. They receive inputs, calculate them, and return a value without affecting any state outside of their scope. [See here](https://github.com/Manav-56/FitnessApp/blob/main/files/FP.py#L14)

- ### Higher-order functions: 
   Higher-order functions are those that accept other functions as arguments and return other functions as results. This enables you to write more abstract, reusable code. [See here](https://github.com/Manav-56/FitnessApp/blob/main/files/FP.py#L30)

- ### Functions as arguments and return values : 
    Functions can be supplied as parameters to other functions and also returned as a function's result. This enables the creation of functions that may be constructed and reused in a variety of ways. [See here](https://github.com/Manav-56/FitnessApp/blob/main/files/FP.py#L34)

- ### Closures / anonymous functions: 
    Closures are functions that continue to have access to variables defined in the scope in which they were defined after the scope has finished. Anonymous functions, also known as lambda expressions, lack a specified identifier and are frequently utilized as parameters to higher-order functions. [See here](https://github.com/Manav-56/FitnessApp/blob/main/files/FP.py#L38)






