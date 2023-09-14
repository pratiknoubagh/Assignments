function findFactorial(number) {
    if (number < 0) {
      return "Factorial is undefined";
    }
  
    let factorial = 1;
  
    for (let i = 1; i <= number; i++) {
      factorial *= i;
    }
  
    return factorial;
  }
  

  const num = 7;
  const result = findFactorial(num);
  console.log(`The factorial of ${num} is: ${result}`);
  