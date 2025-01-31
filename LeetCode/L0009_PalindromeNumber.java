package leetcode.metods;

public class L0009_PalindromeNumber {

	public boolean isPalindrome(int x) {
        if(x < 0) return false;
        
		String number = Integer.toString(x);
		
		if(number.equals(new StringBuilder(number).reverse().toString())) {
			return true;
		}
		
		return false;
	}
}
