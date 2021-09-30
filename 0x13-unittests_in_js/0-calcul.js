function calculateNumber(a, b) {
  // round a, b to the highest number, add together and return the sum
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);
  return roundedA + roundedB;
}
module.exports = calculateNumber;
