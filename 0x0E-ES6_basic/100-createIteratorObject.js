export default function createIteratorObject(report) {
  const iterate = [];
  for (const dept of Object.keys(report.allEmployees)) {
    iterate.push(...report.allEmployees[dept]);
  }
  return iterate;
}
