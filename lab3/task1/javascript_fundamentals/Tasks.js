let name = "Ainur";
alert( `hello ${1}` ); // hello 1

alert( `hello ${"name"}` ); // hello name

alert( `hello ${name}` ); // hello Ainur


//
let a = 1, b = 1;
alert( ++a ); // 2, prefix form returns the new value
alert( b++ ); // 1, postfix form returns the old value

alert( a ); // 2, incremented once
alert( b ); // 2, incremented once


//
let d = 2;
let x = 1 + (d *= 2);
    // d = 4 (multiplied by 2)
    // x = 5 (calculated as 1 + 4)



//  
"" + 1 + 0 = "10";
"" - 1 + 0 = -1 ;
true + false = 1;
6 / "3" = 2;
"2" * "3" = 6;
4 + 5 + "px" = "9px";
"$" + 4 + 5 = "$45";
"4" - 2 = 2;
"4px" - 2 = NaN;
"  -9  " + 5 = "  -9  5"; 
"  -9  " - 5 = -14 ;
null + 1 = 1 ;
undefined + 1 = NaN ;
" \t \n" - 2 = -2 ;


//
let a = +prompt("First number?", 1);
let b = +prompt("Second number?", 2);

alert(a + b); // 3



//
5 > 4 // true
"apple" > "pineapple" // false
"2" > "12" // true
undefined == null // true
undefined === null // false
null == "\n0\n" // false
null === +"\n0\n" // false



//
let value = prompt('Type a number', 0);

if (value > 0) {
  alert( 1 );
} else if (value < 0) {
  alert( -1 );
} else {
  alert( 0 );
}



//
let result = (a + b < 4) ? 'Below' : 'Over';


//
let message = (login == 'Employee') ? 'Hello' :
  (login == 'Director') ? 'Greetings' :
  (login == '') ? 'No login' :
  '';


//
alert( null || 2 || undefined );
//2
alert( alert(1) || 2 || alert(3) );
//1, 2
alert( 1 && null && 2 );
//null
alert( alert(1) && alert(2) );
//1
alert( null || 2 && 3 || 4 );
//3
if(age >= 14 && age <= 90)

if(!(age >= 14 && age <= 90))
if(age < 14 || age > 90)

if (-1 || 0) alert( 'first' ); // will run
if (-1 && 0) alert( 'second' ); // will not
if (null || -1 && 1) alert( 'third' ); // will run

let login = prompt("Who is there", '');
if(login == "Admin") {
  let password = prompt("Password?", '');
  if(password === "TheMaster"){
    alert("Welcome!");
  } else if(password === '' || password === null) {
    alert("Caneled");
  } else {
    alert("Wrong password");
  }
} else if(login === '' || password === null){
  alert("Canceled");
} else {
  alert("I don't know u");
}

//
let i = 3;

while (i) {
  alert( i-- );
} // shows 1 as last

//
let i = 0;
while (++i < 5) alert( i );
//shows from 1 to 4

let i = 0;
while (i++ < 5) alert( i );
//shows from 0 to 4

//
for (let i = 0; i < 5; i++) alert( i );
for (let i = 0; i < 5; ++i) alert( i );

//both will show from 0 to 4

//
for(int i = 2; i <= 10; i+=2){
    alert(i);
}

//
let i = 0;
while(i < 3){
    alert(`number ${i++}`);
}

//
let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);


//
let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) { 

  for (let j = 2; j < i; j++) { 
    if (i % j == 0) continue nextPrime; 
  }

  alert(i); 
}


//
if(browser == 'Edge') {
    alert("You've got the Edge!");
  } else if (browser == 'Chrome'
   || browser == 'Firefox'
   || browser == 'Safari'
   || browser == 'Opera') {
    alert( 'Okay we support these browsers too' );
  } else {
    alert( 'We hope that this page looks ok!' );
  }


//
switch (a){
    case 0:
        alert(0);
        break;
    case 1:
        alert(1);
        break;
    case 2:
    case 3:
        alert("2, 3");
        break;
}


//
function checkAge(age) {
    if (age > 18) {
      return true;
    } else {
      // ...
      return confirm('Did parents allow you?');
    }
  }

function checkAge(age) {
    if (age > 18) {
      return true;
    }
    // ...
    return confirm('Did parents allow you?');
  }


//no, cuz return already does the else's function 


//
function checkAge(age) {
    return (age > 18) ? true : confirm("Did your parents allow you?"); 
  }

function checkAge(age) {
    return (age > 18) || confirm("Did your parents allow you?"); 
  }


//
function findmin(a, b){
    if(a < b) return a;
    else return b;
}


//
function pow(x, n) {
    return x**n;
  }
  
  let x = prompt("x?", '');
  let n = prompt("n?", '');
  
  if (n < 1) {
    alert(`Power ${n} is not supported, use a positive integer`);
  } else {
    alert( pow(x, n) );
  }



//
function ask(question, yes, no) {
    if (confirm(question)) yes();
    else no();
  }
  
  ask(
    "Do you agree?",
    () => alert("You agreed.");
    () => alert("You canceled the execution.");
  );