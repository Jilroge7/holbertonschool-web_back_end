export default function createInt8TypedArray(length, position, value) {
  if (value < -128 || value > 127) {
    throw Error('Position outside range');
c }
}
