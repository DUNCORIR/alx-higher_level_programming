#!/usr/bin/node

const request = require('request');

// Get API URL from command-line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

// Make a GET request to fetch the to-do list data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    // Parse JSON response
    const todos = JSON.parse(body);
    const completedTasks = {};

    // Loop through the tasks
    todos.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    console.log(completedTasks);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
