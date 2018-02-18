/***
    ES6 CONST/LET EXAMPLES
***/

//Example of Scoping difference. Using "var", the variable is declared at the top of the scope, but initialized with a value at the line it was typed. It is given a value of "undefined" until it is initialized with it's actual value. By comparison, Let/Const are defined and initialized on the same line.

//using var
function logger(){
  console.log(x); //returns "undefined", but code still runs.
  var x = "hi";
}
logger();

//using let
function logger2(){
  console.log(y); //ReferenceError: y is not defined . Code will stop execution.
  let y = "hello"
}
logger2();

//Example of const for constant value

//this value is constant, and will refuse attempts at re-assignment.
const myPets = ["dog", "cat", "rabbit", "some endangered species of sea turtle"];

myPets = "ferret"; //This will not work

myPets = ["wolf", "giraffe", "parrot"]; //This will not work either


//HOWEVER, we can still manipulate Objects and Arrays! See below example.
console.log("before: ", myPets);
myPets.pop();//FREE THE TURTLES!!!
console.log("after: ", myPets);


/**
 * forEach
 */

// forEach - basic
function printOne(number) {
  console.log(number);
}

var arr = [1, 2, 3, 4, 5];

// call a function on each item in the array
arr.forEach(printOne);


// forEach with index
function printWithIndex(number, index) {
  console.log(index, number);
}

arr.forEach(printWithIndex);

/**
 * map - functional programming
 */

var theStagesOfJS = ["denial", "anger", "bargaining", "depression", "acceptance"];

// map
theStagesOfJS.map(function(item){
  return item;
});

theStagesOfJS.map(function(item, index) {
  return `Stage ${index + 1}: ${item}`;
});

// Note: The original array is unchanged
console.log(theStagesOfJS);

// map vs forEach
theStagesOfJS.forEach(function(each, index) {
  // the return of forEach is ignored
  return `Stage ${index + 1}: ${each}`;
});

theStagesOfJS.forEach(function(each, index) {
  // you have to mutate the orignal array with forEach
  theStagesOfJS[index] = `Stage ${index + 1}: ${each}`;
});


var bestActors = [
  {name: "Nic Cage", age: 54, knownFor: "Con Air"},
  {name: "Keanu Reeves", age: 53, knownFor: "The Matrix"},
  {name: "Betty White", age: 96, knownFor: "Lake Placid"},
  {name: "Patrick Warburton", age: 53, knownFor: "The Tick"}
];

bestActors.map(function(actor) {
  return actor.knownFor;
})

/**
 * Arrow Functions
 */

// Function Expression
var multiply1 = function (a, b) {
  return a * b;
}

// Arrow Function Expression
var multiply2 = (a, b) => {
  return a * b;
}

multiply2(2, 3); // 6 - called the same way as usual

// Arrow Function Expression - concise
var multiply3 = (a, b) => a * b;
// without curly brackets, the return statement is implied

// can omit the parenthesis if there's only a single parameter
var square = x => x * x;


// Note: there's no arrow-function equivalent of function declarations
function multiply4 (a, b) {
  return a * b;
}

// ¯\_(ツ)_/¯


var princesses = [
  { name: "Rapunzel", age: 18 },
  { name: "Mulan", age: 16 },
  { name: "Anna", age: 18 },
  { name: "Moana", age: 16 }
];

// log the name of each princess, follow by a colon, followed by their age
// forEach: executes a provided function once for each array element
princesses.forEach(princess => console.log(`${princess.name}: ${princess.age}`));

// create an array of just the names from the princesses array
// map: creates a new array with the results of calling a provided function on every element in the calling array
var names = princesses.map(princess => princess.name);
console.log("names: ", names);

// using the `names` array, get only those names that start with an 'M'
// filter: creates a new array with elements that pass the test of the provided function
var mNames = names.filter(name => name.startsWith("M"));
console.log("m-names: ", mNames);
