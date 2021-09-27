const fs = require('fs');

function countStudents(path) {
  try {
    const readAllFile = fs.readFileSync(path, 'utf8');
    const lines = readAllFile.split(/\r?\n/);
    let stuCount = 0;
    lines.forEach((line) => {
      stuCount += 1;
    });
    const listFirstName = lines.map((line) => {
      const students = line.split(',');
      return students;
    });
    console.log(`Number of students: ${stuCount}`);
  } catch (err) {
    throw Error('Cannot load the database');
  }

  // const field = fs.readFileSync(path, 'utf8');
  // const fieldNum = fs.readFileSync(path, 'utf8');
  // console.log(`Number of students in ${field}: ${fieldNum}. List: ${listFirstN}`)
}
module.exports = countStudents;
