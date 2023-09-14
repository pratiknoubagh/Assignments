function calculateFactorial(number) {
  if (number < 0) {
    return "Factorial is not defined for negative numbers";
  }

  let factorial = 1;

  for (let i = 1; i <= number; i++) {
    factorial *= i;
  }

  return factorial;
}


const num = 7;
const result = calculateFactorial(num);
console.log(`The factorial of ${num} is: ${result}`);
