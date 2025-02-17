package leetcode.metods;

public class L3289_TheTwoSneakyNumbersOfDigitville {

	public int[] getSneakyNumbers(int[] nums) {
		int[] sneakyNumbers = new int[2];
		int index = 0;
		for (int i = 0; i < nums.length; i++) {
			for (int j = i + 1; j < nums.length; j++) {
				if (nums[i] == nums[j]) {
					sneakyNumbers[index++] = nums[i];
				}
			}
		}
		return sneakyNumbers;
	}

}
