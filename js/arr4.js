function smallArray(arr, Size) {
    if (Size <= 0) {
      return "Chunk size must be greater than zero.";
    }
  
    const chunkedArray = [];
    for (let i = 0; i < arr.length; i += Size) {
      chunkedArray.push(arr.slice(i, i + Size));
    }
  
    return chunkedArray;
  }
  
 
  const myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  const Size = 2;
  const result = smallArray(myArray, Size);
  console.log(result);
  
  