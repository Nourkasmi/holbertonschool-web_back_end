const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');

    const lines = data.trim().split('\n');

    // Retirer l'en-tête (firstname,lastname,age,field)
    const headers = lines.shift();

    const studentsByField = {};
    let totalStudents = 0;

    for (const line of lines) {
      if (line.trim() === '') continue; // ignorer les lignes vides

      const [firstname, , , field] = line.split(',');

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }

      studentsByField[field].push(firstname);
      totalStudents += 1;
    }

    console.log(`Number of students: ${totalStudents}`);

    for (const [field, students] of Object.entries(studentsByField)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
