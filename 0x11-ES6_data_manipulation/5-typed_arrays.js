export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw Error('Position outside range');
c }
  const buffer = new ArrayBuffer(length);
  const int8View = new DataView(buffer);
  int8View.setInt8(position, value);
  return int8View;
}
