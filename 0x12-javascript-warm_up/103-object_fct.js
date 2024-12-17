#!/usr/bin/node
const myObject = {
    type: 'object',
    value: 12,
    incr: function () {
        this.value += 1; // Increment the value property
      }
  };
  console.log(myObject); // Initial object
  
  myObject.incr(); 
  console.log(myObject);  // After first increment
  myObject.incr();
  console.log(myObject);  // After second increment
  myObject.incr();
  console.log(myObject);  // After third increment
