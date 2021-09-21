export default function getListStudentIds(stuArray) {
  let result = [];
  if (!Array.isArray(stuArray)) {
    return result;
  }
  result = stuArray.map((x) => x.id);
  return result;
}
