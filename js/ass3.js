function isPalindrome(inputString) {
    
    const cleanString = inputString.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    
    
    let start = 0;
    let end = cleanString.length - 1;
    
    
    while (start < end) {
      if (cleanString[start] !== cleanString[end]) {
        
        return false;
      }
      start++;
      end--;
    }
    
    // If the loop completes without returning false, it's a palindrome
    return true;
  }
  
  // Example usage:
  const inputString1 = "racecar";
  const inputString2 = "Hello, World!";
  console.log(isPalindrome(inputString1)); // Output: true
  console.log(isPalindrome(inputString2)); // Output: false
  