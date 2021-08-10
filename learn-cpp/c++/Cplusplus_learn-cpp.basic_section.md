
# Learn-CPP: C++

**Link:** https://www.learn-cpp.org/en/Hello%2C_World%21

C++ is considered an "intermediate" programming language as it has features of high-level and low-level languages. It provide *imperative*,*object-orientated* & *generic* programming features.



## Our 1st program

Every C++ program uses libraries, which give the ability to execute necessary functions. Ie most basic is `cout`, which prints to screen, and is defined in the `iostream` header file.

To be able to run `cout`, we must include the following directive to our first line of code:

```
#include <iostream>
using namespace std;
```

The second part is the actual code we're going to write. The 1st code to be run will always reside in the `main` function:

```
int main() {
  YOUR CODE HERE
}
```

Here, `int` is a **keyword**, which indicates the function `main` returns an integer. The number returned by our function indicates whether the program we wrote worked correctly. If we want to say that our code was run successfully, we will return 0. Greater than 0 means it failed.

For this tutorial, we will return 0 to indicate that our program was successful:

```
return 0;
```

Every line of C++ ends with a semicolon so the computer knows a new line has started. Will also need to use redirection to the `cout` stream to print our sentence.


## Exercise

Change the program in the bottom in a way so that it prints to the output "Hello, world!".

```
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!" << std::endl;
  return 0;
}
```



## Variables & Types

### Data Types

C++ provides a rich set of built-in and user-defined data types. 7 basic data-types are;

* Boolean - `boolean`, `true` of `false`.
* Characters - Alphabets & all symbols, defined with `char`.
* Integers - Whole numbers which can be +ve or -ve, defined with `int` (4 bytes), `short int` (2 bytes) & `long int` (8 bytes) based on the size of the numbers used.
* Floating point numbers - real numbers (numbers with fractions), defined as `float` & `double`.
* Valueless using the `void` keyword.
* Wide character using the `wchar_t` keyword.

### Type modifiers

Can be modified with the following modifiers: `signed` & `unsigned`, `short` & `long`.

### User-defined

* Structures - `struct` - explained later in *Structures* section
* Classes - `class` - explained later *Classes* section

C++ allows an array of characters to define strings. Also provides and extensive `string` library for manipulating strings, explained in the *Strings* section.

### Typedefs

These allow for creating new names (think of them as aliases) for existsing types. Below is the simple syntax to define a new type using `typedef`:

```
typedef int counter;
counter tick_c = 100; // tick_c is a valid integer variable
```

### Enumerated types

To create an enumeration requires the use of the keyword `enum`, general form is:

```
enum enum_name { list, of, names, } var_list;
```

Where the `enum_name` is the enumeration's type. Below defines an enumeration of colours called colours and the variable `a_colour` of type colour. Finally, `a_colour` is assigned the value "green":

```
enum colours {red, green, blue} a_colour, another_colour;
a_colour = green; // a_colour will be assigned value of '1'
```

### Defining Variables

For numbers, usually use the type `int` in the size of a "word", the default number size the machine which you program is compiled on. Ie 32-bit, 64-bit, meaning numbers can range from -2,147,483,648 to 2,147,483,647.

To define variables `foo` & `bar`, we need to use the following syntax:

```
int foo;
int bar = 1;
```

The variable `foo` can be used, but since we don't want to initialise it, we don't know whats in it. The variable `bar` contains the number 1. Now we can do math, assuming `a`, `b`, `c`, `d` & `e` are variables we can simply use `+`, `-` & `*` operators and assign a new value to `a`;

```
int a = 0, b = 1, c = 2, d = 3, e = 4;
a = b - c + d * e;
cout << a << endl; // will print 1 - 2 + 3 * 4
```



## Arrays

## What is an array

An array is a grouping of the same type of variables (ie `int`, `char`) clubbed together. An array declaration is;

```
<type> Name[no of elements];
```

eg for numeric array with 5 elements:

```
int marks[5];
```

We can initialize the array by giving the array values via;

```
marks[0] = 96;
marks[1] = 92;
marks[2] = 78;
marks[3] = 54;
marks[4] = 86;
```

So the entire code for declaring and initialising would be;

```
int marks[5];
marks[0] = 96;
marks[1] = 92;
marks[2] = 78;
marks[3] = 54;
marks[4] = 86;
```

Or in a single line as

```
int marks[5] = { 96, 92, 78, 54, 86 };
```

OR

```
int marks[] = { 96, 92, 78, 54, 86 };
```

Can access the elements of the array using `[]`. They are **zero-indexed**;

```
cout << marks[0] << endl;
```

Can print the entire array with a for loop;

```
for (int i=0,i<5;i++)
{
  cout << marks[i] <<endl;
}
```

Works for `char` too:

```
char keys[6] = {'a','b','c','d','e','f'}
```



## Strings

### Two types of string

In traditional C, they are just arrays of char-values (char, wchar_t).

