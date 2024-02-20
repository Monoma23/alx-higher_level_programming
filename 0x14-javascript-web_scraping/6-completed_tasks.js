#!/usr/bin/node
const request = require('request');
const myurl = process.argv[2];

request.get(myurl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const mytodos = JSON.parse(body);
    const mycompletedTasks = {};
    mytodos.forEach(todo => {
      if (todo.completed) {
        if (mycompletedTasks[todo.userId]) {
          mycompletedTasks[todo.userId] += 1;
        } else {
          mycompletedTasks[todo.userId] = 1;
        }
      }
    });
    console.log(mycompletedTasks);
  } else {
    console.log(err);
  }
});
