const fs = require('fs');

function countStudents(path) {
  try {
    const readAllFile = fs.readFileSync(path, 'utf8');
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
  } catch (err) {
    throw Error('Cannot load the database');
  }
}
module.exports = countStudents;