In C++, strings are represented as objects which offer some comfortable ways to work with these type of data. Are implemented in the standard library `str::string`, which must be referenced (#include) in the program

### Examples:

```
#include<iostream>
#include<string>
using namespace std;
int main()
{
    string sometext="This is a new text"; //Declaring a string

    cout << "Initial value of sometext is: " << sometext << endl;  //Writing the initial text to the console.
    //Note: that endl isn't needed to show the value on the console, but adds a new line at the end

    getline(cin, sometext);  //Reading textinput from the keyboard

    cout << "You entered: " << sometext << endl;  //Writing the given text back to the console.

    return 0;
}
```



## if-else

### if statement

General syntax is;

```
if (condition)
{
  // My code
}
```

eg below prints "The one I searched for" if `num` is 4.

```
if(num == 4)
{
    cout << "The one i searched for" << endl;
}
```

The following example prints "Number is Even" if num is a even number i.e. num % 2 == 0

```
if(num % 2 == 0)  // % is a modulo-operator, which returns the remainder of a division. on even numbers it will return 0
{
    cout << "Number is Even"<< endl;
}
```

### else statement

Else statement preceded by an if block and the block in the else statement is executed only if the if statement fails.

```
if(num % 2 == 0)
{
    cout << "Number is Even"<< endl;
}
else
{
    cout << "Number is not Even" << endl;
}
```

The above code prints "Number is Even" for all even numbers and "Number is not Even" for odd numbers.

Can next if-else statements:

```
if(num % 2 == 0)
{
    cout << "Number divisible by 2" << endl;
}
else if(num % 3 == 0)
{
    cout << "Number divisible by 3" << endl;
}
else
{
    cout << "Bad Number" << endl;
}
```

The above code checks for 2 divisibility, and if the number is not divisible by 2, it checks for 3 divisibility and if not divisible by 3 also, it prints "Bad Number".



## For loops

Execution of a loop can be controlled using the following keywords;

  * `break` - terminates the loop/switch statement and transfers execution to the statement directly after the loop
  * `continue` - which causes the loop to process to the next element, skipping the current one.
  * `goto LABEL` - transfers control to the specified label. ADVISED NOT TO USE THIS STATEMENT

If we know the exact number of times to repeat the loop, we use a *for loop*. Syntax has 4 parts:

1. Initialisation
2. Test expression
3. Modifying the expression
4. Code block to be executed

```
for (initialisation; test condition; update) {
  // Body of loop - code to run
}
```

ie:

```
for(int i=0; i < 10; i++)
{
  cout << "Hello C++" << endl
}
```

Where `i` is a *loop variable* which is initialised at 0. If the test condition turns out to be true we continue the loop and execute the body. After each iteration, the modifying expression is run (`i++` in the above). Continue doing this until the test condition isn't true.

Can initialise `i` separately, and update it in the code chunk, like;

```
int i = 0;
for( ; i <10; )
{
  cout << i << endl
  i++;
}
```

Can also use loops to iterate over arrays:

```
// fetch each array-element and print it out
int arr[] = {1,2,3,4,5,6};

for (int n : arr)
{
  cout << n << endl
}

/*
  Warning: the example above will reference the original memory of arr[] and has write-access!

  As you often don't need to write to that address-space, you should consider to access it read-only for safety reasons.
  To avoid write-access, you might consider using a const-reference like shown below,
  which will create a constant -and therefore unchangeable- reference named "n" to each existing value of "arr",
  effectively referncing the values read-only.

  You'll learn more about reference's and pointer's in the next chapters.
*/

// fetch each array-element and print it out (readonly)
int arr[] = {1,2,3,4,5,6};

for(const int& n : arr)
{
    cout << n << endl;
}
```



## While loops

A *while* loop will repeat a statement or a group of statements while a given condition is true.

```
//Guessing game
#include <iostream>
using namespace std;
int main (void)
{     
    int searched = 5;  //The value we're searching
    int given = -1; // The variable to which we'll write user's guesses

    //Greet the user:
    cout << "This is simple guessing game:" << endl;
    cout << "Please enter a number:" << endl;

    //This while-loop will terminate when the user entered the searched value
    while (searched != given) {
        cin >> given;  // Read a value from the keyboard

        /*
        Note, that the following line(s) within the loop-brackets
        will also execute if the user guessed correctly.
        Checking will be done at the start of the next iteration
        */

        cout << "Thank you for your guess..." << endl;  
    }
cout << "You found the correct number. Good bye." << endl;
return 0;
}

// Some while with continue- and break-statements
#include <iostream>
using namespace std;
int main (void)
{     
    int count = 200;  // The start value
    int destination = 0;  // the destination

    // This while will normally terminate when count reaches the destination-value
    while (count > destination) {  
        count--;  // decrement count

        if (count == 190) { // If count will turn into 190...
            cout << "skipped..." << endl;
            continue; //... the while-loop will skip to the next iteration due to the "continue"-statement.
        }

        if (count < 180) { // If count falls below 180...
            cout << "aborted..." << endl;
            break; //... the while-loop will be aborted due to the "abort"-statement.
        }
        cout << count << endl;  //Note, that this will also execute when target is reached
    }

return 0;
}
```

### Exercise

Try to print all the numbers from 1 to 20 in ascending order using a while loop.

```
#include <iostream>
using namespace std;
int main (void)
{     
        int target = 20;  //The target value
        int counter = 0;  // Counter
        while(counter <= target) {
          cout << counter << endl;
          counter++;
        }

return 0;
}
```



## Functions

Functions take inputs (parameters) and process and return them as an output. General format in C++ is:

```
type name_of_function (p1, p2,... ) {
  statements
}
```

* `type` - Type of variable the function returns
* `name_of_function` - Name of function
* `pn` - Input parameters. Identify the data type then name, separate with `,` for multiple inputs
* `statements` - Lines of code that will perform the function's task

To call a function, write its name with paranthesis following, with parameters within.

```
int squareNumbers(int x){ // Declares function "squareNumbers" that takes in parameter of x.
    y=x*x; //creates int variable equating to x squared
    return y; //returns the value of y when the function is called
}

int main(){
    input = 9;
    output = squareNumbers(input);
    //the function is called, resulting in the int variable "output" equating input squared
}

```


```

void helloThere(string name){//void means this function doesn't return anything
    cout << "Hello, " << name;
}

int main(){
    helloThere("Celina"); //prints out "Hello, Celina"
}

```

### Exercise

In this excercise, you will create a function that prints out the sum of the given variables, a, b, and c. Below is the given code.
