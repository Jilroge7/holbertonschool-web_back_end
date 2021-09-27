const fs = require('fs');

function countStudents(path) {
  try {
    const readAllFile = fs.readFileSync(path, 'utf8');  
  } catch (err) {
     throw Error('Cannot load the database');
  }

  const lines = readAllFile.split(/\r?\n/);
  const stuCount = 0;
  lines.forEach((line) => {
    stuCount++;
  })
  const listFirstName = lines.map((line) => {
    line.split(',');
  })
  console.log(listFirstName);
  //const field = fs.readFileSync(path, 'utf8');
    //const fieldNum = fs.readFileSync(path, 'utf8');
    //console.log(`Number of students: ${stuCount}`);
    //console.log(`Number of students in ${field}: ${fieldNum}. List: ${listFirstN}`)
}
module.exports = countStudents;
