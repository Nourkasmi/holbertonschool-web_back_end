// This function filters a set based on a start string
// and returns a joined string of the remaining parts

export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const filtered = [];

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      filtered.push(value.slice(startString.length));
    }
  }

  return filtered.join('-');
}
