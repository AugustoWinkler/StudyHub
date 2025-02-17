package leetcode.metods;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class L0704_BinarySearch {

	public int search(int[] nums, int target) {
		List<Integer> numList = new ArrayList<>();
		for (int num : nums) {
			numList.add(num);
		}

		if (!numList.contains(target))
			return -1;
		int result = Collections.binarySearch(numList, target);
		return Math.abs(result);
	}
}
