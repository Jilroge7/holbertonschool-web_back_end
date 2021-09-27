// Server structure, reads database asynchronously
const fs = require('fs');

function readDatabase(path) {
  try {
    const fileRead = fs.readFile(path, 'utf8');
    // return a promise
    // return an object of arrays of students' info
  } catch (error) {
    throw Error('Cannot load the database');
  }
}
module.exports = readDatabase;