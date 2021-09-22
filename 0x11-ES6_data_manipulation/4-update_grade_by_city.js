export default function updateStudentByCity(stuArray, city, newGrades) {
  if (!Array.isArray(stuArray)) {
    return [];
  }
  const stuByCity = stuArray.filter((x) => x.location === city);
  stuByCity.map((x) => x.newGrades);
  return stuByCity;
}
