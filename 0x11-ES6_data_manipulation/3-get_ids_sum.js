export default function getStudentIDsSum(stuArray) {
  if (!Array.isArray(stuArray)) {
    return [];
  }
  const reducer = (preValue, currValue) => preValue + currValue;
  const idSum = stuArray.map((x) => x.id).reduce(reducer);
  return idSum;
}
