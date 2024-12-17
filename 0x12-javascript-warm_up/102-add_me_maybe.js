#!/usr/bin/node

// Define the function
function addMeMaybe(number, theFunction) {
    const incrementedValue = number + 1; // inctrease number
    theFunction(incrementedValue); // Call function with incremented value.
}

// Export function to make it visible outside
module.exports = { addMeMaybe };
