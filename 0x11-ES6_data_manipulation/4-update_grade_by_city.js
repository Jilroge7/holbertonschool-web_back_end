export default function updateStudentByCity(stuArray, city, newGrades) {
    if (!Array.isArray(stuArray)) {
        return [];
      }
    const stuByCity = stuArray.filter((x) => x.location === city);
    return stuByCity;
}