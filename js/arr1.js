function calculateArraySum(arr) {
    let sum = 0;
    
    for (let i = 0; i < arr.length; i++) {
      sum += arr[i];
    }
    
    return sum;
  }
  
  const Array = [5, 8, 4, 7, 10];
  const result = calculateArraySum(Array);
  console.log("Sum of array elements:", result);