export default function getStudentsByLocation(stuArray, city) {
  let filtered = [];
  if (!Array.isArray(stuArray)) {
    return filtered;
  }
  filtered = stuArray.filter((x) => x.location === city);
  return filtered;
}
