const fs = require('fs');

const countStudents = (path) => {
  return new Promise((resolve, reject) => {
    fs.readFile(path, (err, readAllFile) => {
      if (err) {
        reject(err);
        throw Error('Cannot load the database');
      }
      // resolve(readAllFile);
      let lines = readAllFile.split(/\r?\n/);
      lines.shift();
      lines = lines.filter(line => line !== '');

      console.log(`Number of students: ${lines.length}`);
      
      const csField = lines.filter((line) => line.endsWith('CS')).map((line) => {
        const student = line.split(',');
        return student[0];
        });
      console.log(`Number of students in CS: ${csField.length}. List: ${csField.join(', ')}`);
      const sweField = lines.filter((line) => line.endsWith('SWE')).map((line) => {
        const student = line.split(',');
        return student[0];
        });
      console.log(`Number of students in SWE: ${sweField.length}. List: ${sweField.join(', ')}`);  
    })
  }
)}
module.exports = countStudents;
