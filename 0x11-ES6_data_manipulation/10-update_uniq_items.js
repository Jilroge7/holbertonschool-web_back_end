export default function updateUniqueItems(groceryItems) {
  if (!(groceryItems instanceof Map)) {
    throw Error('Cannot process');
  }
  groceryItems.forEach((item, key) => {
    if (item === 1) {
      groceryItems.set(key, 100);
    }
  });
  return groceryItems;
}
