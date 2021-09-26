// Welcome message, read name input and display name string to stdout

console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  while (name !== null) {
    process.stdout.write(`Your name is: ${name}`);
  }
});
process.stdin.on('close', () => {
  process.stdout.write('This important software is now closing\n');
  process.exit();
});
