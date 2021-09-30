function calculateNumber(type, a, b) {
  // round a, b to the highest number, add together and return the sum
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);
  if (type === 'SUM') {
  return roundedA + roundedB;
  }
  if (type === 'SUBTRACT') {
    return roundedA - roundedB;
  }
  if (type === 'DIVIDE') {
    if (roundedB === 0) {
      return 'Error';
    } else {
      return roundedA / roundedB;
    }
  }
}
module.exports = calculateNumber;
