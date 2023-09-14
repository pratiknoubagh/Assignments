function filterEvenNumbers(numbers) {
    const evenNumbers = [];
  
    for (let i = 0; i < numbers.length; i++) {
      if (numbers[i] % 2 === 0) {
        evenNumbers.push(numbers[i]);
      }
    }
  
    return evenNumbers;
  }
  
  function filterOddNumbers(numbers) {
    const oddNumbers = [];
  
    for (let i = 0; i < numbers.length; i++) {
      if (numbers[i] % 2 !== 0) {
        oddNumbers.push(numbers[i]);
      }
    }
  
    return oddNumbers;
  }
  const numbers = [9,67,45,3,2,7,8];
  const evenNumbers = filterEvenNumbers(numbers);
  const oddNumbers = filterOddNumbers(numbers);
  
  console.log("Even numbers:", evenNumbers);
  console.log("Odd numbers:", oddNumbers);
  