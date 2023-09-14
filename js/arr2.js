function findMaxAndMin(arr) {
    if (arr.length === 0) {
      return "The array is empty.";
    }
  
    let max = arr[0];
    let min = arr[0];
  
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] > max) {
        max = arr[i];
      }
      if (arr[i] < min) {
        min = arr[i];
      }
    }
  
    return { max, min };
  }
  
  const myArray = [12,45,89,39];
  const result = findMaxAndMin(myArray);
  console.log("Maximum value:", result.max);
  console.log("Minimum value:", result.min);
  