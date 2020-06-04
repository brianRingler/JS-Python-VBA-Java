***
# Fun with Programming 
***

I have been learning JavaScript over the last couple weeks and it is helping me learn more about Python. 
As well, become a better programmer. Not just because it's another language in my tool kit. Rather, its helping me 
understand programming at a deeper level.  As I am working through JS, I am associating it with Python. By noticing the 
similarities and differences it is helping me understand Python better and understand programming concepts at a deeper level.  
For example, lets take a look at a simple JS constructor and Python class. One thing to note is with Python we could replace `self` with any word.
However, it is common Python convention to use `self`.  

```
// JavaScript Constructor
function Car(model, salePrice, color, yearBuilt){
    this.model = model;
    this.salePrice = salePrice;
    this.color = color;
    this.yearBuilt = yearBuilt
    this.getYears =  function() { 
        const today = new Date();
        const carAge = today.getFullYear() - this.yearBuilt;
        return carAge;
 }
}

//Create Objects
const carOne = new Car('Charger',25000,'yellow',2010);
const carTwo = new Car('Rustang',22000,'blue',1998);

//Log out objects properties and methods
console.log(carOne.model);  // "Charger"
console.log(carTwo.model); // "Rustang"
console.log(carOne.color);  // "yellow"
console.log(carTwo.salePrice); // "22000"
console.log(carOne.getYears()); // 10
console.log(carTwo.getYears()); // 22
```

# Python Class
from datetime import datetime

```
class Car():
    def __init__(self, model, salePrice, color,yearBuilt):
        self.model = model
        self.salePrice = salePrice
        self.color = color
        self.yearBuilt = yearBuilt
    
    def getYears(self):
        today = datetime.now()
        year = today.year
        return  year - self.yearBuilt

carOne = Car('Charger',25000,'yellow',2010);
carTwo = Car('Rustang',22000,'blue',1998);

print(carOne.model)  # "Charger"
print(carTwo.model) # "Rustang"
print(carOne.color)  # "yellow"
print(carTwo.salePrice) # "22000"
print(carOne.getYears()) # 10
print(carTwo.getYears()) # 22
```
***
# Super Bowl Get HTML 
***

For another fun side-by-side I want to parse a table of HTML using Python, JavaScript, VBA and Java. In the examples provided 
I have used Python to grab Super Bowl data from Wikipedia. I have provided the code for JS and Python and pull the tabe data for the
Super Bowl Champions. The data is then stored in a dict/object. I still need add a section of code in the JS script to extract 
HTML using JS. As of now, it extracts the data into an object given the entire HTML page. Additionally, the code for VBA and Jave
is still required.  

* https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
