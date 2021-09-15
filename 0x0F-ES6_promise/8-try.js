export default function divideFunction(numerator, denominator) {
  let result = 0;
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  }
  try {
    result = numerator / denominator;
  } catch (e) {
    console.log(e);
  }
  return result;
}
