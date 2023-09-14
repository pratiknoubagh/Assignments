function removeDuplicate(arr) {
    const uniqueArray = [];
    const seen = new Set();
  
    for (const item of arr) {
      if (!seen.has(item)) {
        seen.add(item);
        uniqueArray.push(item);
      }
    }
  
    return uniqueArray;
  }
  
  
  const myArray = [4,7,8,3,56,4,7];
  const result = removeDuplicate(myArray);
  console.log(result); 
  