// Welcome message, read name input and display name string to stdout

console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('readable', () => {
  let name;
  while ((name = process.stdin.read()) !== null) {
    process.stdout.write(`Your name is: ${name}`);
  }
});
process.stdin.on('close', () => {
  process.stdout.write('This important software is now closing\n');
  process.exit();
});