export default function iterateThroughObject(reportWithIterator) {
  return {
    allEmployees: { ...reportWithIterator },
    getNumberOfDepartments: (employeesList) => Object.keys(employeesList).length,
  };
}
