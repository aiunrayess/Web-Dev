let user = {};

user["name"] = "John";
user["surname"] = "Smith";
user["name"] = "Pete"
delete user["name"];

//
let schedule = {};

function isEmpty(schedule) {
    for(let key in schedule){
        return false;
    }
    return true;
}

alert(isEmpty(schedule));

schedule["8:30"] = "go to school";

alert(isEmpty(schedule));

//
let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
  }

let sum = 0;
for(let key in salaries){
    sum += salaries[key];
}

alert(sum);

//
function multiplyNumeric(menu) {
    for(let key in menu){
        if(typeof menu[key] == 'number') menu[key] *= 2;
    }
}

//
let obj = {};
function A() { return obj; }
function B() { return obj; }
alert( new A() == new B() ); // true

//
function Calculator() {
    this.read = function() {
      this.a = +prompt('a?', 0);
      this.b = +prompt('b?', 0);
    };
    this.sum = function() {
      return this.a + this.b;
    };
    this.mul = function() {
      return this.a * this.b;
    };
  }
  let calculator = new Calculator();
  calculator.read();
  alert( "Sum=" + calculator.sum() );
  alert( "Mul=" + calculator.mul() );

//
function Accumulator(startingValue) {
    this.value = startingValue;
    this.read = function() {
      this.value += +prompt('How much to add?', 0);
    };
  }
  let accumulator = new Accumulator(1);
  accumulator.read();
  accumulator.read();
  alert(accumulator.value);